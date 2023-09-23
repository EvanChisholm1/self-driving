import pygame
from math import sin, cos, degrees
from time import sleep

arrow = pygame.image.load('./arrow.png')
arrow = pygame.transform.scale(arrow, (100, 50))

class Car:
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.window = window
        self.dir = 0
        self.speed = 0
        self.turning = 0
    
    def render(self):
        rect = pygame.surface.Surface((100, 50))
        rect.blit(arrow, (0, 0, 100, 50))
        rotated = pygame.transform.rotate(rect, -degrees(self.dir))
        self.window.blit(rotated, rotated.get_rect(center = (self.x, self.y)))
    
    def update(self):
        if self.turning == 1:
            self.dir += 0.001
        elif self.turning == -1:
            self.dir -= 0.001

        vert_vel = sin(self.dir) * self.speed
        hori_vel = cos(self.dir) * self.speed
        
        self.x += hori_vel * 0.1
        self.y += vert_vel * 0.1
    


pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Self Driving Car")

run = True
c = Car(50, 50, window)

while run:
    window.fill((0, 0, 0))
    c.render()
    c.update()
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                c.speed = 1
            elif event.key == pygame.K_d:
                c.turning = 1
            elif event.key == pygame.K_a:
                c.turning = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                c.speed = 0
            elif event.key == pygame.K_d and c.turning == 1:
                c.turning = 0
            elif event.key == pygame.K_a and c.turning == -1:
                c.turning = 0

pygame.quit()