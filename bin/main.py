import pygame

# print("Probando 1.2.3.")
pygame.init()

display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PeruBros')
clock = pygame.time.Clock()

palomaImg = pygame.image.load('./resources/sprites/enemy/paloma8/paloma1.png')

def mover_paloma(x, y):
    gameDisplay.blit(palomaImg, (x, y))

def cambiar_paloma(state):
    state += 1
    global palomaImg
    palomaImg = pygame.image.load('./resources/sprites/enemy/paloma8/paloma%s.png' % state)
    if state == 6 : state = 0
    return state

def test():
    x = (0)
    y = (display_height-palomaImg.get_rect().size[1])
    x_change, y_change = 0, 0
    crashed = False
    paloma_state = 1
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_UP:
                    y_change = -10
                if event.key == pygame.K_DOWN:
                    y_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

        x += x_change
        y += y_change
        paloma_state = cambiar_paloma(paloma_state)
        gameDisplay.fill(white)
        mover_paloma(x, y)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()

def main():
    print('MAIN')
