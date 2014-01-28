__author__ = 'suxor'

import net
#from mock import Mock
import col
import collections


#def test_graphite():
#    net.Graphite.connect = Mock()
#    net.Graphite.send_data = Mock(return_value=None)
#    net.Graphite.__exit__ = Mock()
#
#    with net.Graphite(server="localhost") as graphite:
#        result = graphite.send_data("test", 10000, 10000)
#        assert (result is None)


dict = col.autodict()
#dict['lala']['blub'] = dict()
#dict['lala']['blub']['lala']['bla'] = 1
#test = dict['lala']['123']
#print(dict)
#print('123' in dict['lala'])

dict = {}
dict['1'] = 6
dict['bla'] = {}
dict = col.autodict(dict)
#dict = col.autodict(map(dict.transform, dict.traverse(dict)))
print dict
dict['lala']['blub']['5'] = 4
dict['bla']['lala']['4'] = 5
print dict
#for v in dict.traverse(dict):
#    print v
