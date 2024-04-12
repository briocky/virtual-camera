import pygame

from camera import Camera
from constants import *
from input_handler import handle_input
from obj_loader import load_obj
from renderer import draw_scene


def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Define camera parameters
    camera_pos = [250, 150, -200]  # Initial camera position
    yaw = 0  # Yaw angle (rotation around y-axis)
    pitch = 0  # Pitch angle (rotation around x-axis)
    roll = 0  # roll angle

    camera = Camera(camera_pos, yaw, pitch, roll, FOV)

    vertices, edges = load_obj('c1.obj')  # scene

    while True:
        screen.fill(BLACK)

        handle_input(camera)
        draw_scene(camera, screen, vertices, edges)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
