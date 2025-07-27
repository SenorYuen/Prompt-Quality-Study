class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def is_valid(self):
        parts = self.ip_address.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            if not 0 <= int(part) <= 255:
                return False
        return True

    def get_octets(self):
        if self.is_valid():
            return self.ip_address.split('.')
        else:
            return []

    def get_binary(self):
        if self.is_valid():
            binary_parts = []
            for part in self.ip_address.split('.'):
                binary_part = bin(int(part))[2:].zfill(8)
                binary_parts.append(binary_part)
            return '.'.join(binary_parts)
        else:
            return ''