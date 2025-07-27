class Server:
    def __init__(self):
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        if addr not in self.white_list:
            self.white_list.append(addr)
            return self.white_list
        else:
            return False

    def del_white_list(self, addr):
        if addr in self.white_list:
            self.white_list.remove(addr)
            return self.white_list
        else:
            return False

    def recv(self, info):
        if info["addr"] in self.white_list:
            self.receive_struct = info
            return info["content"]
        else:
            return False

    def send(self, info):
        self.send_struct = info
        return None

    def show(self, type):
        if type == 'send':
            return self.send_struct
        elif type == 'receive':
            return self.receive_struct
        else:
            return False