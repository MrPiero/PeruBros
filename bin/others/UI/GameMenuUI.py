import pygame, requests
import bin.constants as GC

class GameUIMenu:
    def __init__(self, idUser):
        pygame.init()

        self.display_width = 800
        self.display_height = 600

        self.gameMenuDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("PERUBROS. -- PRE-ALPHA GAME MENU --")
        self.clock = pygame.time.Clock()
        self.user = self.obtener_info_usuario(idUser)

    def obtener_info_usuario(self, id):
        return requests.get(GC.URL_USER + str(id)).json()

    def gen_bienvenida(self, text):
        font = pygame.font.Font(GC.FONT_PATH, 35)
        text_surf = font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect()
        #text_rect.center = (width / 2, height / 2)
        return text_surf, text_rect

    def gen_partida(self, text):
        font = pygame.font.Font(GC.FONT_PATH, 24)
        text_surf = font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect()
        return text_surf, text_rect

    def obtener_img_personaje(self, personaje):
        if personaje == 0:
            return pygame.image.load('./resources/nino.png')
        elif personaje == 1:
            return pygame.image.load('./resources/nina.png')


    def main_menu(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if partida1_rec <= pygame.mouse.get_pos()[1] <= partida1_rec + partida1.get_height():
                        print("ABRIENDO LA PARTIDA 1")
                        return 0
                    elif partida2_rec <= pygame.mouse.get_pos()[1] <= partida2_rec + partida2.get_height():
                        print("ABRIENDO LA PARTIDA 2")
                        return 0
                    elif partida3_rec <= pygame.mouse.get_pos()[1] <= partida3_rec + partida3.get_height():
                        print("ABRIENDO LA PARTIDA 3")
                        return 0

            self.gameMenuDisplay.fill((0, 0, 0))

            text, text_rec = self.gen_bienvenida("Bienvenido " + self.user["username"])
            partida1, partida1_rec = self.gen_partida("Partida 1: [Alias]")
            partida2, partida2_rec = self.gen_partida("Partida 2: [Alias]")
            partida3, partida3_rec = self.gen_partida("Partida 3: [Alias]")

            partida1_rec = 50 + text_rec.size[1] * 2
            partida2_rec = 50 + text_rec.size[1] * 4
            partida3_rec = 50 + text_rec.size[1] * 6

            self.gameMenuDisplay.blit(text, (0, 50))
            self.gameMenuDisplay.blit(partida1, (0, partida1_rec))
            self.gameMenuDisplay.blit(partida2, (0, partida2_rec))
            self.gameMenuDisplay.blit(partida3, (0, partida3_rec))

            if partida1_rec <= pygame.mouse.get_pos()[1] <= partida1_rec + partida1.get_height():
                self.gameMenuDisplay.blit(self.obtener_img_personaje(0), (300, 100))
            elif partida2_rec <= pygame.mouse.get_pos()[1] <= partida2_rec + partida2.get_height():
                self.gameMenuDisplay.blit(self.obtener_img_personaje(1), (300, 100))
            elif partida3_rec <= pygame.mouse.get_pos()[1] <= partida3_rec + partida3.get_height():
                self.gameMenuDisplay.blit(self.obtener_img_personaje(0), (300, 100))

            pygame.display.update()
            self.clock.tick(60)
