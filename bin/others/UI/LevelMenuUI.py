import pygame
import bin.constants as GC


def gen_region(text="[REGIÓN]"):
    font = pygame.font.Font(GC.FONT_PATH, 35)
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    return Region(text_surf, text_rect)


def gen_level(text="[LEVEL]"):
    font = pygame.font.Font(GC.FONT_PATH, 20)
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    return Level(text_surf, text_rect)


class Region:
    def __init__(self, text, rect):
        self.text = text
        self.rect = rect
        self.levels = self.obtener_avance()

    def obtener_avance(self):
        avance = []
        avance.append(gen_level())
        return avance

    def get_top_center(self):
        x = (800/2) - (self.rect.width/2)
        return x, 50


class Level:
    def __init__(self, text, rect):
        self.text = text
        self.rect = rect

    def get_top_center(self):
        x = (800/2) - (self.rect.width/2)
        return x, 550


class LevelUIMenu:
    def __init__(self, progress=1):
        pygame.init()

        self.display_width = 800
        self.display_height = 600

        self.levelMenuDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("PERUBROS. -- PRE-ALPHA LEVEL MENU --")
        self.clock = pygame.time.Clock()
        self.progress = progress

    def main_menu(self):
        level_menu_state = True
        while level_menu_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    level_menu_state = False

            self.levelMenuDisplay.fill((0, 0, 0))

            region = gen_region("COSTA")
            self.levelMenuDisplay.blit(region.text, region.get_top_center())
            self.levelMenuDisplay.blit(region.levels[0].text, region.levels[0].get_top_center())

            pygame.display.update()
            self.clock.tick(60)
