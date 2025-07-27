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
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")
            return None

    def write_xml(self, file_name):
        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            print(f"Error writing XML: {e}")
            return False

    def process_xml_data(self, file_name):
        try:
            # Example process: Change all 'item' elements' text to uppercase
            for item in self.root.iter('item'):
                item.text = item.text.upper()
            return self.write_xml(file_name)
        except Exception as e:
            print(f"Error processing XML data: {e}")
            return False

    def find_element(self, element_name):
        try:
            return self.root.findall(f".//{element_name}")
        except Exception as e:
            print(f"Error finding elements: {e}")
            return []