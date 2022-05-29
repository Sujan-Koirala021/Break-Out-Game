from re import X
from tkinter import Y
import pygame, time
from pygame.locals import *

WIDTH, HEIGHT = 800, 600
CAPTION= "Smash Brick"
white = (255, 255, 255)

#   Animation
countrate = pygame.time.Clock()
fps = 60


def createWindow(w,h, caption): 
    global win
    pygame.init()
    win = pygame.display.set_mode((w, h))
    pygame.display.set_caption(caption)
createWindow(WIDTH, HEIGHT, CAPTION)

#   Ball
ballx, bally = 400, 300
ball_speedX = 5
ball_speedY = 5

running = True

#   Paddle
paddlex, paddley  = WIDTH/2-20, HEIGHT -70
class Paddle:
    width, height = 140, 15
    def __init__(self, paddlex, paddley):
        self.x = paddlex
        self.y = paddley
        
    def createPaddle(self):
        #   Get mouse postion as a tuple
        mx, my = pygame.mouse.get_pos()
        #   Set 'y' to original value to avoid moving up and down
        if (mx >= 655):     self.x = 655
        else:   self.x = mx           
        self.y = paddley
        self.paddleBody = pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height) )
        

class Ball:
    height = 10
    width = 10
    def __init__(self, x,y , velocityX, velocityY):
        self.x = x
        self.y = y
        self.velx= velocityX
        self.vely = velocityY
    def createBall(self):
        self.ballBody = pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height) )
        self.ball_bouncing_mechanism()
        self.moveBall()
        
    def moveBall(self):
        self.x += self.velx
        self.y += self.vely
    
    def ball_bouncing_mechanism(self):
        if self.x <= 0:
            self.velx *= -1
        if self.x >= WIDTH - 10:
            self.velx *= -1
        if self.y <=5 :
            self.vely *= -1
        if self.y >= HEIGHT - 10:
            self.vely *= -1

class Brick:
    def __init__(self, x, y,isVisible):
        self.x = x
        self.y = y
        self.width = 59
        self.height = 15
        self.isVisible = isVisible
        
    def makeBrick(self):
        self.brickBody  = pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height) )

#   Creating paddle object
paddle = Paddle(paddlex, paddley)
#   Creating ball
ball = Ball(ballx, bally, ball_speedX, ball_speedY)

def check_collision(ball_body, paddle_body):
    if (ball_body.colliderect(paddle_body) and ball.y> (paddle.y - 5) and ball.x > paddle.x and ball.x < paddle.x + 130):    #checks for collision
        ball.vely  *= -1


    
brickList = []

def addBricks():
    global brickList
    brickList = []
    for i in range(6):
        for j in range(11):
            brickList.append(Brick(24 +j *69, 28 + i* 35 , True))

addBricks()



while (running):
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                running = False
                
    win.fill((0, 0,0))
    for item in brickList:
        item.makeBrick()
    
    paddle.createPaddle()
    ball.createBall()
    check_collision(ball.ballBody, paddle.paddleBody)
    pygame.display.update()
    countrate.tick(fps)
    