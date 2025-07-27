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
        if IpUtil.is_valid_ipv4(ip_address):
            return '.'.join(format(int(part), '08b') for part in ip_address.split('.'))
        elif IpUtil.is_valid_ipv6(ip_address):
            return ':'.join(format(int(part, 16), '016b') for part in ip_address.split(':'))
        else:
            return None