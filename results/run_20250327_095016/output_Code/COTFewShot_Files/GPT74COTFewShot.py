class Server:
    def __init__(self):
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        if addr not in self.white_list:
            self.white_list.append(addr)
            return self.white_list
        return False

    def del_white_list(self, addr):
        if addr in self.white_list:
            self.white_list.remove(addr)
            return self.white_list
        return False

    def recv(self, info):
        addr = info.get('addr')
        content = info.get('content')
        if addr in self.white_list:
            self.receive_struct = {"addr": addr, "content": content}
            return content
        return False

    def send(self, info):
        try:
            addr = info.get('addr')
            content = info.get('content')
            self.send_struct = {"addr": addr, "content": content}
        except:
            return "Error in sending information"

    def show(self, type):
        if type == 'send':
            return self.send_struct
        elif type == 'receive':
            return self.receive_struct
        return False