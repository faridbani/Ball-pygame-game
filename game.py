# Class Game
import pygame as py
from constants import *

class Game:
    def __init__(self) -> None:
        self.ball_x = WIDTH - 200
        self.ball_y = 10
        self.ball_m = 3
        self.ball_x_m = self.ball_m
        self.ball_y_m = self.ball_m
        self.rect_x = 10
        self.rect_y = 10
        self.rect = None #py.draw.rect(screen, WHITE, py.Rect(self.rect_x, self.rect_y, 10, 100))
        self.running = True
        self.speed = 60
        self.count = 0
        self.points = 0
        self.lives = 50
        
    def move(self, ball):
        if self.ball_x > WIDTH:
            self.ball_x_m = self.ball_m + 5
        if self.ball_x <= 0:
            self.lives -= 1
            self.ball_x_m = self.ball_x_m - 5
            #self.speed += 1  
        if self.ball_y > HEIGHT:
            self.ball_y_m = -self.ball_m
        if self.ball_y < 0:
            self.ball_y_m = self.ball_m
        if self.count > 5:
            self.points += 1 
            self.count = 0
            self.speed += 3
        self.ball_x -= self.ball_x_m
        self.ball_y += self.ball_y_m
    def handle_keys(self):
        key = py.key.get_pressed()
        if HEIGHT < self.rect_y:
            self.rect_y = HEIGHT
        if self.rect_y < 0:
            self.rect_y = 0
        if key[py.K_UP]:
            self.rect_y -= 5
        if key[py.K_DOWN]:
            self.rect_y += 5