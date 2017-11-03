import time, datetime
from Estimate import PositionEstimate, AttitudeEstimate

from pymavlink.dialects.v20.ardupilotmega import MAVLink_att_pos_mocap_message, MAVLink, MAVLink_message

from system_args import mav

class MocapBody(object):

    def __init__(self, body_id, xbee_address):
        self.position_estimate = PositionEstimate()
        self.attitude_estimate = AttitudeEstimate()
        self.body_id = body_id
        self.xbee_address = xbee_address
        self.last_update = datetime.datetime.now()

    def update(self, position, rotation):
        if not self.position_estimate.init:
            self.position_estimate.first_position = [position[0], position[2], position[1]]
            self.position_estimate.init = True
            print("mocap body {0} init".format(self.body_id))

        self.position_estimate.receive_new_position(position[0], position[2], position[1])
        self.attitude_estimate.receive_new_rotation(rotation[3] * -1, rotation[0], rotation[2], rotation[1])
        self.last_update = datetime.datetime.now()

    def is_timeout(self):
        datetime.datetime.now() - self.last_update

    @property
    def is_ready(self):
        return self.position_estimate.is_ready() and self.attitude_estimate.is_ready()

    @property
    def att_pos_msg(self):
        return MAVLink_att_pos_mocap_message(int(time.mktime(datetime.datetime.now().timetuple())), self.attitude_estimate.quaternion_data, self.position_estimate.ned_position[0], self.position_estimate.ned_position[1], self.position_estimate.ned_position[2]).pack(mav.mav)
