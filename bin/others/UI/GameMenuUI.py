import pygame
import sys
import requests
import bin.constants as GC
import bin.others.Data.DAO as DAO


def gen_bienvenida(text):
    font = pygame.font.Font(GC.FONT_PATH, 35)
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    return text_surf, text_rect


def gen_partida(text="*** [Crear partida] ***"):
    font = pygame.font.Font(GC.FONT_PATH, 24)
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    return text_surf, text_rect


def obtener_img_personaje(personaje):
    if personaje == "hombre":
        return pygame.image.load('./resources/nino.png') # La imagen cargada ya está diseñada en 8 bits
    elif personaje == "mujer":
        return pygame.image.load('./resources/nina.png') # La imagen cargada NO está diseñada en 8 bits


def obtener_fondo():
    return pygame.image.load(GC.GAME_MENU_WALLPAPER)


def check_save(saves, i):
    try:
        return saves[i]["nombre"]
    except:
        return "*** [Crear partida] ***"


class GameUIMenu:
    def __init__(self, id_user):
        pygame.init()

        self.display_width = 600
        self.display_height = 400

        self.gameMenuDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("PERUBROS. -- GAME MENU --")
        self.clock = pygame.time.Clock()
        self.user = DAO.get_user(id_user)
        self.saves = DAO.get_saves(id_user)

    def main_menu(self):
        game_menu_state = True
        while game_menu_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if partida1_rec <= pygame.mouse.get_pos()[1] <= partida1_rec + partida1.get_height():
                        if self.progress_by_save(0): return DAO.get_progress(self.saves[0]["id"])[0]
                        else: print("PARTIDA 1 INEXISTENTE")
                    elif partida2_rec <= pygame.mouse.get_pos()[1] <= partida2_rec + partida2.get_height():
                        if self.progress_by_save(1): return DAO.get_progress(self.saves[1]["id"])[0]
                        else: print("PARTIDA 2 INEXISTENTE")
                    elif partida3_rec <= pygame.mouse.get_pos()[1] <= partida3_rec + partida3.get_height():
                        if self.progress_by_save(2): return DAO.get_progress(self.saves[2]["id"])[0]
                        else: print("PARTIDA 3 INEXISTENTE")

            self.gameMenuDisplay.blit(obtener_fondo(), (0, 0))

            text, text_rec = gen_bienvenida("Bienvenido " + self.user["name"])
            partida1, partida1_rec = gen_partida(check_save(self.saves, 0))
            partida2, partida2_rec = gen_partida(check_save(self.saves, 1))
            partida3, partida3_rec = gen_partida(check_save(self.saves, 2))

            partida1_rec = 50 + text_rec.size[1] * 2
            partida2_rec = 50 + text_rec.size[1] * 4
            partida3_rec = 50 + text_rec.size[1] * 6

            self.gameMenuDisplay.blit(text, (0, 50))
            self.gameMenuDisplay.blit(partida1, (0, partida1_rec))
            self.gameMenuDisplay.blit(partida2, (0, partida2_rec))
            self.gameMenuDisplay.blit(partida3, (0, partida3_rec))

            if partida1_rec <= pygame.mouse.get_pos()[1] <= partida1_rec + partida1.get_height():
                self.gameMenuDisplay.blit(obtener_img_personaje(self.sex_by_save(0)), (300, 100))
            elif partida2_rec <= pygame.mouse.get_pos()[1] <= partida2_rec + partida2.get_height():
                self.gameMenuDisplay.blit(obtener_img_personaje(self.sex_by_save(1)), (300, 100))
            elif partida3_rec <= pygame.mouse.get_pos()[1] <= partida3_rec + partida3.get_height():
                self.gameMenuDisplay.blit(obtener_img_personaje(self.sex_by_save(2)), (300, 100))

            pygame.display.update()
            self.clock.tick(60)

    def sex_by_save(self, i):
        try:
            return self.saves[i]["sexo"]
        except:
            return "mujer"

    def progress_by_save(self, i):
        try:
            DAO.get_progress(self.saves[i]["id"])[0]
            return True
        except:
            return False
