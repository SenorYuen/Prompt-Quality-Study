import xml.etree.ElementTree as ET

class XMLProcessor:
    def __init__(self, file_name):
        # Initialize the XMLProcessor object with the given file name
        self.file_name = file_name
        self.root = None
        try:
            # Attempt to parse the XML file
            self.tree = ET.parse(file_name)
            self.root = self.tree.getroot()
        except FileNotFoundError:
            # Handle the case where the file does not exist
            print(f"File {file_name} not found.")
        except ET.ParseError:
            # Handle the case where the file is not a valid XML
            print(f"File {file_name} is not a valid XML.")

    def read_xml(self):
        # Reads the XML file and returns the root element
        return self.root

    def write_xml(self, file_name):
        # Writes the XML data to the specified file
        if self.root is not None:
            self.tree.write(file_name)
            return True
        else:
            return False

    def process_xml_data(self, file_name):
        # Modifies the data in XML elements and writes the updated XML data to a new file
        # For demonstration purposes, we'll modify the text of all elements
        if self.root is not None:
            for elem in self.root.iter():
                # Modify the text of each element
                elem.text = "Modified"
            self.tree.write(file_name)
            return True
        else:
            return False

    def find_element(self, element_name):
        # Finds the XML elements with the specified name
        if self.root is not None:
            # Use the findall method to find all elements with the specified name
            return self.root.findall(".//{}".format(element_name))
        else:
            return []

# Example usage:
if __name__ == "__main__":
    processor = XMLProcessor("example.xml")
    root = processor.read_xml()
    print("Root element:", root.tag)

    # Write the XML data to a new file
    processor.write_xml("new_example.xml")

    # Process the XML data and write it to a new file
    processor.process_xml_data("processed_example.xml")

    # Find elements with a specific name
    elements = processor.find_element("element")
    print("Found elements:")
    for elem in elements:
        print(elem.tag, elem.text)