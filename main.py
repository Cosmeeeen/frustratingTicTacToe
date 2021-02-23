import pygame

import ai

# Culori
midnight_blue = (44, 62, 80)
carrot = (230, 126, 34)
cloud = (236, 240, 241)

# Initializare + setari ecran
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("X si 0 doar ca nu ai cum sa castigi")
pygame.font.init()
big_font = pygame.font.SysFont("Lucida Sans Unicode", 82)
small_font = pygame.font.SysFont("Lucida Sans Unicode", 32)

clock = pygame.time.Clock()

board = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]


def new_game():
    global board
    global players_turn
    players_turn = False
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

    return grid_x, grid_y


def position_to_grid(position):
    pos_x = position[0]
    pos_y = position[1]

    if 0 <= pos_x <= 160:
        pos_x = 0
    elif 160 < pos_x <= 340:
        pos_x = 1
    else:
        pos_x = 2

    if 0 <= pos_y <= 160:
        pos_y = 0
    elif 160 < pos_y <= 340:
        pos_y = 1
    else:
        pos_y = 2

    return pos_x + pos_y * 3


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


# Actionam dupa inputul jucatorului, care jocaca intotdeuna cu 0 (2)
def player_turn(square):
    if board[square] == 0:
        board[square] = 2


def ai_turn():
    global board
    best = ai.best_move(board, get_board_state)
    board[best] = 1
    global players_turn
    players_turn = True


# Arata pe ecran ecranul cand jocul s-a terminat
def draw_game_over(winner):
    if winner == 'X' or winner == '0':
        winner = winner + ' won'
    else:
        winner = 'Draw'
    game_over_text = big_font.render(winner, True, carrot)
    text_width = game_over_text.get_rect().width
    text_height = game_over_text.get_rect().height
    screen.blit(
        game_over_text,
        (
            SCREEN_WIDTH // 2 - text_width // 2,
            SCREEN_HEIGHT // 2 - text_height // 2 - 50
        )
    )

    try_again_text = small_font.render('Click anywhere to try again', True, cloud)
    text_width = try_again_text.get_rect().width
    text_height = try_again_text.get_rect().height
    screen.blit(
        try_again_text,
        (
            SCREEN_WIDTH // 2 - text_width // 2,
            SCREEN_HEIGHT // 2 - text_height // 2 + 50
        )
    )


def get_board_state(board):
    # verificam liniile
    p1 = 1
    p2 = 1
    p3 = 1
    for i in range(3):
        p1 *= board[i]
        p2 *= board[i+3]
        p3 *= board[i+6]

    if p1 == 1 or p2 == 1 or p3 == 1:
        return 'X'
    if p1 == 8 or p2 == 8 or p3 == 8:
        return '0'

    # verificam coloanele
    p1 = 1
    p2 = 1
    p3 = 1
    for i in range(3):
        p1 *= board[3*i]
        p2 *= board[1 + 3*i]
        p3 *= board[2 + 3*i]

    if p1 == 1 or p2 == 1 or p3 == 1:
        return 'X'
    if p1 == 8 or p2 == 8 or p3 == 8:
        return '0'

    p1 = 1
    p2 = 1
    for i in range(3):
        p1 *= board[4*i]
        p2 *= board[i*2+2]

    if p1 == 1 or p2 == 1:
        return 'X'
    if p1 == 8 or p2 == 8:
        return '0'

    if p1 and p2 and p3:
        return 'draw'  # egalitate


# Main game loop
running = True
playing = True
players_turn = False


while running:
    for event in pygame.event.get():
        # Iesire din aplicatie cand se apasa X
        if event.type == pygame.QUIT:
            running = False

        # Verificare click pe ecran
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playing and players_turn:
                position = pygame.mouse.get_pos()
                clicked_square = position_to_grid(position)
                player_turn(clicked_square)
                winner_check = get_board_state(board)
                players_turn = False
                if winner_check:
                    playing = False
            elif not playing:
                playing = True
                new_game()

    screen.fill(midnight_blue)

    if playing:
        if players_turn is False:
            ai_turn()
            winner_check = get_board_state(board)
            if winner_check:
                playing = False
        draw_board()
    else:
        draw_game_over(winner_check)

    pygame.display.flip()

    # Setare fps la maxim 20
    clock.tick(20)
