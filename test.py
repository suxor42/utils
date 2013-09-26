__author__ = 'suxor'

import net
from mock import Mock

def test_graphite():
    net.graphite.connect = Mock()
    net.graphite.send_data = Mock(return_value=None)
    net.graphite.__exit__ = Mock()

    with net.graphite(server="localhost") as graphite:
        result = graphite.send_data("test",10000,10000)
        assert(result is None)
