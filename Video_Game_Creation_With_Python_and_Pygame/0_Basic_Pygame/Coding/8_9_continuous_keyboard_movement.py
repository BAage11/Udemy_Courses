import pygame

# Initialize pygame
pygame.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Continuous Movement!")

# Set FPS (frames per second) and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5

# Load images
dragon_image = pygame.image.load(
    "0_Basic_Pygame/Images/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()
    # print(keys)

    # Move the dragon continuously
    if keys[pygame.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP] and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY

    # Fill the display
    display_surface.fill((0, 0, 0))

    # Blit assets
    display_surface.blit(dragon_image, dragon_rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)


# End game
pygame.quit()