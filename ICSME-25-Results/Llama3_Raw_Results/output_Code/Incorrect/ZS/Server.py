class Server:
    # Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
    def __init__(self):
        # Initialize the whitelist as an empty list
        self.white_list = []
        # Initialize the sending and receiving information as an empty dictionary
        self.send_info = {}
        self.recv_info = {}

    # Add an address to the whitelist and do nothing if it already exists
    def add_white_list(self, addr):
        # Check if the address already exists in the whitelist
        if addr not in self.white_list:
            # Add the address to the whitelist
            self.white_list.append(addr)
            # Return the new whitelist
            return self.white_list
        else:
            # Return False if the address already exists
            return False

    # Remove an address from the whitelist and do nothing if it does not exist
    def del_white_list(self, addr):
        # Check if the address exists in the whitelist
        if addr in self.white_list:
            # Remove the address from the whitelist
            self.white_list.remove(addr)
            # Return the new whitelist
            return self.white_list
        else:
            # Return False if the address does not exist
            return False

    # Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
    def recv(self, info):
        # Extract the address from the information
        addr = info['addr']
        # Extract the content from the information
        content = info['content']
        # Check if the address is on the whitelist
        if addr in self.white_list:
            # Receive the content and store it in the receiving information dictionary
            self.recv_info[addr] = content
            # Return the content of the information
            return content
        else:
            # Return False if the address is not on the whitelist
            return False

    # Send information containing address and content
    def send(self, info):
        # Extract the address from the information
        addr = info['addr']
        # Extract the content from the information
        content = info['content']
        # Try to send the information
        try:
            # Store the sent information in the sending information dictionary
            self.send_info[addr] = content
            # Return nothing if successfully sent
            return None
        except Exception as e:
            # Return an error message if failed to send
            return f"Error: {str(e)}"

    # Returns struct of the specified type
    def show(self, type):
        # Check if the type is 'send'
        if type == 'send':
            # Return the sending information dictionary
            return self.send_info
        # Check if the type is 'receive'
        elif type == 'receive':
            # Return the receiving information dictionary
            return self.recv_info
        else:
            # Return False if the type is neither 'send' nor 'receive'
            return False