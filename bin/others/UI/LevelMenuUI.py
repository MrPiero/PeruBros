import pygame
import bin.constants as GC


def gen_region(region_state):
    font = pygame.font.Font(GC.FONT_PATH, 35)
    text_surf = font.render(GC.REGIONS[region_state], True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    return Region(text_surf, text_rect, GC.REGIONS[region_state])


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
        self.wallpaper = self.obtener_fondo(region)

    def obtener_avance(self, region):
        for i in range(1, 4):
            self.levels.append(gen_level(region, pos=i))

    def get_top_center(self):
        x = (800/2) - (self.rect.width/2)
        return x, 50

    def obtener_fondo(self, region):
        return pygame.image.load(GC.RESOURCES_OTHERS+region+".jpg")


class Level:
    def __init__(self, text, rect, pos):
        self.text = text
        self.rect = rect
        self.top_center = self.get_top_center(pos)

    def get_top_center(self, pos):
        if pos == 1:
            x = 50
        elif pos == 2:
            x = (800/2) - (self.rect.width/2)
        else:
            x = 550
        return x, 550


class Flecha:
    def __init__(self, file):
        self.img = get_img_others(file)


class LevelUIMenu:
    def __init__(self, progress=(2, 2)):
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
        region = gen_region(region_state-1)
        while level_menu_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN:
                    mouse = pygame.mouse.get_pos()
                    if FI_area.collidepoint(mouse) or event.key == pygame.K_LEFT:
                        if region_state == 1:
                            region_state = 3
                        else:
                            region_state -= 1
                        region = gen_region(region_state-1)
                        print("F. IZQUIERDA")
                    if FD_area.collidepoint(mouse) or event.key == pygame.K_RIGHT:
                        if region_state == 3:
                            region_state = 1
                        else:
                            region_state += 1
                        region = gen_region(region_state-1)
                        print("F. DERECHA")

            self.levelMenuDisplay.blit(region.wallpaper, (0, 0))

            flechaI = Flecha("flecha_izquierda.png")
            flechaD = Flecha("flecha_derecha.png")
            FI_area = self.levelMenuDisplay.blit(flechaI.img, (0, 0))
            FD_area = self.levelMenuDisplay.blit(flechaD.img, (700, 0))

            self.levelMenuDisplay.blit(region.text, region.get_top_center())
            for i in region.levels:
                pygame.draw.rect(self.levelMenuDisplay, GC.RED, (i.top_center[0], i.top_center[1], i.rect.width, i.rect.height))
                self.levelMenuDisplay.blit(i.text, i.top_center)
                if region_state > self.progress[0] or (region_state == self.progress[0] and region.levels.index(i)+1 > self.progress[1]):
                    pygame.draw.rect(self.levelMenuDisplay, GC.BLACK, (i.top_center[0], i.top_center[1], i.rect.width, i.rect.height))
                

            pygame.display.update()
            self.clock.tick(60)
