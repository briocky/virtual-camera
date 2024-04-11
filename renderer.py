from constants import *
from projector import project_3d_to_2d
import pygame


def draw_scene(camera, screen, vertices, edges):
    projected_points = []
    for point in vertices:
        projected_point = project_3d_to_2d(point, camera, SCREEN_WIDTH, SCREEN_HEIGHT, FOV)
        projected_points.append(projected_point)
        if projected_point:
            pygame.draw.circle(screen, WHITE, projected_point, 5)
    for edge in edges:
        start = projected_points[edge[0] - 1]
        end = projected_points[edge[1] - 1]
        if start and end:
        # print(start, end)
            pygame.draw.line(screen, WHITE, start[0:2], end[0:2], 2)