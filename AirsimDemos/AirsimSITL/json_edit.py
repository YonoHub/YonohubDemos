# import json
# import os

# filename = '/MyDrive/YonohubDemos/AirsimDemos/AirsimSITL/settings_asap.json'
# with open(filename, 'r') as f:
#     data = json.load(f)
#     data['Vehicles']['drone_1']['UdpIp'] = "100.233.119.20" # <--- add `id` value.
#     print(data['Vehicles']['drone_1']['UdpIp'])
# os.remove(filename)
# with open(filename, 'w') as f:
#     json.dump(data, f, indent=4)

import socket
print()