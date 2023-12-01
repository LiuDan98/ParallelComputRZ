import pygame
from pygame.locals import *
from OpenGL.GL import *
import math

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

orig_scale = 100
scale = orig_scale
polar = False
paused = False
update = None
window = [600, 600]

def zeta(s, n):
    total = [1]
    for i in range(2, n + 1):
        total.append(total[-1] + i ** -s)
    return total

def mouse_wheel(event):
    global scale
    scale += int(event.y)
    scale = abs(scale)

def mouse_dragged(event):
    if event.type == pygame.MOUSEMOTION and event.buttons[2]:  # Check if right mouse button is pressed
        glViewport(0, 0, event.x, event.y)
    elif event.type == pygame.MOUSEMOTION and not any(event.buttons):  # Check if no mouse button is pressed
        glViewport(0, 0, window[0], window[1])

def mouse_pressed(event):
    global paused
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
        paused = not paused

def key_pressed(event):
    global paused, update, scale, polar
    if event.key == K_SPACE:
        paused = True
        real_part = float(input("Real part: "))
        imag_part = float(input("Imaginary part: "))
        update = complex(real_part, imag_part)
    elif event.key == K_r:
        glViewport(0, 0, window[0], window[1])
        scale = orig_scale
    elif event.key == K_s:
        scale = orig_scale
    elif event.key == K_w:
        glViewport(0, 0, window[0], window[1])
    elif event.key == K_p:
        polar = not polar

def draw_circle(center, radius):
    num_segments = 100
    glBegin(GL_LINE_LOOP)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta) + center[0]
        y = radius * math.sin(theta) + center[1]
        glVertex2f(x, y)
    glEnd()

def draw():
    global comp, update
    trans = [window[0] / 2, window[1] / 2]
    glClearColor(*white, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, window[0], window[1], 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslated(trans[0], trans[1], 0)

    glColor3fv(black)  # Set color to black for the coordinate system

    # Draw two perpendicular lines for coordinate axes
    glBegin(GL_LINES)
    glVertex2f(-trans[0], 0)
    glVertex2f(trans[0], 0)
    glVertex2f(0, -trans[1])
    glVertex2f(0, trans[1])
    glEnd()

    if polar:
        rad = math.ceil((trans[0] + trans[1]) / 2) + scale
        for r in range(scale, rad * 2 + scale, scale):
            draw_circle([0, 0], r)
        rad *= 2
        for t in [math.pi / 4, math.pi / 3, math.pi / 6, 0]:
            glBegin(GL_LINES)
            glVertex2f(rad * math.cos(t), rad * math.sin(t))
            glVertex2f(rad * math.cos(t + math.pi), rad * math.sin(t + math.pi))
            glVertex2f(rad * math.cos(-t), rad * math.sin(-t))
            glVertex2f(rad * math.cos(-t + math.pi), rad * math.sin(-t + math.pi))
            glEnd()
    else:
        range_x = math.ceil(trans[0])
        range_y = math.ceil(trans[1])
        for x in range(-scale, -range_x, -scale):
            glBegin(GL_LINES)
            glVertex2f(x, 5)
            glVertex2f(x, -5)
            glEnd()
        for x in range(scale, range_x, scale):
            glBegin(GL_LINES)
            glVertex2f(x, 5)
            glVertex2f(x, -5)
            glEnd()
        for y in range(-scale, -range_y, -scale):
            glBegin(GL_LINES)
            glVertex2f(5, y)
            glVertex2f(-5, y)
            glEnd()
        for y in range(scale, range_y, scale):
            glBegin(GL_LINES)
            glVertex2f(5, y)
            glVertex2f(-5, y)
            glEnd()

    if not paused and update is None:
        comp = complex(pygame.mouse.get_pos()[0] - trans[0], -(pygame.mouse.get_pos()[1] - trans[1]))
        # comp = complex(pygame.mouse.get_pos()[0] - trans[0], pygame.mouse.get_pos()[1] - trans[1])
    if update is not None:
        comp = update * scale

    glColor3fv(yellow)
    glBegin(GL_POLYGON)
    for i in range(100):
        theta = 2.0 * math.pi * i / 100
        x = 5 * math.cos(theta) + comp.real
        y = -5 * math.sin(theta) + comp.imag
        glVertex2f(x, y)
    glEnd()

    comps = zeta(comp / scale, 201)
    for i in range(len(comps) - 1):
        glColor3fv(red)
        c = comps[i] * scale
        c2 = comps[i + 1] * scale
        glBegin(GL_LINES)
        glVertex2f(c.real, -c.imag)
        glVertex2f(c2.real, -c2.imag)
        glEnd()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.init()
window = (600, 600)
pygame.display.set_mode(window, DOUBLEBUF | OPENGL)
glViewport(0, 0, window[0], window[1])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed(event)
        elif event.type == pygame.MOUSEMOTION:
            mouse_dragged(event)
        elif event.type == pygame.KEYDOWN:
            key_pressed(event)
        elif event.type == pygame.MOUSEWHEEL:
            mouse_wheel(event)

    draw()
