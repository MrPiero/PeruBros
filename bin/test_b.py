import pygame

class Game:
    def __init__(self, state, state_o, screen):
        self.state = state
        self.state_o = state_o
        self.screen = screen

    def event(self):
        self.state.event()

    def update(self):
        self.state.update()

    def draw(self):
        pass

