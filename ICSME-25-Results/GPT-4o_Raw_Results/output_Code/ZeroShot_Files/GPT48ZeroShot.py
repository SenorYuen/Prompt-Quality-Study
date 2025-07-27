class IpUtil:

    @staticmethod
    def is_valid_ipv4(ip_address):
        """
        Check if the given IP address is a valid IPv4 address.
        :return: bool, True if the IP address is valid, False otherwise
        """
        try:
            # Attempt to convert the IP address to a valid IPv4 address
            socket.inet_pton(socket.AF_INET, ip_address)
            return True
        except socket.error:
            return False

    @staticmethod
    def is_valid_ipv6(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :return: bool, True if the IP address is valid, False otherwise
        """
        try:
            # Attempt to convert the IP address to a valid IPv6 address
            socket.inet_pton(socket.AF_INET6, ip_address)
            return True
        except socket.error:
            return False

    @staticmethod
    def get_hostname(ip_address):
        """
        Get the hostname associated with the given IP address.
        :return: string, the hostname associated with the IP address
        """
        try:
            # Use gethostbyaddr to find the hostname for the given IP address
            hostname, _, _ = socket.gethostbyaddr(ip_address)
            return hostname
        except socket.herror:
            return None

    @staticmethod
    def get_local_ip():
        """
        Get the local IP address of the machine.
        :return: string, the local IP address
        """
        try:
            # Use netifaces to get the default gateway interface
            default_gateway = netifaces.gateways()['default'][netifaces.AF_INET][1]
            # Get the IP address associated with the default gateway interface
            local_ip = netifaces.ifaddresses(default_gateway)[netifaces.AF_INET][0]['addr']
            return local_ip
        except KeyError:
            return None