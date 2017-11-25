import pygame

pygame.init()

display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PeruBros')
clock = pygame.time.Clock()

palomaImg = pygame.image.load('resources/sprites/enemy/paloma8/paloma1.png')
logoImg = pygame.image.load('resources/logos/perubrologo.png')

def mover_paloma(x, y):
    gameDisplay.blit(palomaImg, (x, y))

def cambiar_paloma(state):
    state += 1
    global palomaImg
    palomaImg = pygame.image.load('./resources/sprites/enemy/paloma8/paloma%s.png' % state)
    if state == 6 : state = 0
    return state, 1

##############################


def game_loop():
    x = (0)
    y = (display_height - palomaImg.get_rect().size[1])
    x_change, y_change = 0, 0
    gameExit = False
    paloma_state = 1
    sec = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

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

        if sec == 0: paloma_state, sec = cambiar_paloma(paloma_state)
        else: sec = 0

        gameDisplay.fill(white)
        mover_paloma(x, y)

        if x > display_width-palomaImg.get_rect().size[0] or x < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)

def test():
    game_loop()
    pygame.quit()
    quit()

def gen_text(text, width, height):
    font = pygame.font.Font('./resources/squarefont/Square.ttf', 35)
    text_surf = font.render(text, True, white)
    text_rect = text_surf.get_rect()
    text_rect.center = (width / 2, height/2)
    return text_surf, text_rect

class Main:
    def __init__(self, width=display_width, height=display_height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        #Lógica
        pygame.display.set_caption('PeruBros')
        self.display.fill(white)

    def menu_login(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.draw.rect(self.display, black, (20, 20, self.width-40, self.height-40))

            logo_rect = logoImg.get_rect()
            logo_rect.center = (self.width/2, self.height*0.2)
            print(logo_rect.center)
            self.display.blit(logoImg, logo_rect)

            text, text_rec = gen_text('Hola',self.width, self.height)

            self.display.blit(text, text_rec)

            pygame.display.update()
            self.clock.tick(20)

def main():
    MainLogin = Main()
    MainLogin.menu_login()


