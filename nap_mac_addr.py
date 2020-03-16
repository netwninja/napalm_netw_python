import json
from napalm import get_network_driver
dest_node = input("target node ip: ")
node_driver = input("type target node driver type: ")
find_mac = input("Type the mac address in format xx.xx.xx.xx.xx.xx : ")
driver = get_network_driver(node_driver)
dev = driver(hostname=dest_node, username='ansible', password='ansible123')
dev.open()
dev_info = dev.get_mac_address_table()
dev.close()
try:
    for d in dev_info:
        #print(d['mac'])
        if d['mac'].lower() == find_mac.lower():
            print (d['mac'], 'connected to interface', d['interface'], 'of node', dest_node)
        else:
            print('')
except KeyError:
    pass
