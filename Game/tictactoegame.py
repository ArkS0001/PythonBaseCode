import pygame
import random
import sys 

pygame.init()
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
WHITE = (255,255,255)
LINE_COLOR = (23,145,135)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((WIDTH,HEIGHT))

board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_grid():
    for x in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (x * SQUARE_SIZE, 0), (x * SQUARE_SIZE, HEIGHT),LINE_WIDTH)
    for y in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, y * SQUARE_SIZE), (WIDTH, y * SQUARE_SIZE),LINE_WIDTH)

def draw_markers():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + 15, row * SQUARE_SIZE + 15), ((col + 1) * SQUARE_SIZE - 15, (row + 1) * SQUARE_SIZE - 15), 5)
                pygame.draw.line(screen, RED , ((col + 1) * SQUARE_SIZE - 15, row * SQUARE_SIZE + 15), (col * SQUARE_SIZE + 15, (row + 1) * SQUARE_SIZE - 15), 5)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, BLUE, (int(col * SQUARE_SIZE + SQUARE_SIZE/2),int(row * SQUARE_SIZE + SQUARE_SIZE/2)),50,5)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == ""

def check_win(player):
    for row in range(BOARD_ROWS):
        if all([board[row][col] == player for col in range(BOARD_COLS)]):
            return True
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            return True
    if all([board[i][i] == player for i in range(BOARD_ROWS)]) or \
       all([board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)]):
        return True
    return False

def check_draw():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '':
                return False
    return True

def draw_board():
    screen.fill(WHITE)
    draw_grid()
    draw_markers()
    pygame.display.update()

def main():
    player = 'X'
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        print("You win!")
                        game_over = True
                    elif check_draw():
                        print("It's a draw!")
                        game_over = True
                    else:
                        player = "O" if player == "X" else "X"
                    
                    draw_board()

        if player == "O" and not game_over:
            row, col = random.choice([(r,c) for r in range(BOARD_ROWS) for c in range(BOARD_COLS) if available_square(r,c)])
            mark_square(row, col, player)
            if check_win(player):
                print("You lose!")
                game_over = True
            elif check_draw():
                print("It's a draw!")
                game_over = True
            else:
                player = "O" if player == "X" else "X"
            draw_board()

draw_board()
main()


            


    







            








