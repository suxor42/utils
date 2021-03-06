__author__ = 'suxor'
import socket

UDP = socket.SOCK_DGRAM
TCP = socket.SOCK_STREAM


class NetSender(object):
    _remoteserver = None
    _remoteport = None
    _soc = None

    def __init__(self, server, port, proto=TCP):
        self._remoteport = port
        self._remoteserver = server
        self._soc = socket.socket(socket.AF_INET, proto)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def connect(self):
        self._soc.connect((self._remoteserver, self._remoteport))

    def close(self):
        self._soc.shutdown(socket.SHUT_RDWR)
        self._soc.close()

    def send_data(self, data):
        self._soc.sendall(data)


class Graphite(NetSender):

    def __init__(self, server="127.0.0.1", port=2003):
        super(Graphite, self).__init__(server, port, TCP)

    def send_data(self, path, value, timestamp):
        super(Graphite, self).send_data(("%s %s %s\n" % (path, value, timestamp)).encode())


