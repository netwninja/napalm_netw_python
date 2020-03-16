import json
from napalm import get_network_driver
dest_node = input("target node ip: ")
neigh_ip = input("type the BGP neighbor ip: ")
node_driver = input("type target node driver type: ")
attribute = input('type one of the following: is_up or description or remote_as ')
driver = get_network_driver(node_driver)
dev = driver(hostname=dest_node, username='ansible', password='ansible123')
dev.open()
dev_info = dev.get_bgp_neighbors()
dev.close()
dict = dev_info['global']['peers'][neigh_ip][attribute]
print(json.dumps(dict, sort_keys=True, indent=4)) ## NICE Json output
