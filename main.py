# main.py - Main Program
# Bridge Visualization using DDA Algorithm with Car Animation

import pygame
import sys
from dda    import draw_line_dda
from bridge import draw_bridge
from car    import draw_car, animate_car

# --- Window Settings ---
WIDTH  = 800
HEIGHT = 600
FPS    = 60

# --- Colors ---
SKY_BLUE = (135, 206, 235)
GREEN    = ( 34, 139,  34)
WHITE    = (255, 255, 255)
YELLOW   = (255, 220,   0)
BLACK    = (  0,   0,   0)

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bridge - DDA Algorithm")
clock  = pygame.font.SysFont("Arial", 18)
font   = pygame.font.SysFont("Arial", 18)
clock_ = pygame.time.Clock()

# --- Car starting position ---
car_x = -90   # start off screen (left side)
car_y = 316   # road surface y

# --- Draw Sun ---
def draw_sun(surface):
    pygame.draw.circle(surface, YELLOW, (700, 80), 40)
    # Sun rays using DDA
    import math
    for i in range(8):
        angle = math.radians(i * 45)
        x1 = int(700 + 45 * math.cos(angle))
        y1 = int( 80 + 45 * math.sin(angle))
        x2 = int(700 + 65 * math.cos(angle))
        y2 = int( 80 + 65 * math.sin(angle))
        draw_line_dda(surface, x1, y1, x2, y2, YELLOW)

# --- Draw Clouds ---
def draw_clouds(surface):
    for cx, cy in [(150, 80), (380, 55), (580, 90)]:
        pygame.draw.circle(surface, WHITE, (cx,      cy),     25)
        pygame.draw.circle(surface, WHITE, (cx + 25, cy - 8), 30)
        pygame.draw.circle(surface, WHITE, (cx + 50, cy),     22)

# --- Main Game Loop ---
running = True
while running:

    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 2. Update car position
    car_x = animate_car(car_x, speed=2)

    # 3. Draw everything
    screen.fill(SKY_BLUE)             # sky background
    draw_sun(screen)                  # sun
    draw_clouds(screen)               # clouds

    # Ground
    pygame.draw.rect(screen, GREEN, (0, 440, WIDTH, HEIGHT - 440))

    # Bridge (uses DDA algorithm)
    draw_bridge(screen)

    # Car (moves across bridge)
    draw_car(screen, car_x, car_y)

    # Label
    label = font.render("DDA Algorithm Used", True, BLACK)
    pygame.draw.rect(screen, WHITE, (8, 8, label.get_width() + 14, 34))
    screen.blit(label, (15, 13))

    # 4. Update display
    pygame.display.flip()
    clock_.tick(FPS)

pygame.quit()
sys.exit()
