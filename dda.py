# dda.py - DDA Line Drawing Algorithm

import pygame

def draw_line_dda(screen, x1, y1, x2, y2, color):
    """
    DDA Line Drawing Algorithm
    
    Steps:
    1. Calculate dx and dy
    2. Find number of steps = max(|dx|, |dy|)
    3. Calculate x and y increment
    4. Plot each point by incrementing x and y
    """
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    if steps == 0:
        return

    x_increment = dx / steps
    y_increment = dy / steps

    x = float(x1)
    y = float(y1)

    for i in range(steps + 1):
        # Plot the point on screen
        pygame.draw.rect(screen, color, (round(x), round(y), 2, 2))
        x += x_increment
        y += y_increment
