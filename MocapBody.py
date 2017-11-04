import time, datetime
import numpy as np
import struct

class MocapBody(object):

    def __init__(self, body_id):
        self.body_id = body_id
        self.last_update = datetime.datetime.now()
        self.raw_data = np.zeros(0)

    def update(self, position, rotation):
        self.raw_data = np.array(position + rotation, dtype=np.float64)
        self.last_update = datetime.datetime.now()

    def is_timeout(self):
        return (datetime.datetime.now() - self.last_update).total_seconds() > 2

    @property
    def is_ready(self):
        return self.raw_data.size > 0 

    @property
    def output(self):
        return struct.pack('B7f', self.body_id, *self.raw_data)
