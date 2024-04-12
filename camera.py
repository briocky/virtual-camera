class Camera:
    def __init__(self, pos, yaw, pitch, roll, move_delta=0.2, rot_delta=5):
        self.pos = pos
        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll
        self.move_delta = move_delta
        self.rot_delta = rot_delta

    def move_forward(self):
        self.pos[2] += 10

    def move_backward(self):
        self.pos[2] -= 10

    def move_left(self):
        self.pos[0] -= 10

    def move_right(self):
        self.pos[0] += 10

    def move_up(self):
        self.pos[1] += 10

    def move_down(self):
        self.pos[1] -= 10

    def rotate_up(self):
        self.pitch += 0.1

    def rotate_down(self):
        self.pitch -= 0.1

    def rotate_left(self):
        self.yaw += 0.1

    def rotate_right(self):
        self.yaw -= 0.1

    def roll_right(self):
        self.roll -= 0.1

    def roll_left(self):
        self.roll += 0.1
