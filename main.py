import pygame as snake_game
import time
import random
 
snake_game.init()

yellow = (254,211,105)
bg = (57,62,70)
textclr = (238,238,238)
foodclr = (56,126,184)

game_y = 500
game_x  = 500
playboard = snake_game.display.set_mode((game_x, game_y))
snake_game.display.set_icon(snake_game.image.load('logo.png'))
snake_game.display.set_caption('Snake by pythonexplainedto.me')
 
clock = snake_game.time.Clock()
 
snake_block = 10
snake_speed = 20
 
font_style = snake_game.font.SysFont("arial", 25)
score_font = snake_game.font.SysFont("arial", 35)
 
 
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    playboard.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        snake_game.draw.rect(playboard, yellow, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    note = font_style.render(msg, True, color)
    playboard.blit(note, [30, 250])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = game_x / 2
    y1 = game_y / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, game_x - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, game_y - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            playboard.fill(bg)
            message("You Lost! Press R-Play Again or E-Exit!", textclr)
            Your_score(Length_of_snake - 1)
            snake_game.display.update()
 
            for event in snake_game.event.get():
                if event.type == snake_game.KEYDOWN:
                    if event.key == snake_game.K_e:
                        game_over = True
                        game_close = False
                    if event.key == snake_game.K_r:
                        gameLoop()
 
        for event in snake_game.event.get():
            if event.type == snake_game.QUIT:
                game_over = True
            if event.type == snake_game.KEYDOWN:
                if event.key == snake_game.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == snake_game.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == snake_game.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == snake_game.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= game_x or x1 < 0 or y1 >= game_y or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        playboard.fill(bg)

        snake_game.draw.rect(playboard, foodclr, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        snake_game.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, game_x - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, game_y - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    snake_game.quit()
    quit()
 
 
gameLoop()
