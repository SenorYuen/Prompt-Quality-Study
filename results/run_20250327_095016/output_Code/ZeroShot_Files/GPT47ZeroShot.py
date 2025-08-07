class IPAddress:
    def __init__(self, ip_address):
        """
        Initialize the IP address to the specified address
        """
        self.ip_address = ip_address

    def is_valid(self):
        """
        Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. 
        Each digit is greater than or equal to 0 and less than or equal to 255
        :return: bool
        """
        # Split the IP address by '.'
        octets = self.ip_address.split('.')
        
        # Check if the IP address has exactly four parts
        if len(octets) != 4:
            return False
        
        for octet in octets:
            # Check if each part is a digit and convert to integer
            if not octet.isdigit():
                return False
            num = int(octet)
            
            # Check if each number is in the range of 0 to 255
            if num < 0 or num > 255:
                return False
        
        return True

    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; 
        otherwise, an empty list is returned
        :return: list
        """
        if self.is_valid():
            # Split the valid IP address and return the list of octets as integers
            return [int(octet) for octet in self.ip_address.split('.')]
        else:
            return []

    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        """
        if self.is_valid():
            # Convert each octet to an 8-bit binary string and join them with '.'
            return '.'.join(format(int(octet), '08b') for octet in self.ip_address.split('.'))
        else:
            return ''