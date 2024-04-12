import numpy as np
from rotator import rotation_matrix_x, rotation_matrix_y, rotation_matrix_z
from constants import *


def project_3d_to_2d(point, camera):
    x, y, z = point
    x -= camera.pos[0]
    y -= camera.pos[1]
    z -= camera.pos[2]

    # Apply camera rotations using rotation matrices
    rotated_point = np.dot(rotation_matrix_y(camera.yaw), [x, y, z])
    rotated_point = np.dot(rotation_matrix_x(camera.pitch), rotated_point)
    rotated_point = np.dot(rotation_matrix_z(camera.roll), rotated_point)

    # Translate camera position
    #rotated_point = rotated_point - camera.pos

    # Perspective projection
    x_final, y_final, z_final = rotated_point
    if z_final > 0:  # Prevent division by zero
        scale = SCREEN_HEIGHT / (2 * np.tan(np.radians(FOV / 2)) * z_final)
        x_projected = int(SCREEN_WIDTH / 2 + x_final * scale)
        y_projected = int(SCREEN_HEIGHT / 2 - y_final * scale)
        return x_projected, y_projected
    else:
        # Return None if point is behind the camera
        return None