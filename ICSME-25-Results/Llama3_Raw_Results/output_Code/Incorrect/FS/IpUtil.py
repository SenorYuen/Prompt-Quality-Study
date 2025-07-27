import socket
import netifaces
import ipaddress


class IpUtil:
    """
    This is a class as tool for ip that can be used to obtain the local IP address, validate its validity, and also provides the functionality to retrieve the corresponding hostname.
    """

    # Method to check if the given IP address is a valid IPv4 address
    @staticmethod
    def is_valid_ipv4(ip_address):
        # Try to create an IPv4Address object with the given IP address
        try:
            ipaddress.IPv4Address(ip_address)
            return True
        except ipaddress.AddressValueError:
            return False

    # Method to check if the given IP address is a valid IPv6 address
    @staticmethod
    def is_valid_ipv6(ip_address):
        # Try to create an IPv6Address object with the given IP address
        try:
            ipaddress.IPv6Address(ip_address)
            return True
        except ipaddress.AddressValueError:
            return False

    # Method to get the hostname associated with the given IP address
    @staticmethod
    def get_hostname(ip_address):
        # Try to get the hostname using the socket.gethostbyaddr method
        try:
            hostname, _, _ = socket.gethostbyaddr(ip_address)
            return hostname
        except socket.herror:
            # If the hostname cannot be found, return None
            return None