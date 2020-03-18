import json
from napalm.base import get_network_driver
from getpass import getpass
import pdb
dest_node = input("target node ip: ")
node_driver = input("type the node driver type: ")
dest_ip = input("Type the IP you are trying to ping: ")
driver = get_network_driver(node_driver)
#dev = driver(hostname=dest_node, username='ansible', password='ansible123')
dev = driver(hostname=dest_node, username='ansible', password=getpass())
#pdb.set_trace()
dev.open()
ping_stats = dev.ping(dest_ip)
dev.close()
#print(json.dumps(ping_stats, sort_keys=True, indent=4))
#print(ping_stats['success'])
if ping_stats['success']['packet_loss'] == 5:
    print ('Host', dest_ip, 'is DOWN')
else:
    print ('Host', dest_ip, 'is ALIVE')
