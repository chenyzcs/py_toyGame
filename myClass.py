import pygame
import os

pwd = os.getcwd()
# print pwd

paddle_src = pwd + '/img/paddle.png'


class Block(object):
    """docstring for Block."""

    def __init__(self, screen, block):
        super(Block, self).__init__()
        self.name = "Block"
        self.screen = screen
        self.x = 0
        self.y = 0
        self.block = block

    def draw(self):
        self.screen.blit(self.block, (self.x, self.y))


class Paddle(Block):
    """docstring for Paddle."""
    moveSpeed = 10

    def __init__(self, screen):
        self.name = "Paddle"
        self.screen = screen
        self.x = 250
        self.y = 350
        self.img_src = paddle_src
        self.img = pygame.image.load(self.img_src).convert_alpha()

    def moveLeft(self):
        self.x -= Paddle.moveSpeed
        if self.x <= 0:
            self.x = 0

    def moveRight(self):
        self.x += Paddle.moveSpeed
        if self.x >= 520:
            self.x = 520

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))


class Ball(object):
    """This class for Ball"""

    ballSpeed = 2
    ballRid = 15

    def __init__(self, screen):
        self.name = "Ball"
        self.x = 250
        self.y = 250
        self.xSpeed = Ball.ballSpeed
        self.ySpeed = Ball.ballSpeed
        self.screen = screen
        self.color = 255, 0, 0
        # self.color = red

    def moveBall(self):

        if self.x < Ball.ballRid or self.x > 600 - Ball.ballRid:
            # self.x -= Ball.ballSpeedhhhhhh
            if self.x < Ball.ballRid:
                self.x = Ball.ballRid
            else:
                self.x = 600 - Ball.ballRid
            self.xSpeed *= -1

        elif self.y < Ball.ballRid or self.y > 400 - Ball.ballRid:
            if self.y < Ball.ballRid:
                self.y = Ball.ballRid
            else:
                self.y = 400 - Ball.ballRid
            self.ySpeed *= -1
            # self.y -= Ball.ballSpeed
        self.x += self.xSpeed
        self.y += self.ySpeed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y],
                           Ball.ballRid, 0)

    def xBallReverse(self):
        self.xSpeed *= -1
        self.moveBall()

    def yBallReverse(self):
        self.ySpeed *= -1
        self.moveBall()

    def xyBallReverse(self):
        self.xSpeed *= -1
        self.ySpeed *= -1
