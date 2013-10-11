__author__ = 'suxor'
import socket


class NetSender(object):
    _remoteserver = None
    _remoteport = None
    _soc = None
    __proto = {'TCP':socket.SOCK_STREAM, 'UDP': socket.SOCK_DGRAM}

    def __init__(self, server, port, proto='TCP'):
        self._remoteport = port
        self._remoteserver = server
        self._soc = socket.socket(socket.AF_INET, self.__proto[proto])

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self):
        self.close()

    def connect(self):
        self._soc.connect((self._remoteserver, self._remoteport))

    def close(self):
        self.__soc.shutdown(socket.SHUT_RDWR)
        self.__soc.close()

    def send_data(self, data):
        self._soc.sendall(data)


class Graphite(NetSender):

    def __init__(self, server="127.0.0.1", port=2003):
        super(Graphite, self).__init__(server, port, 'TCP')

    def send_data(self, path, value, timestamp):
        super(Graphite, self).send_data(("%s %s %s\n" % (path, value, timestamp)).encode())
