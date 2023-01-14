import pygame as py
import sys
from game import Game
from constants import *

py.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption('Ball Game')


def main():
    game = Game()
    clock = py.time.Clock()
    while True:
        screen.fill(BLACK)
        game.rect = py.draw.rect(screen, WHITE, (game.rect_x, game.rect_y, 10, 100))
        #game.handle_keys()
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            # if event.type == py.KEYDOWN:
            #     if event.key == py.K_DOWN:
            #         dist = 1
            #         game.rect.move_ip(100, 100)
        
        
        #py.time.delay(10)
        if game.running:
            ball = py.draw.circle(screen, WHITE, (game.ball_x, game.ball_y), 10, 10)
            game.move(ball)
            
            #py.display.update()
                #py.time.delay(100) 
            if game.rect.colliderect(ball): #ball.left - 10 < game.rect.right and ball.top > game.rect.top and ball.bottom < game.rect.bottom:
                #print(game.rect.right, ball.left)
                game.ball_x_m = game.ball_x_m - 5
                game.count += 1
                #print(game.count)
            game.handle_keys()
        font = font = py.font.Font('freesansbold.ttf', 24)
        points_text = font.render(f'Points: {game.points}', True, POINTS_COLOR, BLACK)
        pointsRect = points_text.get_rect()
        pointsRect.center = (WIDTH - 150, 20)
        screen.blit(points_text, pointsRect)
        lives_text = font.render(f'Lives: {game.lives}', True, LIVES_COLOR, BLACK)
        livesRect = lives_text.get_rect()
        livesRect.center = (WIDTH - 450, 20)
        screen.blit(lives_text, livesRect)
        if game.lives <= 0:
            game.running = False
            font = font = py.font.Font('freesansbold.ttf', 72)
            text = font.render(f'GAME OVER', True, POINTS_COLOR, BLACK)
            textRect = text.get_rect()
            textRect.center = (WIDTH//2, HEIGHT//2)
            screen.blit(text, textRect)
            py.display.update()
            py.time.delay(2000)
            
        py.display.update()
        clock.tick(game.speed)

main()