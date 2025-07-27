class IPAddress:
    """
    This is a class to process IP Address, including validating, getting the octets and obtaining the binary representation of a valid IP address.
    """

    def __init__(self, ip_address):
        """
        Initialize the IP address to the specified address
        :param ip_address:string
        """
        self.ip_address = ip_address

    def is_valid(self):
        """
        Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. 
        Each digit is greater than or equal to 0 and less than or equal to 255
        :return: bool
        """
        # Split the IP address into four parts
        parts = self.ip_address.split('.')
        
        # Check if the IP address has four parts
        if len(parts) != 4:
            return False
        
        # Check each part
        for part in parts:
            # Check if the part is a digit
            if not part.isdigit():
                return False
            
            # Convert the part to an integer
            num = int(part)
            
            # Check if the number is between 0 and 255
            if num < 0 or num > 255:
                return False
        
        # If all checks pass, the IP address is valid
        return True


    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; 
        otherwise, an empty list is returned
        :return: list
        """
        # Check if the IP address is valid
        if self.is_valid():
            # Split the IP address into four parts and return them as a list
            return self.ip_address.split('.')
        else:
            # If the IP address is not valid, return an empty list
            return []


    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        """
        # Check if the IP address is valid
        if self.is_valid():
            # Split the IP address into four parts
            parts = self.ip_address.split('.')
            
            # Convert each part to binary and format it to 8 bits
            binary_parts = [format(int(part), '08b') for part in parts]
            
            # Join the binary parts with '.' and return the result
            return '.'.join(binary_parts)
        else:
            # If the IP address is not valid, return an empty string
            return ''