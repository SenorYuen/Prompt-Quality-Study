class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def is_valid(self):
        octets = self.ip_address.split('.')
        if len(octets) != 4:
            return False
        for octet in octets:
            if not octet.isdigit():
                return False
            num = int(octet)
            if num < 0 or num > 255:
                return False
        return True

    def get_octets(self):
        if self.is_valid():
            return self.ip_address.split('.')
        return []

    def get_binary(self):
        if not self.is_valid():
            return ''
        octets = self.get_octets()
        binary_octets = [format(int(octet), '08b') for octet in octets]
        return '.'.join(binary_octets)