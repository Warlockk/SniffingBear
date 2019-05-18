from yapsy.IPlugin import IPlugin
import socket

class FTPTest():
    """Name"""
    __name = "dionaea FTP Banner Test"

    """ Description """
    __description = "Test for service banner of dionaea"

    """ Port nedded on the test"""
    __port = [20, 21, 989, 990]

    @staticmethod
    def get_name():
        return FTPTest.__name

    @staticmethod
    def get_description():
        return FTPTest.__description

    @staticmethod
    def get_port():
        return FTPTest.__port

    @staticmethod
    def run(ip):
        banners = [
            b'220 Welcome to my FTP Server\r\n'
        ]

        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.settimeout(2)
            for j in FTPTest.__port:
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
        except socket.timeout: 
            print("conexao deu timeout")

class IMAPTest():
    """Name"""
    __name = "amun IMAP Banner Test"

    """ Description """
    __description = "Test for service banner (IMAP) of amun"

    """ Port nedded on the test"""
    __port = [993, 143, 220]

    @staticmethod
    def get_name():
        return IMAPTest.__name

    @staticmethod
    def get_description():
        return IMAPTest.__description

    @staticmethod
    def get_port():
        return IMAPTest.__port

    @staticmethod
    def run(ip):
        banners = [
            b'a200 Lotus Domino 6.5.4 7.0.2 IMAP4\r\n'
        ]

        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.settimeout(2)
            for j in IMAPTest.__port:
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
        except socket.timeout: 
            print("conexao deu timeout")

class SMTPTest():
    """Name"""
    __name = "amun SMTP Banner Test"

    """ Description """
    __description = "Test for service banner (SMTP) of amun"

    """ Port nedded on the test"""
    __port = [587, 25, 366, 465]

    @staticmethod
    def get_name():
        return SMTPTest.__name

    @staticmethod
    def get_description():
        return SMTPTest.__description

    @staticmethod
    def get_port():
        return SMTPTest.__port

    @staticmethod
    def run(ip):
        banners = [
            b'220 mail.example.com SMTP Mailserver\r\n'
        ]

        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.settimeout(2)
            for j in SMTPTest.__port:
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
        except socket.timeout: 
            print("conexao deu timeout")

class Amun(IPlugin):

    """ List of tests """
    __test_list = [FTPTest,IMAPTest,SMTPTest]

    @staticmethod
    def get_test_list():
        return Amun.__test_list

    @staticmethod
    def get_port_list():
        port_list = set()

        for i in Amun.__test_list:
            port_list.update(i.get_port())
        return port_list

    @staticmethod
    def run(ip):
        for i in Amun.__test_list:
            i.run(ip)
