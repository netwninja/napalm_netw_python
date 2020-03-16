import json
from napalm.base import get_network_driver
from termcolor import colored
from getpass import getpass
#optional_args = {'transport': 'https'}
dest_prefix = input("destination network: ")
device_driver = input("type the device_driver type: ")
dest_node = input("Destination node: ")
#print('The network is', dest_prefix) ### This is just to test the user input gets assigned as a VARIABLE OR NOT
driver = get_network_driver(device_driver)
#dev = driver(hostname=dest_node, username='ansible', password='ansible123')
dev = driver(hostname=dest_node, username='ansible', password=getpass())
dev.open()
dev_info = dev.get_route_to(dest_prefix)
dev.close()
#print(dev_info)   ### It's going to print list '4.4.4.4/32'
#print(json.dumps(dev_info, sort_keys=True, indent=4))  #### This prints nice JSON output
#list1 = dev_info['4.4.4.4/32'] ### This prints the index 0 for list '4.4.4.4/32'
for dictionary in dev_info[dest_prefix]:
    try:
     print('The route', dest_prefix, 'is reachable via nexthop', dictionary['next_hop'], 'using protocol', dictionary['protocol'])
    except KeyError:
     pass
