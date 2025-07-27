import xml.etree.ElementTree as ET

class XMLProcessor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.root = None

    def read_xml(self):
        try:
            tree = ET.parse(self.file_name)
            self.root = tree.getroot()
            return self.root
        except FileNotFoundError:
            print("File not found.")
            return None
        except ET.ParseError:
            print("Error parsing XML file.")
            return None

    def write_xml(self, output_file_name):
        if self.root is not None:
            try:
                tree = ET.ElementTree(self.root)
                tree.write(output_file_name)
                return True
            except Exception as e:
                print(f"Error writing XML file: {e}")
                return False
        else:
            print("No XML data to write.")
            return False

    def process_xml_data(self, output_file_name):
        if self.root is not None:
            # Modify the data in XML elements
            for elem in self.root.iter():
                if elem.text:
                    elem.text = elem.text.upper()
            return self.write_xml(output_file_name)
        else:
            print("No XML data to process.")
            return False

    def find_element(self, element_name):
        if self.root is not None:
            return self.root.findall(".//{}".format(element_name))
        else:
            print("No XML data to search.")
            return []