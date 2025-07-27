class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def is_valid(self):
        parts = self.ip_address.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            if not 0 <= int(part) <= 255:
                return False
        return True

    def get_octets(self):
        if not self.is_valid():
            return []
        return self.ip_address.split(".")

    def get_binary(self):
        if not self.is_valid():
            return ''
        binary_parts = []
        for part in self.ip_address.split("."):
            binary_part = format(int(part), '08b')
            binary_parts.append(binary_part)
        return ".".join(binary_parts)