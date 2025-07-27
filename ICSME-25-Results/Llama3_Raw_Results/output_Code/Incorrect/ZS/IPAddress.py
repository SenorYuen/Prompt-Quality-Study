class IPAddress:
    def __init__(self, ip_address):
        # Initialize the IP address to the specified address
        self.ip_address = ip_address

    def is_valid(self):
        # Split the IP address into four parts
        parts = self.ip_address.split('.')
        
        # Check if the IP address has four parts
        if len(parts) != 4:
            return False
        
        # Check each part of the IP address
        for part in parts:
            # Check if the part is a digit
            if not part.isdigit():
                return False
            
            # Convert the part to an integer
            num = int(part)
            
            # Check if the number is between 0 and 255
            if num < 0 or num > 255:
                return False
            
            # Check if the number has a leading zero
            if len(part) > 1 and part[0] == '0':
                return False
        
        # If all checks pass, the IP address is valid
        return True


    def get_octets(self):
        # Check if the IP address is valid
        if not self.is_valid():
            return []
        
        # Split the IP address into four parts and convert each part to an integer
        return [int(part) for part in self.ip_address.split('.')]


    def get_binary(self):
        # Check if the IP address is valid
        if not self.is_valid():
            return ''
        
        # Split the IP address into four parts
        parts = self.ip_address.split('.')
        
        # Convert each part to binary and remove the '0b' prefix
        binary_parts = [bin(int(part))[2:].zfill(8) for part in parts]
        
        # Join the binary parts with '.'
        return '.'.join(binary_parts)