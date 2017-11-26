import pygame
import sys
import bin.constants as GC
import bin.others.Data.DAO as DAO


def gen_region(region_state, p):
    font = pygame.font.Font(GC.FONT_PATH, 35)
    text_surf = font.render(GC.REGIONS[region_state], True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    return Region(text_surf, text_rect, GC.REGIONS[region_state], p)


def gen_level(text="[LEVEL ???]", pos=1):
    font = pygame.font.Font(GC.FONT_PATH, 20)
    text_surf = font.render((GC.LEVELS.get(text))[pos-1], True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    return Level(text_surf, text_rect, pos)


def get_img_others(file):
    return pygame.image.load(GC.RESOURCES_OTHERS + file)


def change_region_state(region_state, direction):
    if direction == "L":
        if region_state == 1:
            region_state = 3
        else:
            region_state -= 1
    else:
        if region_state == 3:
            region_state = 1
        else:
            region_state += 1
    return region_state


def check_level_availability(progress, region, level):
    if region > progress[0] or (region == progress[0] and level > progress[1]): return False
    else: return True


class Region:
    def __init__(self, text, rect, region, p):
        self.text = text
        self.rect = rect
        self.levels = []
        self.obtener_avance(region)
        self.wallpaper = self.obtener_fondo(region, p)

    def obtener_avance(self, region):
        for i in range(1, 4):
            self.levels.append(gen_level(region, pos=i))

    def get_top_center(self):
        x = (800/2) - (self.rect.width/2)
        return x, 50

    def obtener_fondo(self, region, p):
        # return pygame.image.load(GC.RESOURCES_OTHERS + region + ".jpg")
        if region == "COSTA":
            return pygame.image.load(GC.RESOURCES_OTHERS + region + ".jpg")
        if region == "SIERRA":
            if p >= 2:
                return pygame.image.load(GC.RESOURCES_OTHERS + region + ".jpg")
            else:
                return pygame.image.load(GC.RESOURCES_OTHERS + region + "_BW.jpg")
        if region == "SELVA":
            if p == 3:
                return pygame.image.load(GC.RESOURCES_OTHERS + region + ".jpg")
            else:
                return pygame.image.load(GC.RESOURCES_OTHERS + region + "_BW.jpg")


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
    def __init__(self, id_char):
        pygame.init()

        self.display_width = 800
        self.display_height = 600

        self.levelMenuDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("PERUBROS. -- PRE-ALPHA LEVEL MENU --")
        self.clock = pygame.time.Clock()
        self.save = DAO.get_progress(id_char)[0]
        self.progress = (int(self.save["region"]), int(self.save["nivel"]))

    def main_menu(self):
        level_menu_state = True
        region_state = 1
        region = gen_region(region_state-1, self.progress[0])
        level_frames = [0, 0, 0]
        while level_menu_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse = pygame.mouse.get_pos()
                    if FI_area.collidepoint(mouse):
                        region_state = change_region_state(region_state, "L")
                        region = gen_region(region_state-1, self.progress[0])
                    if FD_area.collidepoint(mouse):
                        region_state = change_region_state(region_state, "R")
                        region = gen_region(region_state-1, self.progress[0])
                    if level_frames[0].collidepoint(mouse):
                        if check_level_availability(self.progress, region_state, 1): return (region_state, 1)
                        else: print("NIVEL NO PERMITIDO")
                    if level_frames[1].collidepoint(mouse):
                        if check_level_availability(self.progress, region_state, 2): return (region_state, 2)
                        else: print("NIVEL NO PERMITIDO")
                    if level_frames[2].collidepoint(mouse):
                        if check_level_availability(self.progress, region_state, 3): return (region_state, 3)
                        else: print("NIVEL NO PERMITIDO")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        region_state = change_region_state(region_state, "L")
                        region = gen_region(region_state - 1, self.progress[0])
                    if event.key == pygame.K_RIGHT:
                        region_state = change_region_state(region_state, "R")
                        region = gen_region(region_state - 1, self.progress[0])

            self.levelMenuDisplay.blit(region.wallpaper, (0, 0))

            flechaI = Flecha("flecha_izquierda.png")
            flechaD = Flecha("flecha_derecha.png")
            FI_area = self.levelMenuDisplay.blit(flechaI.img, (0, 0))
            FD_area = self.levelMenuDisplay.blit(flechaD.img, (700, 0))

            self.levelMenuDisplay.blit(region.text, region.get_top_center())
            for i in region.levels:
                frame = pygame.draw.rect(self.levelMenuDisplay, GC.RED, (i.top_center[0], i.top_center[1], i.rect.width, i.rect.height))
                self.levelMenuDisplay.blit(i.text, i.top_center)
                if region_state > self.progress[0] or (region_state == self.progress[0] and region.levels.index(i)+1 > self.progress[1]):
                    pygame.draw.rect(self.levelMenuDisplay, GC.SLATEGREY, (i.top_center[0], i.top_center[1], i.rect.width, i.rect.height))
                level_frames[region.levels.index(i)] = frame
            pygame.display.update()
            self.clock.tick(60)
