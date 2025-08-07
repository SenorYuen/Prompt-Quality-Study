import os
import sys
import importlib
import unittest
import glob
import re
import argparse
import inspect
import importlib.util
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def find_runs(pattern=None):
    """Find all or filtered run directories."""
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    run_dirs = glob.glob(os.path.join(results_dir, "run_*"))

    if pattern:
        run_dirs = [d for d in run_dirs if re.search(pattern, os.path.basename(d))]

    # Sort by timestamp
    run_dirs = sorted(
        run_dirs,
        key=lambda x: (
            re.search(r"run_(\d+)", x).group(1) if re.search(r"run_(\d+)", x) else ""
        ),
    )

    return run_dirs


def find_classes_in_module(module):
    """Find all classes in a module."""
    return {
        name: obj
        for name, obj in inspect.getmembers(module, inspect.isclass)
        if obj.__module__ == module.__name__
    }


def discover_output_classes(run_dir):
    """Discover all classes in output_Code directory of a run."""
    output_code_dir = os.path.join(run_dir, "output_Code")
    if not os.path.exists(output_code_dir):
        return {}

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.append(parent_dir)

    classes = {}
    for py_file in glob.glob(os.path.join(output_code_dir, "*.py")):
        module_name = os.path.basename(py_file)[:-3]
        module_path = f"results.{os.path.basename(run_dir)}.output_Code.{module_name}"

        try:
            module = importlib.import_module(module_path)
            module_classes = find_classes_in_module(module)
            classes.update(
                {name: (module_path, cls) for name, cls in module_classes.items()}
            )
        except Exception as e:
            logger.warning(f"Could not import {module_path}: {e}")

    return classes


def get_test_files_for_class(class_name):
    """Find test files for a given class."""

    # First, look for exact class name file
    test_file = os.path.join("tests", f"test_{class_name.lower()}.py")
    return [test_file] if os.path.exists(test_file) else None


def extract_test_class_names(test_file):
    """Extract test class names from a test file."""
    with open(test_file, "r") as f:
        content = f.read()

    # Find all class definitions that inherit from unittest.TestCase
    class_pattern = r"class\s+(\w+)\s*\(\s*(?:unittest\.)?TestCase\s*\)"
    return re.findall(class_pattern, content)


def run_tests_for_class(run_dir, class_name, verbose=True):
    """Run tests for a specific class from a specific run."""
    classes = discover_output_classes(run_dir)

    if class_name not in classes:
        if verbose:
            logger.info(f"Class '{class_name}' not found in {run_dir}")
        return False

    module_path, target_class = classes[class_name]

    # Look for test files
    test_files = get_test_files_for_class(class_name)
    print(test_files)
    if not test_files:
        if verbose:
            logger.info(f"No test files found for {class_name}")
        return False

    success = True

    for test_file in test_files:
        if verbose:
            logger.info(f"Running tests from {os.path.basename(test_file)}")

        # Extract test class names from the file
        test_class_names = extract_test_class_names(test_file)

        if not test_class_names:
            if verbose:
                logger.info(f"  No test classes found in {os.path.basename(test_file)}")
            continue

        # Create a new module namespace for tests to run in
        spec = importlib.util.spec_from_file_location(
            f"test_{class_name}_{os.path.basename(test_file)[:-3]}", test_file
        )

        if spec is None:
            if verbose:
                logger.info(f"  Cannot create module spec for {test_file}")
            continue

        test_module = importlib.util.module_from_spec(spec)

        # Add globals to the module
        test_module.__dict__[class_name] = target_class

        # Execute the module code
        try:
            spec.loader.exec_module(test_module)
        except Exception as e:
            if verbose:
                logger.info(f"  Error loading test module: {e}")
            success = False
            continue

        # Run test classes from the test module
        for test_class_name in test_class_names:
            if not hasattr(test_module, test_class_name):
                if verbose:
                    logger.info(f"  Test class {test_class_name} not found in module")
                continue

            test_class = getattr(test_module, test_class_name)

            # Make sure it's really a TestCase
            if not issubclass(test_class, unittest.TestCase):
                continue

            if verbose:
                logger.info(f"  Running test case: {test_class_name}")

            # Create test suite
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromTestCase(test_class)

            # Run tests
            runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
            result = runner.run(suite)

            if not result.wasSuccessful():
                success = False

    return success


def discover_all_test_files():
    """Discover all test files in the src/tests directory."""
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_path = os.path.join(parent_dir, "src", "tests")

    return glob.glob(os.path.join(test_path, "*.py"))


def main():
    parser = argparse.ArgumentParser(
        description="Run tests for classes in output_Code directories"
    )
    parser.add_argument(
        "--run", help="Specific run ID or pattern to search for (e.g., '20241022')"
    )
    parser.add_argument("--class", dest="class_name", help="Specific class to test")
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available runs and classes that can be tested",
    )
    parser.add_argument(
        "--all", action="store_true", help="Run tests for all classes in the latest run"
    )
    parser.add_argument(
        "--quiet", action="store_true", help="Reduce verbosity of output"
    )

    args = parser.parse_args()
    verbose = not args.quiet

    # Find appropriate runs
    runs = find_runs(args.run)
    if not runs:
        logger.error("No runs found matching the pattern.")
        return

    # Use latest run if not explicitly specified
    run_dir = runs[-1]
    if verbose:
        logger.info(f"Using run: {os.path.basename(run_dir)}")

    if args.list:
        for run_dir in runs:
            logger.info(f"Run: {os.path.basename(run_dir)}")
            classes = discover_output_classes(run_dir)
            if classes:
                logger.info("  Classes:")
                for class_name, (module_path, _) in classes.items():
                    test_files = get_test_files_for_class(class_name)
                    test_status = "Has tests" if test_files else "No tests found"
                    logger.info(f"    - {class_name} ({test_status}) from {module_path}")
                    if test_files and verbose:
                        for tf in test_files:
                            logger.info(f"      Test File: {os.path.basename(tf)}")
                logger.info(f"Number of classes that can be tested: {len(classes)}")
            else:
                logger.info("  No classes found.")
            logger.info("")
        return

    elif args.all:
        # Run tests for all classes
        classes = discover_output_classes(run_dir)
        if not classes:
            logger.info("No classes found.")
            return

        success = True
        for class_name in classes:
            if verbose:
                logger.info(f"\nRunning tests for {class_name}...")
            if not run_tests_for_class(run_dir, class_name, verbose):
                success = False

        sys.exit(0 if success else 1)

    elif args.class_name:
        # Run tests for specific class

        success = run_tests_for_class(run_dir, args.class_name, verbose)
        sys.exit(0 if success else 1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
