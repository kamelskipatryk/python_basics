import pygame
import random

### Initialization
pygame.init() # Not necessary
font = pygame.font.SysFont('Arial', 30)

# Colours
blue = (0, 0, 255) # hex code for blue
black = (0, 0, 0) # hex code for black
red = (255, 0, 0) # hex code for red
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the snake in the middle of the screen
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_speed = 20
snake_size = 10
snake_length = 1
snake_blocks = []

fruit_x = 300
fruit_y = 400

speed_x = 0
speed_y = 10

game_over = False

running = True
clock = pygame.time.Clock()

# While "running" is true (always true unless user quits):
while running:
  # If the user hasn't lost the game:
  if not game_over:
    screen.fill((255,255,255)) # 255, 255, 255 is hexadecimal for the colour black

    # Set the snake head to the current position, append to snake blocks to
    # keep track
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_blocks.append(snake_head)

    # Ensure the snake is only as big as the length we've set
    if len(snake_blocks) > snake_length:
      del snake_blocks[0]

    # Not counting the last block, check if any other existing snake
    # blocks are crossing over the snake head (dead)
    for x in snake_blocks[:-1]:
      if x == snake_head:
        game_over = True

    # Draw a snake block for each point the user has
    for block in snake_blocks:
      pygame.draw.rect(screen, blue, [block[0], block[1], snake_size, snake_size])
    pygame.draw.rect(screen, red, [fruit_x, fruit_y, snake_size, snake_size])

    # Update the speed of the snake
    snake_x += speed_x
    snake_y += speed_y

    # If the snake is touching fruit (x and y position match for snake head and
    # fruit), set the fruit to a new, random position and update snake length
    if snake_x == fruit_x and snake_y == fruit_y:
      fruit_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
      fruit_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
      snake_length += 1

    # If the snake goes beyond the left or right side of the screen,
    if (snake_x >= screen_width or snake_x < 0 or
      # if the snake goes beyond the top of bottom of the screen,
      snake_y >= screen_height or snake_y < 0):
        # Set game over to true
        game_over = True

  # Game over logic (screen showing users score + how to continue)
  else:
    screen.fill(blue)
    score = font.render('You scored ' + str(snake_length), False, black)
    screen.blit(score, (10, screen_height / 2 - 100))
    text = font.render('You lost! Press \'Q\' to quit, or Spacebar to play again', False, black)
    screen.blit(text, (10, screen_height / 2))

  # Update the screen
  pygame.display.flip()
  clock.tick(snake_speed)

  ### Event Loop
  # Get the next events from the queue
  # For each event returned from get(),
  for event in pygame.event.get():
    # If the event is "KEYDOWN"
    if event.type == pygame.KEYDOWN:
        # If "Q" is pressed, stop game
        if event.key == pygame.K_q:
            running = False
        # If space is pressed, reset game
        if event.key == pygame.K_SPACE:
            game_over = False
            snake_x = screen_width / 2
            snake_y = screen_height / 2
            snake_blocks = []
            snake_length = 1
        # Movement (up, down, left, right arrow keys)
        if event.key == pygame.K_UP:
            speed_x = 0
            speed_y = -10
        if event.key == pygame.K_DOWN:
            speed_x = 0
            speed_y = 10
        if event.key == pygame.K_LEFT:
            speed_y = 0
            speed_x = -10
        if event.key == pygame.K_RIGHT:
            speed_y = 0
            speed_x = 10
    # If the event is "QUIT" (when user clicks X on window)
    if event.type == pygame.QUIT:
      # Set running to False, stop event loop
      running = False