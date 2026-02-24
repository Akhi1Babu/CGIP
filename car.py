# car.py - Draw Car and Animate it

import pygame
import math
from dda import draw_line_dda

# Car colors
RED   = (220,  50,  50)
BLACK = ( 30,  30,  30)
WHITE = (220, 220, 220)
BLUE  = (173, 216, 230)

def draw_car(screen, x, y):
    """
    Draw a simple car at position (x, y).
    x, y = bottom-left corner of the car body
    
    Car parts:
    - Rectangle  → car body
    - Rectangle  → car roof
    - Two circles → wheels
    """
    # Car body
    pygame.draw.rect(screen, RED,   (x, y - 30, 80, 30))   # body
    pygame.draw.rect(screen, RED,   (x + 15, y - 50, 50, 22))  # roof
    pygame.draw.rect(screen, BLACK, (x, y - 30, 80, 30), 2)    # outline

    # Windows
    pygame.draw.rect(screen, BLUE, (x + 18, y - 48, 20, 18))   # rear window
    pygame.draw.rect(screen, BLUE, (x + 42, y - 48, 18, 18))   # front window

    # Wheels (two circles)
    wheel_radius = 12
    wheel_centers = [(x + 15, y + 2), (x + 63, y + 2)]
    
    # Calculate rotation angle based on x position
    # angle = distance / radius
    angle = (x % (2 * math.pi * wheel_radius)) / wheel_radius

    for cx, cy in wheel_centers:
        pygame.draw.circle(screen, BLACK, (cx, cy), wheel_radius)  # tire
        
        # Draw rotating spokes (white spikes) using DDA
        num_spikes = 6
        for i in range(num_spikes):
            spike_angle = angle + (2 * math.pi * i / num_spikes)
            # End point on the tire edge
            ex = int(cx + wheel_radius * math.cos(spike_angle))
            ey = int(cy + wheel_radius * math.sin(spike_angle))
            # Draw from center to edge
            draw_line_dda(screen, cx, cy, ex, ey, WHITE)

        pygame.draw.circle(screen, WHITE, (cx, cy), 4)  # hub


def animate_car(car_x, speed=2):
    """
    Move car to the right. Reset when it goes off screen.
    """
    car_x += speed
    if car_x > 800:
        car_x = -90   # reset to left side
    return car_x
