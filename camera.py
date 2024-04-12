import numpy as np


class Camera:
    # yaw, pitch, roll - in radians
    def __init__(self, pos, yaw, pitch, roll, move_delta=10, rot_delta=0.1):
        self.pos = pos
        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll
        self.move_delta = move_delta
        self.rot_delta = rot_delta

    def move_forward(self):
        self.pos += self.get_direction_vector() * self.move_delta

    def move_backward(self):
        self.pos -= self.get_direction_vector() * self.move_delta

    def move_left(self):
        self.pos[0] -= self.move_delta

    def move_right(self):
        self.pos[0] += self.move_delta

    def move_up(self):
        self.pos[1] += self.move_delta

    def move_down(self):
        self.pos[1] -= self.move_delta

    def rotate_up(self):
        self.pitch += self.rot_delta

    def rotate_down(self):
        self.pitch -= self.rot_delta

    def rotate_left(self):
        self.yaw += self.rot_delta

    def rotate_right(self):
        self.yaw -= self.rot_delta

    def roll_right(self):
        self.roll -= self.rot_delta

    def roll_left(self):
        self.roll += self.rot_delta

    def get_direction_vector(self):
        direction = np.array([
            np.cos(self.pitch) * np.sin(-self.yaw),  # Inverting yaw angle
            np.sin(self.pitch),
            np.cos(self.pitch) * np.cos(-self.yaw)  # Inverting yaw angle
        ])
        return direction
