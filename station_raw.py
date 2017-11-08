from system_args import mocap_body_team

from NatNetClient import NatNetClient
from Estimate import receiveNewFrame, receiveRigidBodyFrame

nat_net_streaming_client = NatNetClient(serverIPAddress=mocap_pc_ip)

nat_net_streaming_client.newFrameListener = receiveNewFrame
nat_net_streaming_client.rigidBodyListener = receiveRigidBodyFrame
nat_net_streaming_client.run()

import time, datetime
from xbee.python2to3 import intToByte, stringToBytes

base_interval = 0.02
single_interval = 0
sys_counter = datetime.datetime.now()

#  from WatchMan import WatchMan
#  watch_man = WatchMan()
#watch_man.start()

import socket
data_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 100)

time.sleep(4)
while True:
    try:
        if mocap_body_team.size > 0:
            for msg in mocap_body_team.output_list:
                #  xbee_device.send('tx_explicit',
                        #  frame_id=stringToBytes('1'),
                        #  dest_addr_long=bytearray.fromhex('000000000000FFFF'),
                        #  src_endpoint=bytearray.fromhex('E8'),
                        #  dest_endpoint=bytearray.fromhex('E8'),
                        #  cluster=bytearray.fromhex('0011'),
                        #  profile=bytearray.fromhex('C105'),
                        #  data=msg)

                #  xbee_device.send('tx',
                        #  frame_id=stringToBytes('1'),
                        #  dest_addr=bytearray.fromhex('000000000000FFFF'),
                        #  broadcast_radius = bytearray.fromhex('00'),
                        #  data=msg)

                data_socket.sendto(msg, ('255.255.255.255', 49600))

            time.sleep(0.005)
        else:
            time.sleep(1)

        print('beat')

        #  single_interval = (datetime.datetime.now() - sys_counter).total_seconds()
        #  base_interval = 0.001 - single_interval
        #  print(base_interval, single_interval)

        #  if base_interval > 0:
            #  time.sleep(base_interval)

        #  sys_counter = datetime.datetime.now()
    except Exception as e:
        #  serial_port.flushOutput()
        print(e)
