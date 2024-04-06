
import pygame 

pygame.init() 

WIN = pygame.display.set_mode((500,500)) 
pygame.display.set_caption("First Game") 
clock = pygame.time.Clock()

run = True 
FPS = 60


x = 0 
y = 0 
height = 60
width = 40
speed = 5 



while run: 
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed 
    if keys[pygame.K_RIGHT] and x < 500 - width - speed:
        x += speed 
    if keys[pygame.K_UP] and y > speed:  
        y -= speed 
    if keys[pygame.K_DOWN] and y < 500 - height -speed:
        y += speed 

    WIN.fill((0,0,0)) 
    pygame.draw.rect(WIN, (255, 0,0), (x,y, width, height)) 
    pygame.display.update() 
    

pygame.quit()

