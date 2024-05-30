import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load queen image
QUEEN_IMAGE = pygame.transform.scale(pygame.image.load('queen.png'), (SQUARE_SIZE, SQUARE_SIZE))

# Fonts
FONT = pygame.font.SysFont('Arial', 24)
GAME_OVER_FONT = pygame.font.SysFont('Arial', 48)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Queens Chess")

# Board setup
board = [[None for _ in range(COLS)] for _ in range(ROWS)]
attacked_squares = set()

# Draw grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[row][col] == 'Q':
                screen.blit(QUEEN_IMAGE, (col * SQUARE_SIZE, row * SQUARE_SIZE))


# Highlight squares and mark them as attacked
def highlight_squares(row, col):
    for i in range(ROWS):
        # Vertical and horizontal
        attacked_squares.add((col, i))
        attacked_squares.add((i, row))
        pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, i * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
        pygame.draw.circle(screen, RED, (i * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
        # Diagonals
        if 0 <= row + i < ROWS and 0 <= col + i < COLS:
            attacked_squares.add((col + i, row + i))
            pygame.draw.circle(screen, RED, ((col + i) * SQUARE_SIZE + SQUARE_SIZE // 2, (row + i) * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
        if 0 <= row - i < ROWS and 0 <= col + i < COLS:
            attacked_squares.add((col + i, row - i))
            pygame.draw.circle(screen, RED, ((col + i) * SQUARE_SIZE + SQUARE_SIZE // 2, (row - i) * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
        if 0 <= row + i < ROWS and 0 <= col - i < COLS:
            attacked_squares.add((col - i, row + i))
            pygame.draw.circle(screen, RED, ((col - i) * SQUARE_SIZE + SQUARE_SIZE // 2, (row + i) * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
        if 0 <= row - i < ROWS and 0 <= col - i < COLS:
            attacked_squares.add((col - i, row - i))
            pygame.draw.circle(screen, RED, ((col - i) * SQUARE_SIZE + SQUARE_SIZE // 2, (row - i) * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

# Display current player
def display_current_player(player):
    text = FONT.render(f"Player {player + 1}'s turn", True, GREEN)
    screen.blit(text, (10, 10))

# Display game over
def display_game_over():
    text = GAME_OVER_FONT.render("Game Over", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    subtext = FONT.render("Press R to Restart", True, GREEN)
    screen.blit(subtext, (WIDTH // 2 - subtext.get_width() // 2, HEIGHT // 2 + text.get_height()))

# Check if the board is full
def is_board_full():
    for row in board:
        if None in row:
            return False
    return True

# Reset the board
def reset_board():
    global board, player, attacked_squares
    board = [[None for _ in range(COLS)] for _ in range(ROWS)]
    attacked_squares = set()
    player = 0

# Main loop
running = True
player = 0  # Player 0 or 1
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                col = mouse_pos[0] // SQUARE_SIZE
                row = mouse_pos[1] // SQUARE_SIZE
                if board[row][col] is None and (col, row) not in attacked_squares:
                    board[row][col] = 'Q'
                    highlight_squares(row, col)
                    player = (player + 1) % 2  # Switch player
                    if is_board_full():
                        game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_board()
                game_over = False

    # Draw everything
    screen.fill(BLACK)
    draw_grid()
    if not game_over:
        display_current_player(player)
    else:
        display_game_over()

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 'Q':
                highlight_squares(row, col)

    pygame.display.flip()
