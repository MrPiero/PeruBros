import pygame
#import constants
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.pos = vec(x,y)
        self.vel = vec(0,0)
        self.image = pygame.Surface((70,70))
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.vel.y += -2
        if keys[pygame.K_LEFT]:
            self.vel.x += -2
        if keys[pygame.K_RIGHT]:
            self.vel.x += 2

        self.pos.x = self.vel.x
        self.pos.y = self.vel.y


