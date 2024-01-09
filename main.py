import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße
screen_width = 800
screen_height = 600

# Farben
white = (255, 255, 255)
black = (0, 0, 0)

# Spielgeschwindigkeit
speed = 5

# Erstellung des Bildschirms
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bewegendes Quadrat')

# Quadrat-Eigenschaften
square_size = 50
x = (screen_width - square_size) // 2
y = (screen_height - square_size) // 2
direction = 1  # 1 für rechts, -1 für links

clock = pygame.time.Clock()

# Hauptspielschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bewegung des Quadrats
    x += direction * speed

    # Überprüfen, ob das Quadrat den Bildschirmrand erreicht hat
    if x < 0:
        x = 0
        direction = 1
    elif x > screen_width - square_size:
        x = screen_width - square_size
        direction = -1

    # Hintergrund zeichnen
    screen.fill(white)

    # Quadrat zeichnen
    pygame.draw.rect(screen, black, (x, y, square_size, square_size))

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Begrenzung der Bildrate
    clock.tick(30)

# Pygame beenden
pygame.quit()
sys.exit()
