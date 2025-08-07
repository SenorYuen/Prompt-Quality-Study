'''
# This is a class as XML files handler, including reading, writing, processing as well as finding elements in a XML file.

import xml.etree.ElementTree as ET


class XMLProcessor:
    def __init__(self, file_name):
        """
        Initialize the XMLProcessor object with the given file name.
        """

    def read_xml(self):
        """
        Reads the XML file and returns the root element.
        :return: Element, the root element of the XML file.
        """


    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :return: bool, True if the write operation is successful, False otherwise.
        """


    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :return: bool, True if the write operation is successful, False otherwise.
        """


    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :return: list, a list of found elements with the specified name.
        """

'''

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
        except:
            return None

    def write_xml(self, file_name):
        try:
            tree = ET.ElementTree(self.root)
            tree.write(file_name)
            return True
        except:
            return False

    def process_xml_data(self, file_name):
        for element in self.root.iter('item'):
            text = element.text
            element.text = text.upper()
        return self.write_xml(file_name)

    def find_element(self, element_name):
        elements = self.root.findall(element_name)
        return elements


