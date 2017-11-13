import pygame
import bin.constants as GC


def gen_region(region_state):
    font = pygame.font.Font(GC.FONT_PATH, 35)
    if region_state == 1:
        text = "COSTA"
    elif region_state == 2:
        text = "SIERRA"
    else:
        text = "SELVA"
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    return Region(text_surf, text_rect, text)


def gen_level(text="[LEVEL ???]", pos=1):
    font = pygame.font.Font(GC.FONT_PATH, 20)
    text_surf = font.render((GC.LEVELS.get(text))[pos-1], True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    return Level(text_surf, text_rect, pos)


def get_img_others(file):
    return pygame.image.load(GC.RESOURCES_OTHERS + file)


class Region:
    def __init__(self, text, rect, region):
        self.text = text
        self.rect = rect
        self.levels = []
        self.obtener_avance(region)

    def obtener_avance(self, region):
        for i in range(1, 4):
            self.levels.append(gen_level(region, pos=i))

    def get_top_center(self):
        x = (800/2) - (self.rect.width/2)
        return x, 50


class Level:
    def __init__(self, text, rect, pos):
        self.text = text
        self.rect = rect
        self.top_center = self.get_top_center(pos)

    def get_top_center(self, pos):
        if pos == 1:
            x = 150
        elif pos == 2:
            x = (800/2) - (self.rect.width/2)
        else:
            x = 650
        return x, 550


class Flecha:
    def __init__(self, file):
        self.img = get_img_others(file)


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
        region_state = 1
        region = gen_region(region_state)
        while level_menu_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse = pygame.mouse.get_pos()
                    if FI_area.collidepoint(mouse):
                        if region_state == 1:
                            region_state = 3
                        else:
                            region_state -= 1
                        region = gen_region(region_state)
                        print("F. IZQUIERDA")
                    if FD_area.collidepoint(mouse):
                        if region_state == 3:
                            region_state = 1
                        else:
                            region_state += 1
                        region = gen_region(region_state)
                        print("F. DERECHA")

            self.levelMenuDisplay.fill((119, 136, 153))

            flechaI = Flecha("flecha_izquierda.png")
            flechaD = Flecha("flecha_derecha.png")
            FI_area = self.levelMenuDisplay.blit(flechaI.img, (0, 0))
            FD_area = self.levelMenuDisplay.blit(flechaD.img, (700, 0))

            self.levelMenuDisplay.blit(region.text, region.get_top_center())
            for i in region.levels:
                self.levelMenuDisplay.blit(i.text, i.top_center)

            pygame.display.update()
            self.clock.tick(60)
