# bridge.py - Draw Bridge using DDA Algorithm

from dda import draw_line_dda

# Colors
GRAY   = (100, 100, 100)
BROWN  = (101,  67,  33)
YELLOW = (255, 220,   0)

def draw_bridge(screen):
    """
    Draw a simple bridge using the DDA algorithm.
    
    Structure:
        /\    /\    /\
    ___/  \__/  \__/  \___    <-- road
       |    |    |    |        <-- pillars
    """

    # --- Projection (simple perspective) ---
    # We shift x slightly based on a z value to simulate depth
    def project(x, y, z=0):
        d = 500  # focal distance
        x_proj = int(400 + (x - 400) / (1 + z / d))
        y_proj = int(300 + (y - 300) / (1 + z / d))
        return x_proj, y_proj

    road_y = 320  # y position of the bridge road

    # --- 1. Bridge Road (horizontal line) ---
    ax, ay = project(-100, road_y)
    bx, by = project(900, road_y)
    draw_line_dda(screen, ax, ay, bx, by, GRAY)
    draw_line_dda(screen, ax, ay+3, bx, by+3, GRAY)
    draw_line_dda(screen, ax, ay+6, bx, by+6, GRAY)

    # --- 2. Vertical Pillars ---
    pillar_positions = [-50, 100, 250, 400, 550, 700, 850]
    for px in pillar_positions:
        top_x,    top_y    = project(px, road_y)
        bottom_x, bottom_y = project(px, road_y + 120)
        draw_line_dda(screen, top_x, top_y, bottom_x, bottom_y, GRAY)

    # --- 3. Triangle / Arch Supports above road ---
    spans = [
        (-50, 100),
        (100, 250),
        (250, 400),
        (400, 550),
        (550, 700),
        (700, 850),
    ]
    for (left, right) in spans:
        peak = (left + right) // 2
        peak_y = road_y - 70

        lx, ly  = project(left,  road_y)
        px, py  = project(peak,  peak_y)
        rx, ry  = project(right, road_y)

        # Left slope
        draw_line_dda(screen, lx, ly, px, py, BROWN)
        # Right slope
        draw_line_dda(screen, px, py, rx, ry, BROWN)

    # --- 4. Road center markings (dashes) ---
    dash_x = -80
    while dash_x < 880:
        ax, ay = project(dash_x,      road_y + 3)
        bx, by = project(dash_x + 25, road_y + 3)
        draw_line_dda(screen, ax, ay, bx, by, YELLOW)
        dash_x += 50
