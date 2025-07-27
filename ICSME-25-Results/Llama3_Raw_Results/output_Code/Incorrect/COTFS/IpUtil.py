import socket
import ipaddress


class IpUtil:
    @staticmethod
    def is_valid_ipv4(ip_address):
        try:
            ipaddress.IPv4Address(ip_address)
            return True
        except ipaddress.AddressValueError:
            return False

    @staticmethod
    def is_valid_ipv6(ip_address):
        try:
            ipaddress.IPv6Address(ip_address)
            return True
        except ipaddress.AddressValueError:
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
                return ipaddress.IPv4Address(ip_address).packed
            elif IpUtil.is_valid_ipv6(ip_address):
                return ipaddress.IPv6Address(ip_address).packed
            else:
                return None
        except ipaddress.AddressValueError:
            return None