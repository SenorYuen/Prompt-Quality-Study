class Server:
    """
    This is a class as a server, which handles a white list, message sending and receiving, and information display.
    """

    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """
        # Initialize an empty whitelist and empty dictionaries for sending and receiving information
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: new whitelist, return False if the address already exists
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """
        # Check if the address already exists in the whitelist
        if addr not in self.white_list:
            # Add the address to the whitelist
            self.white_list.append(addr)
            # Return the updated whitelist
            return self.white_list
        else:
            # Return False if the address already exists
            return False

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist
        :param addr: int, address to be deleted
        :return: new whitelist, return False if the address does not exist
        >>> server.add_white_list(88)
        >>> server.del_white_list(88)
        []
        """
        # Check if the address exists in the whitelist
        if addr in self.white_list:
            # Remove the address from the whitelist
            self.white_list.remove(addr)
            # Return the updated whitelist
            return self.white_list
        else:
            # Return False if the address does not exist
            return False

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the information; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
        # Check if the address is in the whitelist
        if info["addr"] in self.white_list:
            # Receive the content and update the receive_struct dictionary
            self.receive_struct = info
            # Return the received content
            return info["content"]
        else:
            # Return False if the address is not in the whitelist
            return False

    def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
        # Update the send_struct dictionary with the sent information
        self.send_struct = info
        # No return value if successfully sent

    def show(self, type):
        """
        Returns struct of the specified type
        :param type: string, the type of struct to be returned, which can be 'send' or 'receive'
        :return: if type is equal to 'send' or 'receive', return the corresponding struct; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        >>> server.send({"addr":66,"content":"ABC"})
        >>> server.show("send")
        {"addr":66,"content":"ABC"}
        """
        # Check the type of struct to return
        if type == "send":
            # Return the send_struct dictionary
            return self.send_struct
        elif type == "receive":
            # Return the receive_struct dictionary
            return self.receive_struct
        else:
            # Return False if the type is neither 'send' nor 'receive'
            return False