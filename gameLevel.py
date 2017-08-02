# -*- coding:utf-8 -*-

from myClass import *


class Enemy(Block):
    """Document for Enemy"""

    def __init__(self, screen):
        self.name = "Enemy"
        self.x = 100
        self.y = 100
        self.screen = screen
        self.lives = 1
        self.alive = True
        self.color = [216, 220, 216]
        self.width = 150
        self.height = 20
        self.Rect = [self.x, self.y, self.width, self.height]

    def draw(self):
        if (self.lives > 0):
            pygame.draw.rect(self.screen, self.color, self.Rect, 0)
