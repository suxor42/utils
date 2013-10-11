__author__ = 'suxor'
import socket

#graphite send_data
class graphite(object):
    __graphite_server = "localhost"
    __graphite_port = 2003
    __soc = None

    def __init__(self, port=2003, server="127.0.0.1"):
        self.__graphite_port = port
        self.__graphite_server = server
        self.__soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__soc.shutdown(socket.SHUT_RDWR)
        self.__soc.close()

    def connect(self):
        self.__soc.connect((self.__graphite_server, self.__graphite_port))

    def close(self):
        self.__soc.shutdown(socket.SHUT_RDWR)
        self.__soc.close()

    def send_data(self, path, value, timestamp):
        self.__soc

        #print "%s %s %s" % (path,value,timestamp)
        self.__soc.sendall(("%s %s %s\n" % (path, value, timestamp)).encode())
        #__soc.flush()
        #__soc.close()
