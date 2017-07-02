import sys
import getopt
sys.path.append('../')
from cream import ERS
ise = ERS(ise_node='10.10.10.10', ers_user='xxxxxxxx', ers_pass='xxxxxxxx', verify=False, disable_warnings=True)

if len(sys.argv) == 2:
	if sys.argv[1] == "-g":
		print()
		resp_idgrp = ise.get_identity_groups()['response']
		idgrp_len = len(resp_idgrp)

		for num in range(0, idgrp_len):
			print(resp_idgrp[num])
elif len(sys.argv) == 3:
	mac_address = sys.argv[1]
	group_id = sys.argv[2]
	resp_add_endpoint = ise.add_endpoint(mac_address, group_id, profile_id = 'None')
	print(resp_add_endpoint)
else:
	input_file = open("add_endpoint.csv", "r") 
	list_of_lines = input_file.readlines()
	for line in list_of_lines:
		mac_address = line.split(",")[0]
		group_id = line.split(",")[1]
		print(mac_address, group_id)
		resp_add_endpoint = ise.add_endpoint(mac_address, group_id, profile_id = 'None')
		print(resp_add_endpoint)
