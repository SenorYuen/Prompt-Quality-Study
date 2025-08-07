class Server:

    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """
        self.whitelist = []  # List to store whitelisted addresses
        self.sent_info = {}  # Dictionary to store sent information
        self.received_info = {}  # Dictionary to store received information

    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :return: new whitelist, return False if the address already exists
        """
        if addr in self.whitelist:
            return False  # Address already exists in the whitelist
        self.whitelist.append(addr)  # Add address to the whitelist
        return self.whitelist  # Return updated whitelist

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist
        :return: new whitelist, return False if the address does not exist
        """
        if addr not in self.whitelist:
            return False  # Address does not exist in the whitelist
        self.whitelist.remove(addr)  # Remove address from the whitelist
        return self.whitelist  # Return updated whitelist

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :return: if successfully received, return the content of the information; otherwise, return False
        """
        addr, content = info['address'], info['content']
        if addr in self.whitelist:
            self.received_info[addr] = content  # Store received content
            return content  # Return the received content
        return False  # Address not in whitelist, do not receive

    def send(self, info):
        """
        Send information containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        """
        addr, content = info['address'], info['content']
        if addr in self.whitelist:
            self.sent_info[addr] = content  # Store sent content
            return  # Successfully sent, return nothing
        return "Error: Address not in whitelist"  # Error message if address not in whitelist

    def show(self, type):
        """
        Returns struct of the specified type
        :return: if type is equal to 'send' or 'receive', return the corresponding struct; otherwise, return False
        """
        if type == 'send':
            return self.sent_info  # Return sent information
        elif type == 'receive':
            return self.received_info  # Return received information
        return False  # Invalid type, return False