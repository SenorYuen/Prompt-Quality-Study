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
        Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. Each digit is greater than or equal to 0 and less than or equal to 255
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
        # Split the IP address into its components
        parts = self.ip_address.split('.')
        
        # Check if there are exactly four parts
        if len(parts) != 4:
            return False
        
        for part in parts:
            # Check if each part is a digit and within the range 0 to 255
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
        
        return True

    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
        # Return the octets if the IP address is valid
        if self.is_valid():
            return self.ip_address.split('.')
        return []

    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """
        if not self.is_valid():
            return ''

        # Convert each octet to its binary representation, zero-padded to 8 bits
        octets = self.get_octets()
        binary_octets = ['{:08b}'.format(int(octet)) for octet in octets]
        
        # Join the binary octets with dots
        return '.'.join(binary_octets)