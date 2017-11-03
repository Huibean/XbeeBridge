class PositionEstimate(object):

    def __init__(self):
        self.positions_buffer = []
        self.delay = 0.05
        self.init = False
        self.first_position = []
        self.estimated_position = []

    def is_ready(self):
        return len(self.estimated_position) > 0

    def receive_new_position(self, x, y, z):
        new_position = [x, y, z]
        if not self.init:
            self.first_position = new_position[:]
            self.init = True

        self.positions_buffer.append(new_position)

        if len(self.positions_buffer) > 1:
            self.positions_buffer = self.positions_buffer[-2:]
            position = []
            for i in range(3):
                position.append((self.positions_buffer[-1][i] - self.positions_buffer[-2][i])*self.delay + self.positions_buffer[-1][i])
            self.estimated_position = position

    @property
    def ned_position(self):
        x, y, z = self.estimated_position
        x0, y0, z0 = self.first_position
        return x - x0, y - y0, z0 - z
