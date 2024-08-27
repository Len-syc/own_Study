class HK4E:
    def __init__(self,server:str,version:str,ip:str):
        self.server = server
        self.version = version
        self.ip = ip
    def __inner__(self)->str:
        return self.ip
###########################################################


class PS(HK4E):
    def __init__(self,server:str,version:str,ip:str):
        self.server = server
        self.version = version
        self.ip = ip




if __name__ == '__main__':
    office=HK4E('rel','1.0','192.168.3.11')
    private=PS('rel','1.0.5','127.0.0.1')
    print(private.__inner__())