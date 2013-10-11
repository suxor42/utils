__author__ = 'suxor'

import net
from mock import Mock


def test_graphite():
    net.Graphite.connect = Mock()
    net.Graphite.send_data = Mock(return_value=None)
    net.Graphite.__exit__ = Mock()

    with net.Graphite(server="localhost") as graphite:
        result = graphite.send_data("test", 10000, 10000)
        assert (result is None)
