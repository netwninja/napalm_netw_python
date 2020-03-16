import json
from napalm.base import get_network_driver
from getpass import getpass
import pdb
dest_node = input("target node ip: ")
node_driver = input("type the node driver type: ")
driver = get_network_driver(node_driver)
#dev = driver(hostname=dest_node, username='ansible', password='ansible123')
dev = driver(hostname=dest_node, username='ansible', password=getpass())
#pdb.set_trace()
dev.open()
facts_gather = dev.get_facts()
dev.close()
#print(json.dumps(facts_gather['os_version'], sort_keys=True, indent=4))
print('The node', dest_node, 'is running SOFTWARE', facts_gather['os_version'])
print()
