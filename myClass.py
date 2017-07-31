import pygame


class Block(object):
    """docstring for Block."""

    def __init__(self, screen, block):
        super(Block, self).__init__()
        self.screen = screen
        self.x = 0
        self.y = 0
        self.block = block

    def draw(self):
        self.screen.blit(self.block, (self.x, self.y))


class Paddle(Block):
    """docstring for Paddle."""
    moveSpeed = 10

    def __init__(self, screen, paddle):
        self.screen = screen
        self.block = paddle
        self.x = 250
        self.y = 350

    def moveLeft(self):
        self.x -= Paddle.moveSpeed
        if self.x <= 0:
            self.x = 0

    def moveRight(self):
        self.x += Paddle.moveSpeed
        if self.x >= 520:
            self.x = 520


class Ball(object):
    """This class for Ball"""

    ballSpeed = 2
    ballRid = 15

    def __init__(self, screen):
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
            self.xSpeed *= -1

        elif self.y < Ball.ballRid or self.y > 400 - Ball.ballRid:
            self.ySpeed *= -1
            # self.y -= Ball.ballSpeed
        self.x += self.xSpeed
        self.y += self.ySpeed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y],
                           Ball.ballRid, 0)

    def xBallReverse(self):
        self.xSpeed *= -1

    def yBallReverse(self):
        self.ySpeed *= -1
