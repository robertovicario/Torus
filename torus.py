"""
/**
 * @copyright Roberto Vicario (c) 2024
 */
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def torus(R, r, num_segments=25, num_sides=25):
    vertices = []
    edges = []

    for i in range(num_segments):
        for j in range(num_sides):
            u = i * 2 * math.pi / num_segments
            v = j * 2 * math.pi / num_sides
            x = (R + r * math.cos(v)) * math.cos(u)
            y = (R + r * math.cos(v)) * math.sin(u)
            z = r * math.sin(v)
            vertices.append((x, y, z))

    for i in range(num_segments):
        for j in range(num_sides):
            edges.append(((i * num_sides + j),
                          (i * num_sides + (j + 1) % num_sides)))
            edges.append(((i * num_sides + j),
                          (((i + 1) % num_segments) * num_sides + j)))

    return vertices, edges

def DrawTorus(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    R = 1.5
    r = 0.5
    vertices, edges = torus(R, r)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        DrawTorus(vertices, edges)
        pygame.display.flip()
        pygame.time.wait(10)

main()
