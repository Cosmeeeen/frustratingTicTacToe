import pygame

# Culori
midnight_blue = (44, 62, 80)
carrot = (230, 126, 34)
cloud = (236, 240, 241)

# Initializare + setari ecran
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("X si 0 doar ca nu ai cum sa castigi")

clock = pygame.time.Clock()

board = [
    0, 2, 0,
    0, 1, 0,
    0, 0, 0
]


def new_game():
    global board
    board = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]


def grid_converter(grid_number):
    grid_x = grid_number % 3
    grid_y = grid_number // 3

    if grid_x == 0:
        grid_x = 80
    elif grid_x == 1:
        grid_x = 250
    else:
        grid_x = 420

    if grid_y == 0:
        grid_y = 80
    elif grid_y == 1:
        grid_y = 250
    else:
        grid_y = 420

    return (grid_x, grid_y)


def draw_x(grid_number):
    global board
    board[grid_number] = 1
    size = 50
    position = grid_converter(grid_number)
    pos_x = position[0]
    pos_y = position[1]
    pygame.draw.line(screen, carrot, (pos_x - size, pos_y - size), (pos_x + size, pos_y + size), 20)
    pygame.draw.line(screen, carrot, (pos_x - size, pos_y + size), (pos_x + size, pos_y - size), 20)


def draw_0(grid_number):
    size = 60
    position = grid_converter(grid_number)
    pygame.draw.circle(screen, carrot, position, size, 15)


def draw_board():
    # Linii
    pygame.draw.line(screen, cloud, (160, 0), (160, 500), 5)
    pygame.draw.line(screen, cloud, (340, 0), (340, 500), 5)

    pygame.draw.line(screen, cloud, (0, 160), (500, 160), 5)
    pygame.draw.line(screen, cloud, (0, 340), (500, 340), 5)

    # X si 0 in functie de variabila board
    global board
    for i in range(len(board)):
        if board[i] == 1:
            draw_x(i)
        elif board[i] == 2:
            draw_0(i)


# Main game loop
running = True

while running:
    # Iesire din aplicatie cand se apasa X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(midnight_blue)

    draw_board()

    pygame.display.flip()

    # Setare fps la maxim 20
    clock.tick(20)
