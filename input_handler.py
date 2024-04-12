import pygame
from pygame.locals import *
import sys


def handle_input(camera):

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:  # Move camera forward
                camera.move_forward()
            elif event.key == K_s:  # Move camera backward
                camera.move_backward()
            elif event.key == K_a:  # Move camera left
                camera.move_left()
            elif event.key == K_d:  # Move camera right
                camera.move_right()
            elif event.key == K_q:  # Move camera up
                camera.move_up()
            elif event.key == K_e:  # Move camera down
                camera.move_down()
            elif event.key == K_RIGHT:  # Rotate camera right
                camera.rotate_right()
            elif event.key == K_LEFT:  # Rotate camera left
                camera.rotate_left()
            elif event.key == K_UP:  # Pitch camera up
                camera.rotate_up()
            elif event.key == K_DOWN:  # Pitch camera down
                camera.rotate_down()
            elif event.key == K_o:  # roll camera
                camera.roll_left()
            elif event.key == K_p:  # roll camera
                camera.roll_right()
            elif event.key == K_f:
                camera.increase_fov()
            elif event.key == K_g:
                camera.decrease_fov()
