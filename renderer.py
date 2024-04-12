import pygame

from constants import *
from projector import project_3d_to_2d


def draw_scene(camera, screen, vertices, edges):
    # project points to 2D
    projected_points = []
    for point in vertices:
        projected_point = project_3d_to_2d(point, camera)
        projected_points.append(projected_point)
        if projected_point:
            pygame.draw.circle(screen, WHITE, projected_point, 5)

    # draw connection lines
    for edge in edges:
        start = projected_points[edge[0] - 1]
        end = projected_points[edge[1] - 1]
        if start and end:
            pygame.draw.aaline(screen, WHITE, start[0:2], end[0:2], 2)