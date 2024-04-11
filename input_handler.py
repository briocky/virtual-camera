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
                camera.pos[2] += 10
            elif event.key == K_s:  # Move camera backward
                camera.pos[2] -= 10
            elif event.key == K_a:  # Move camera left
                camera.pos[0] -= 10
            elif event.key == K_d:  # Move camera right
                camera.pos[0] += 10
            elif event.key == K_q:  # Move camera left
                camera.pos[1] -= 10
            elif event.key == K_e:  # Move camera right
                camera.pos[1] += 10
            elif event.key == K_RIGHT:  # Rotate camera left
                camera.yaw += 0.1
            elif event.key == K_LEFT:  # Rotate camera right
                camera.yaw -= 0.1
            elif event.key == K_UP:  # Pitch camera up
                camera.pitch += 0.1
            elif event.key == K_DOWN:  # Pitch camera down
                camera.pitch -= 0.1
            elif event.key == K_o:  # Pitch camera down
                camera.roll -= 0.1
            elif event.key == K_p:  # Pitch camera down
                camera.roll += 0.1
