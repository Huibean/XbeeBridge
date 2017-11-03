from Estimate.Quaternion import Quaternion

class AttitudeEstimate(object):

    def __init__(self):
        self.rotations_buffer = []

    def is_ready(self):
        return len(self.rotations_buffer) > 0

    def receive_new_rotation(self, w, x, y, z):
        self.rotations_buffer = [w, x, y, z]

    @property
    def quaternion(self):
        return Quaternion(self.rotations_buffer).processed_quat

    @property
    def quaternion_data(self):
        return self.quaternion.q.tolist()
