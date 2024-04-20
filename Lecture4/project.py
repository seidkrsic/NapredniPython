
import pygame 

pygame.init() 

WIN = pygame.display.set_mode((500,500)) 
pygame.display.set_caption("First Game") 
clock = pygame.time.Clock()

run = True 
FPS = 60


x = 0 
y = 430 
height = 60
width = 40
speed = 5 

# promjenljive vezane za skok naseg lika 
isJump = False  
jumpCount = 10 


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



    if not isJump: 
        if keys[pygame.K_SPACE]: 
            isJump = True 

    else: 
            # ovdje se desava skok 
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5 
                jumpCount -= 1 
                
            else: 
                # ovdje treba da ga zaustavimo da skace 
                isJump = False 
                jumpCount = 10 




    WIN.fill((0,0,0)) 
    pygame.draw.rect(WIN, (255, 0,0), (x,y, width, height)) 
    pygame.display.update() 
    

pygame.quit()

