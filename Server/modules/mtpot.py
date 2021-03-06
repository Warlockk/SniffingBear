from yapsy.IPlugin import IPlugin
import socket

class TELNETTest():
    """Name"""
    __name = "mtpot telnet Banner Test"

    """ Description """
    __description = "Test for service (telnet) banner of mtpot"

    """ Port nedded on the test"""
    __port = [23, 992]

    @staticmethod
    def get_name():
        return TELNETTest.__name

    @staticmethod
    def get_description():
        return TELNETTest.__description

    @staticmethod
    def get_port():
        return TELNETTest.__port

    @staticmethod
    def run(ip):
        banners = [
            b'\xff\xfb\x01\xff\xfb\x03\xff\xfc\'\xff\xfe\x01\xff\xfd\x03\xff\xfe"\xff\xfd\'\xff\xfd\x18\xff\xfe\x1f'
            b'\xff\xfb\x01\xff\xfb\x03'
            b'\xff\xfb\x01'
        ]

        for j in TELNETTest.__port:
            try:
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                soc.settimeout(2)
                soc.connect((ip, j))

                max_length = len(banners[0])

                for i in banners:
                    if max_length < len(i):
                        max_length = len(i)

                r = soc.recv(max_length)
                soc.close()
                for i in banners:
                    if i in r:
                        return True  
            except socket.error:
                pass
        return False


class MtPot(IPlugin):

    """ List of tests """
    __test_list = [TELNETTest]

    @staticmethod
    def get_test_list():
        return MtPot.__test_list

    @staticmethod
    def get_port_list():
        port_list = set()

        for i in MtPot.__test_list:
            port_list.update(i.get_port())
        return port_list

    @staticmethod
    def run(ip):
        list = []
        for i in MtPot.__test_list:
            list.append(i.run(ip))
        return list
