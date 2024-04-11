class Camera:
    def __init__(self, pos, yaw, pitch, roll, move_delta=0.2, rot_delta=5):
        self.pos = pos
        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll
        self.move_delta = move_delta
        self.rot_delta = rot_delta

    def move_forward(self):
        self.position[2] += self.move_delta * 10

    def move_backward(self):
        self.position[2] -= self.move_delta * 10

    def move_left(self):
        self.position[0] -= self.move_delta

    def move_right(self):
        self.position[0] += self.move_delta

    def move_up(self):
        self.position[1] += self.move_delta

    def move_down(self):
        self.position[1] -= self.move_delta

    def rotate_up(self):
        self.rotation[0] -= self.rot_delta

    def rotate_down(self):
        self.rotation[0] += self.rot_delta

    def rotate_left(self):
        self.rotation[1] -= self.rot_delta

    def rotate_right(self):
        self.rotation[1] += self.rot_delta

    def rotate_y(self, ry):
        pass
