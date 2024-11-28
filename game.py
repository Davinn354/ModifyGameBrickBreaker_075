import pygame

# Start the game
pygame.init()

# Screen settings
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Brick Breaker Game")

# Define colors
GREEN = (28, 252, 106)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (252, 3, 152)
ORANGE = (252, 170, 28)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (252, 252, 28)
PURPLE = (128, 0, 128)

# Initialize game objects
floor = pygame.Rect(100, 550, 200, 10)
ball = pygame.Rect(50, 250, 10, 10)
score = 0
move = [2, 2]  # Kecepatan bola
continueGame = True

# Bricks
b1 = [pygame.Rect(1 + i * 100, 60, 98, 38) for i in range(6)]
b2 = [pygame.Rect(1 + i * 100, 100, 98, 38) for i in range(6)]
b3 = [pygame.Rect(1 + i * 100, 140, 98, 38) for i in range(6)]


# Function to display menu
def show_menu():
    menu_running = True
    while menu_running:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        title = font.render("Brick Breaker", True, WHITE)
        screen.blit(title, (150, 100))

        font = pygame.font.Font(None, 50)
        start_text = font.render("1. Start Game", True, GREEN)
        exit_text = font.render("2. Exit", True, RED)
        screen.blit(start_text, (200, 250))
        screen.blit(exit_text, (200, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Start game
                    menu_running = False
                if event.key == pygame.K_2:  # Exit game
                    pygame.quit()
                    exit()


# Function to display game over menu
def game_over_menu():
    game_over_running = True
    while game_over_running:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        title = font.render("Game Over!", True, RED)
        screen.blit(title, (150, 100))

        font = pygame.font.Font(None, 50)
        restart_text = font.render("1. Restart Game", True, GREEN)
        exit_text = font.render("2. Exit", True, RED)
        screen.blit(restart_text, (200, 250))
        screen.blit(exit_text, (200, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Restart game
                    return True
                if event.key == pygame.K_2:  # Exit game
                    pygame.quit()
                    exit()


# Draw bricks on screen
def draw_brick(bricks, color):
    for i in bricks:
        pygame.draw.rect(screen, color, i)


# Show start menu
show_menu()

# Main game loop
while continueGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueGame = False

    # Move floor using key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and floor.x < 540:
        floor.x += 5  # Kecepatan floor (langkah)
    if keys[pygame.K_LEFT] and floor.x > 0:
        floor.x -= 5  # Kecepatan floor (langkah)

    # Clear screen
    screen.fill(BLACK)

    # Draw floor and ball
    pygame.draw.rect(screen, PINK, floor)
    pygame.draw.rect(screen, WHITE, ball)

    # Display score
    font = pygame.font.Font(None, 34)
    text = font.render("CURRENT SCORE: " + str(score), 1, WHITE)
    screen.blit(text, (180, 10))

    # Draw bricks
    draw_brick(b1, BLUE)
    draw_brick(b2, YELLOW)
    draw_brick(b3, PURPLE)

    # Ball movement
    ball.x += move[0]
    ball.y += move[1]

    # Ball collision with walls
    if ball.x > 590 or ball.x < 0:
        move[0] = -move[0]
    if ball.y <= 3:
        move[1] = -move[1]

    # Ball collision with floor
    if floor.collidepoint(ball.x, ball.y):
        move[1] = -move[1]

    # Ball collision with bricks
    for i in b1 + b2 + b3:
        if i.collidepoint(ball.x, ball.y):
            if i in b1:
                b1.remove(i)
            elif i in b2:
                b2.remove(i)
            elif i in b3:
                b3.remove(i)
            move[0] = -move[0]
            move[1] = -move[1]
            score += 1

    # Game over condition
    if ball.y >= 590:
        if not game_over_menu():
            break
        else:
            # Reset game variables
            ball = pygame.Rect(50, 250, 10, 10)
            score = 0
            b1 = [pygame.Rect(1 + i * 100, 60, 98, 38) for i in range(6)]
            b2 = [pygame.Rect(1 + i * 100, 100, 98, 38) for i in range(6)]
            b3 = [pygame.Rect(1 + i * 100, 140, 98, 38) for i in range(6)]

    # Win condition
    if score == 18:
        font = pygame.font.Font(None, 30)
        text = font.render("YOU WON THE GAME", 1, GREEN)
        screen.blit(text, (150, 350))
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    pygame.display.flip()
    pygame.time.delay(10)

# Quit the game
pygame.quit()
