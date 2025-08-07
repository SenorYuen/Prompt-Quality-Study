import xml.etree.ElementTree as ET

class XMLProcessor:
    """
    This is a class as XML files handler, including reading, writing, processing as well as finding elements in a XML file.
    """

    def __init__(self, file_name):
        """
        Initialize the XMLProcessor object with the given file name.
        :param file_name:string, the name of the XML file to be processed.
        """
        self.file_name = file_name
        self.root = None

    def read_xml(self):
        """
        Reads the XML file and returns the root element.
        :return: Element, the root element of the XML file.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root_element = xml_processor.read_xml()
        >>> print(root_element)
        <Element 'root' at 0x7f8e3b7eb180>
        """
        try:
            # Parse the XML file and set the root element
            tree = ET.parse(self.file_name)
            self.root = tree.getroot()
            return self.root
        except Exception as e:
            # Return None if there is an error in parsing
            print(f"Error reading XML file: {e}")
            return None

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: string, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> success = xml_processor.write_xml('output.xml')
        >>> print(success)
        True
        """
        try:
            # Create an ElementTree object from the root and write it to a file
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except Exception as e:
            # Return False if there is an error in writing
            print(f"Error writing XML file: {e}")
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :param file_name: string, the name of the file to write the modified XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> success = xml_processor.process_xml_data('processed.xml')
        >>> print(success)
        True
        """
        try:
            # Iterate over each 'item' element and modify its text
            for element in self.root.iter('item'):
                if element.text:
                    element.text = element.text.upper()
            # Write the modified XML to the specified file
            return self.write_xml(file_name)
        except Exception as e:
            # Return False if there is an error in processing
            print(f"Error processing XML data: {e}")
            return False

    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_element('item')
        >>> for item in items:
        >>>     print(item.text)
        apple
        banana
        orange
        """
        try:
            # Find all elements with the specified name
            elements = self.root.findall(element_name)
            return elements
        except Exception as e:
            # Return an empty list if there is an error in finding elements
            print(f"Error finding elements: {e}")
            return []