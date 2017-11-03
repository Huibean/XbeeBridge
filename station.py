from system_args import *

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

from WatchMan import WatchMan
watch_man = WatchMan()

while True:
    try:
        for id in mocap_bodies:
            mocap_body = mocap_bodies[id]
            if mocap_body.is_ready:
                xbee_device.send('tx_explicit',
                        frame_id=stringToBytes('1'),
                        dest_addr_long=bytearray.fromhex(mocap_body.xbee_address),
                        src_endpoint=bytearray.fromhex('E8'),
                        dest_endpoint=bytearray.fromhex('E8'),
                        cluster=bytearray.fromhex('0011'),
                        profile=bytearray.fromhex('C105'),
                        data=mocap_body.att_pos_msg)


        single_interval = (datetime.datetime.now() - sys_counter).total_seconds()
        base_interval = 0.03 - single_interval
        print(len(mocap_bodies), base_interval, single_interval)

        if base_interval > 0:
            time.sleep(base_interval)

        #  serial_port.flushInput()
        sys_counter = datetime.datetime.now()
    except Exception as e:
        print(e)
