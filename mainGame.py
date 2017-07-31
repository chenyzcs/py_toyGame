# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from gameLevel import *
from myClass import *

pygame.init()
screen = pygame.display.set_mode((600, 400))
gray = (130, 84, 70)
red = (255, 255, 255)
paddle = pygame.image.load("py_toyGame/img/paddle.png").convert_alpha()


def collide(ball, block):
    isCollide = False
    if ball.x >= block.x and ball.x <= block.x + 85:
        if ball.y >= block.y - Ball.ballRid and ball.y <= block.y + 20 + Ball.ballRid:
            ball.yBallReverse()
            isCollide = True
    elif ball.y + Ball.ballRid >= block.y and ball.y - Ball.ballRid <= block.y + 21:
        if ball.x - Ball.ballRid <= block.x + 85 and ball.x + Ball.ballRid >= block.x:
            ball.xBallReverse()
            isCollide = True

    return isCollide


def isBallCollidePaddle(ball, block):
    collide(ball, block)


def isBallCollideEmeny(ball, emeny):
    isCollide = collide(ball, emeny)
    if isCollide:
        emeny.lives -= 1
        if emeny.lives < 1:
            emeny.alive = False


clsPaddle = Paddle(screen, paddle)
framerate = pygame.time.Clock()
clsBall = Ball(screen)
clsEmeny = Enemy(screen)

while True:
    framerate.tick(60)
    screen.fill(gray)
    # pygame.draw.circle(screen, red, [0, 0], 30, 0)
    clsBall.draw()
    clsBall.moveBall()
    clsPaddle.draw()
    clsEmeny.draw()

    isBallCollidePaddle(clsBall, clsPaddle)
    if clsEmeny.alive:
        isBallCollideEmeny(clsBall, clsEmeny)
    pygame.display.update()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
        clsPaddle.moveLeft()
    elif pressed_keys[K_RIGHT]:
        clsPaddle.moveRight()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
