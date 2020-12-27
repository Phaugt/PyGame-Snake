import pygame
import time
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
 
game_y = 500
game_x  = 500
playboard = pygame.display.set_mode((game_x, game_y))
pygame.display.set_caption('Snake by pythonexplainedto.me')
 
game_over = False
 
x1 = game_x/2
y1 = game_y/2
 
snake_block=10
 
x1_change = 0
y1_change = 0
 
clock = pygame.time.Clock()
snake_speed=20
 
font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    note = font_style.render(msg, True, color)
    playboard.blit(note, [150, 250])
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
 
    if x1 >= game_x or x1 < 0 or y1 >= game_y or y1 < 0:
        game_over = True #if border is hit = game over
 
    x1 += x1_change
    y1 += y1_change
    playboard.fill(black)
    pygame.draw.rect(playboard, white, [x1, y1, snake_block, snake_block]) #we draw our snake in the middle of the screen
 
    pygame.display.update()
 
    clock.tick(snake_speed)
 
message("Game Over!",yellow)
pygame.display.update()
time.sleep(2) #exits the game 2 seconds after game over
 
pygame.quit()
quit()
