import pygame
import random

# Start the game
pygame.init()

# Screen dimensions
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Enhanced Brick Breaker Game")

# Game variables
floor = pygame.Rect(100, 550, 200, 10)
ball = pygame.Rect(50, 250, 10, 10)
score = 0
move = [3, 3]  # Ball speed
continueGame = True

# Colors
DARK_BLUE = (10, 10, 50)
WHITE = (255, 255, 255)
PINK = (252, 3, 152)
YELLOW = (252, 252, 3)
RED = (255, 0, 0)
CYAN = (3, 252, 252)
GREEN = (28, 252, 106)

# Bricks
b1 = [pygame.Rect(1 + i * 100, 60, 98, 38) for i in range(6)]
b2 = [pygame.Rect(1 + i * 100, 100, 98, 38) for i in range(6)]
b3 = [pygame.Rect(1 + i * 100, 140, 98, 38) for i in range(6)]
bricks = [b1, b2, b3]

# Draw bricks on screen
# Draw bricks on screen
def draw_brick(bricks):
    colors = [RED, CYAN, GREEN, YELLOW]  # List of brick colors
    for i, brick_row in enumerate(bricks):
        for j, brick in enumerate(brick_row):
            color = colors[(i + j) % len(colors)]  # Cycle through colors
            pygame.draw.rect(screen, color, brick)
            pygame.draw.rect(screen, DARK_BLUE, brick, 2)  # Brick border


while continueGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueGame = False

    # Detect key press for paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and floor.x < 600 - floor.width:
        floor.x += 5
    if keys[pygame.K_LEFT] and floor.x > 0:
        floor.x -= 5

    # Background
    screen.fill(DARK_BLUE)

    # Paddle
    pygame.draw.rect(screen, PINK, floor)

    # Score display
    font = pygame.font.Font(None, 34)
    text = font.render("CURRENT SCORE: " + str(score), 1, WHITE)
    screen.blit(text, (180, 10))

    # Ball Movement
    ball.x += move[0]
    ball.y += move[1]

    if ball.x <= 0 or ball.x >= 590:
        move[0] = -move[0]
    if ball.y <= 0:
        move[1] = -move[1]

    # Paddle Collision
    if floor.colliderect(ball):
        move[1] = -move[1]

    # Game Over
    if ball.y >= 600:
        # Display Game Over
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over!", 1, RED)
        screen.blit(text, (150, 250))
        font = pygame.font.Font(None, 50)
        text = font.render("YOUR FINAL SCORE: " + str(score), 1, WHITE)
        screen.blit(text, (100, 320))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

    # Brick Collision
    for brick_row in bricks:
        for brick in brick_row[:]:
            if brick.colliderect(ball):
                brick_row.remove(brick)
                move[1] = -move[1]
                score += 1

                # Increase ball speed as score increases
                if score % 5 == 0:
                    move[0] += 1 if move[0] > 0 else -1
                    move[1] += 1 if move[1] > 0 else -1

    # Check Win Condition
    if score == len(b1) + len(b2) + len(b3):
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON THE GAME!", 1, GREEN)
        screen.blit(text, (50, 300))
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    # Draw bricks and ball
    draw_brick(bricks)
    pygame.draw.rect(screen, WHITE, ball)
    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
