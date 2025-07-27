# This is a class as tool for ip that can be used to obtain the local IP address, validate its validity, and also provides the functionality to retrieve the corresponding hostname.

import socket
import netifaces
import ipaddress


class IpUtil:

    # Check if the given IP address is a valid IPv4 address.
    @staticmethod
    def is_valid_ipv4(ip_address):
        """
        Check if the given IP address is a valid IPv4 address.
        :return: bool, True if the IP address is valid, False otherwise
        """
        try:
            # Attempt to create an IPv4 address object
            ipaddress.IPv4Address(ip_address)
            return True
        except ipaddress.AddressValueError:
            # If the address is not valid, return False
            return False

    # Check if the given IP address is a valid IPv6 address.
    @staticmethod
    def is_valid_ipv6(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :return: bool, True if the IP address is valid, False otherwise
        """
        try:
            # Attempt to create an IPv6 address object
            ipaddress.IPv6Address(ip_address)
            return True
        except ipaddress.AddressValueError:
            # If the address is not valid, return False
            return False

    # Get the hostname associated with the given IP address.
    @staticmethod
    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
        :return: string, the hostname associated with the IP address
        """
        try:
            # Use the socket.gethostbyaddr function to get the hostname
            hostname, _, _ = socket.gethostbyaddr(ip_address)
            return hostname
        except socket.herror:
            # If the hostname cannot be found, return None
            return None


# Example usage
if __name__ == "__main__":
    ip_address = "8.8.8.8"
    print(f"Is {ip_address} a valid IPv4 address? {IpUtil.is_valid_ipv4(ip_address)}")
    print(f"Is {ip_address} a valid IPv6 address? {IpUtil.is_valid_ipv6(ip_address)}")
    print(f"The hostname for {ip_address} is: {IpUtil.get_hostname(ip_address)}")