import socket


class IpUtil:
    @staticmethod
    def is_valid_ipv4(ip_address):
        try:
            socket.inet_pton(socket.AF_INET, ip_address)
            return True
        except socket.error:
            return False

    @staticmethod
    def is_valid_ipv6(ip_address):
        try:
            socket.inet_pton(socket.AF_INET6, ip_address)
            return True
        except socket.error:
            return False

    @staticmethod
    def get_hostname(ip_address):
        try:
            return socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            return None

    @staticmethod
    def get_binary(ip_address):
        try:
            if IpUtil.is_valid_ipv4(ip_address):
                return bin(int.from_bytes(socket.inet_pton(socket.AF_INET, ip_address), 'big'))
            elif IpUtil.is_valid_ipv6(ip_address):
                return bin(int.from_bytes(socket.inet_pton(socket.AF_INET6, ip_address), 'big'))
            else:
                return None
        except socket.error:
            return None