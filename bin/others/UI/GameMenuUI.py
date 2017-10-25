import pygame, requests, _json

class GameUIMenu:
    def __init__(self, idUser):
        pygame.init()

        self.display_width = 800
        self.display_height = 600
        self.animar = False
        self.last_update = 0
        self.current_frame = 0

        self.gameMenuDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("PERUBROS. -- PRE-ALPHA --")
        self.clock = pygame.time.Clock()
        self.user = self.obtener_info_usuario(idUser)

    def animate(self, action_type):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(action_type)
            self.image = action_type[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.topleft = ((300, 100))

    def obtener_info_usuario(self, id):
        url = "https://jsonplaceholder.typicode.com/users/" + str(id)
        return requests.get(url).json()

    def gen_bienvenida(self, text, width, height):
        font = pygame.font.Font('resources/squarefont/Square.ttf', 35)
        text_surf = font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect()
        #text_rect.center = (width / 2, height / 2)
        return text_surf, text_rect

    def gen_partida(self, text, width, height):
        font = pygame.font.Font('resources/squarefont/Square.ttf', 35)
        text_surf = font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect()
        #text_rect.center = (width / 2, height / 2)
        return text_surf, text_rect

    def obtener_img_personaje(self, personaje):
        self.imagenes = []
        self.imagenes.append(pygame.image.load('./resources/nino.png'))
        self.imagenes.append(pygame.image.load('./resources/nina.png'))
        personajeImg = None
        if personaje == 1 : personajeImg = pygame.image.load('./resources/nino.png')
        elif personaje == 2 : personajeImg = pygame.image.load('./resources/nina.png')
        return personajeImg


    def main_menu(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if pygame.mouse.get_pos()[1] >= partida1_rec and pygame.mouse.get_pos()[1] < partida2_rec:
                        print("HAS SELECCIONADO LA PARTIDA 1")
                    elif pygame.mouse.get_pos()[1] >= partida2_rec and pygame.mouse.get_pos()[1] < partida3_rec:
                        print("HAS SELECCIONADO LA PARTIDA 2")
                    elif pygame.mouse.get_pos()[1] >= partida3_rec:
                        print("HAS SELECCIONADO LA PARTIDA 3")

            self.gameMenuDisplay.fill((0, 0, 0))

            text, text_rec = self.gen_bienvenida("Bienvenido " + self.user["username"], self.display_width, self.display_height)
            partida1, partida1_rec = self.gen_partida("Partida 1: Alias", self.display_width, self.display_height)
            partida2, partida2_rec = self.gen_partida("Partida 2: Alias", self.display_width, self.display_height)
            partida3, partida3_rec = self.gen_partida("Partida 3: Alias", self.display_width, self.display_height)

            partida1_rec = 50 + text_rec.size[1] * 2
            partida2_rec = 50 + text_rec.size[1] * 4
            partida3_rec = 50 + text_rec.size[1] * 6

            self.gameMenuDisplay.blit(text, (0, 50))
            self.gameMenuDisplay.blit(partida1, (0, partida1_rec))
            self.gameMenuDisplay.blit(partida2, (0, partida2_rec))
            self.gameMenuDisplay.blit(partida3, (0, partida3_rec))

            if pygame.mouse.get_pos()[1] >= partida1_rec and pygame.mouse.get_pos()[1] < partida2_rec:
                self.animate(self.imagenes)
                self.gameMenuDisplay.blit(self.image, self.rect)
                self.animar = True
            elif pygame.mouse.get_pos()[1] >= partida2_rec and pygame.mouse.get_pos()[1] < partida3_rec:
                self.gameMenuDisplay.blit(self.obtener_img_personaje(2), (300, 100))
                self.animar = True
            elif pygame.mouse.get_pos()[1] >= partida3_rec:
                self.gameMenuDisplay.blit(self.obtener_img_personaje(1), (300, 100))

            pygame.display.update()
            self.clock.tick(60)
