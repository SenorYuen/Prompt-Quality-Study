# analyze_gpt_files.py
import pandas as pd
import re

def analyze_csv(file_path, output_file):
    # Load the CSV file
    df = pd.read_csv(file_path)
    print("CSV file loaded.")
    
    # Step 1: Filter rows where "Name" ends with ".py"
    df_py = df[df["Name"].str.endswith("")].copy()
    print(f"Filtered .py files: {len(df_py)} rows remaining.")
    
    if df_py.empty:
        print("No .py files found. Exiting.")
        return
    
    # Step 2: Extract [number] and [COT or something] from the "Name" column
    def extract_parts(name):
        match = re.match(r"GPT(\d+)([A-Za-z]+)\.", name)
        if match:
            number, category = match.groups()
            return int(number), category
        return None, None
    
    df_py["Number"], df_py["Category"] = zip(*df_py["Name"].map(extract_parts))
    
    # Drop rows where extraction failed
    df_py.dropna(subset=["Number", "Category"], inplace=True)
    print(f"After extraction: {len(df_py)} valid rows remaining.")
    
    # if df_py.empty:
    #     print("No valid GPT[Number][Category] patterns found. Exiting.")
    #     return
    
    # Convert "Number" to integer
    df_py["Number"] = df_py["Number"].astype(int)
    
    # Ensure only numeric columns are used for averaging
    numeric_cols = df_py.select_dtypes(include=["number"]).columns
    print(f"Numeric columns for averaging: {list(numeric_cols)}")
    
    # Step 3: Compute averages grouped by "Number"
    avg_by_number = df_py.groupby("Number")[numeric_cols].mean()
    print(f"Computed averages by Number: {avg_by_number.shape}")
    
    # Step 4: Compute stats grouped by "Category"
    agg_funcs = ["mean", "min", "max", "median"]
    stats_by_category = df_py.groupby("Category")[numeric_cols].agg(agg_funcs)
    print(f"Computed stats by Category: {stats_by_category.shape}")
    
    # Step 5: Store results in a CSV file
    if not avg_by_number.empty:
        avg_by_number.to_csv(f"{output_file}_by_number.csv")
        print(f"Saved {output_file}_by_number.csv")
    else:
        print("No data to save for averages by Number.")
    
    if not stats_by_category.empty:
        stats_by_category.to_csv(f"{output_file}_stats_by_category.csv")
        print(f"Saved {output_file}_stats_by_category.csv")
    else:
        print("No data to save for stats by Category.")
    
    print("Processing complete.")

if __name__ == "__main__":
    file_path = "input"
    output_file = "output_results_good_final"  # Replace with desired output filename prefix
    analyze_csv(file_path, output_file)
