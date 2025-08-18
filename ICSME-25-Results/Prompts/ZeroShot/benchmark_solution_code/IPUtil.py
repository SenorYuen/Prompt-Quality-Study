'''
# This is a class as tool for ip that can be used to obtain the local IP address, validate its validity, and also provides the functionality to retrieve the corresponding hostname.

import socket
import netifaces


class IpUtil:

    @staticmethod
    def is_valid_ipv4(ip_address):
        """
        Check if the given IP address is a valid IPv4 address.
        :return: bool, True if the IP address is valid, False otherwise
        """

    @staticmethod
    def is_valid_ipv6(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :return:bool, True if the IP address is valid, False otherwise
        """


    @staticmethod
    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
        :return: string, the hostname associated with the IP address
        """


'''

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
            hostname = socket.gethostbyaddr(ip_address)[0]
            return hostname
        except socket.herror:
            return None


