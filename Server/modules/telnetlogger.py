from yapsy.IPlugin import IPlugin
import socket

class TELNETTest():
    """Name"""
    __name = "telnetlogger telnet Banner Test"

    """ Description """
    __description = "Test for service (telnet) banner of telnetlogger"

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
            b'\xff\xfb\x03\xff\xfb\x01\xff\xfd\x1f\xff\xfd\x18\r\nlogin: '
        ]

        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.settimeout(2)
            for j in TELNETTest.__port:
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
            return False
        except socket.error: 
            return False


class TelnetLogger(IPlugin):

    """ List of tests """
    __test_list = [TELNETTest]

    @staticmethod
    def get_test_list():
        return TelnetLogger.__test_list

    @staticmethod
    def get_port_list():
        port_list = set()

        for i in TelnetLogger.__test_list:
            port_list.update(i.get_port())
        return port_list

    @staticmethod
    def run(ip):
        list = []
        for i in TelnetLogger.__test_list:
            list.append(i.run(ip))
        return list
