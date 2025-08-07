import xml.etree.ElementTree as ET


class XMLProcessor:
    def __init__(self, file_name):
        """
        Initialize the XMLProcessor object with the given file name.
        """
        self.file_name = file_name
        self.tree = None
        self.root = None

    def read_xml(self):
        """
        Reads the XML file and returns the root element.
        :return: Element, the root element of the XML file.
        """
        try:
            self.tree = ET.parse(self.file_name)
            self.root = self.tree.getroot()
            return self.root
        except ET.ParseError as e:
            print(f"Error parsing XML file: {e}")
            return None
        except FileNotFoundError:
            print(f"File not found: {self.file_name}")
            return None

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if self.tree is not None:
            try:
                self.tree.write(file_name)
                return True
            except Exception as e:
                print(f"Error writing XML file: {e}")
                return False
        else:
            print("No XML data to write.")
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        if self.root is not None:
            # Example processing: Add an attribute to each child of the root
            for elem in self.root:
                elem.set('processed', 'true')

            # Write the updated XML data to a new file
            return self.write_xml(file_name)
        else:
            print("No XML data to process.")
            return False

    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :return: list, a list of found elements with the specified name.
        """
        if self.root is not None:
            found_elements = self.root.findall(element_name)
            return found_elements
        else:
            print("No XML data to search.")
            return []