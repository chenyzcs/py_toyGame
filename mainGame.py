# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from gameLevel import *
from myClass import *

print "hi"

pygame.init()
screen = pygame.display.set_mode((600, 400))
gray = (130, 84, 70)
red = (255, 255, 255)


def collide(ball, block):

    # print type(block)
    if block.name == 'Paddle':
        blockRec = pygame.Surface.get_rect(block.img)
    else:
        blockRec = pygame.Rect(block.Rect)
    blockWidth = blockRec.width
    blockHeight = blockRec.height

    isCollide = False
    if ball.x >= block.x and ball.x <= block.x + blockWidth:
        if ball.y >= block.y - Ball.ballRid and ball.y <= block.y + blockHeight + Ball.ballRid:
            if block.y - Ball.ballRid <= ball.y <= block.y:
                ball.y = block.y - Ball.ballRid
            elif block.y + blockHeight <= ball.y <= block.y + blockHeight + Ball.ballRid:
                ball.y = block.y + blockHeight + Ball.ballRid
            ball.yBallReverse()
            isCollide = True
    elif ball.y + Ball.ballRid >= block.y and ball.y - Ball.ballRid <= block.y + blockHeight:
        if ball.x - Ball.ballRid <= block.x + blockWidth and ball.x + Ball.ballRid >= block.x:
            if block.x - Ball.ballRid <= ball.x <= block.x:
                ball.x = block.x - Ball.ballRid
            elif block.x + blockWidth <= ball.x <= block.x + blockWidth + Ball.ballRid:
                ball.x = block.x + blockWidth + Ball.ballRid
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


clsPaddle = Paddle(screen)
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
