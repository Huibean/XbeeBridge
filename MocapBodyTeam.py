import struct
import numpy as np
from MocapBody import MocapBody

class MocapBodyTeam():
    blank_msg = struct.pack('B7f', 0, *np.zeros(7))

    def __init__(self):
        self.team = {}

    def is_exist(self, id):
        return id in self.team

    def create_new_body(self, id):
        self.team[id] = MocapBody(id)
        print("init new mocap body {0}".format(id))

    def body(self, id):
        return self.team[id]

    @property
    def size(self):
        return len(self.team)
    
    @property
    def output_list(self):
        msg_buffer = b''
        msg_group = []
        mocap_body_group = list(self.team.values())[:12]

        for index, mocap_body in enumerate(mocap_body_group + (12 - len(mocap_body_group)) * ['']):
            if mocap_body:
                msg_buffer += mocap_body.output
            else:
                msg_buffer += MocapBodyTeam.blank_msg

            if (index+1) % 4 == 0:
                msg_group.append(msg_buffer)
                msg_buffer = b''

        return msg_group
