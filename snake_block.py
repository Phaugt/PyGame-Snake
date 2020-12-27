import pygame
pygame.init()
 
white = (255, 255, 255)

 
game_y = 500
game_x  = 500
playboard = pygame.display.set_mode((game_x, game_y))
pygame.display.set_caption('Snake by pythonexplainedto.me')
 
game_over = False
 
x1 = game_x/2
y1 = game_y/2
 
snake_block=10


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    pygame.draw.rect(playboard, white, [x1, y1, snake_block, snake_block])
 
    pygame.display.update()

pygame.quit()
quit()