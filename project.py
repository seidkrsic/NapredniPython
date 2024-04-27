
import pygame 

pygame.init() 

WIN = pygame.display.set_mode((500,480))  
pygame.display.set_caption("First Game") 
clock = pygame.time.Clock()

run = True 
FPS = 60 

# ovdje dodajemo slike 
walkLeft = [pygame.image.load("L1.png"),pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png"),pygame.image.load("L5.png"),pygame.image.load("L6.png"),pygame.image.load("L7.png"),pygame.image.load("L8.png"),pygame.image.load("L9.png")]
walkRight = [pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),pygame.image.load("R6.png"),pygame.image.load("R7.png"),pygame.image.load("R8.png"),pygame.image.load("R9.png")]
bg = pygame.image.load("bg.jpg") 
char = pygame.image.load("standing.png") 

x = 0 
y = 400 
height = 60
width = 40
speed = 5 

# promjenljive vezane za skok naseg lika 
isJump = False  
jumpCount = 10 

left = False 
right = False 
walkCount = 0 


def redrawGameWindow():
    global walkCount 
    WIN.blit(bg, (0,0))
    if walkCount > 26: 
        walkCount = 0

    if left: 
        WIN.blit(walkLeft[walkCount//3],(x,y))
        walkCount +=1 
    elif right: 
        WIN.blit(walkRight[walkCount//3], (x,y)) 
        walkCount +=1 
    else: 
        WIN.blit(char, (x,y)) 

    pygame.display.update() 





while run: 
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed 
        # ovo smo dodali zbog slika 
        left = True 
        right = False 
    elif keys[pygame.K_RIGHT] and x < 500 - width - speed:
        x += speed 
        # ovo smo dodali zbog slika 
        right = True 
        left = False  
    else: 
        # ovo smo dodali zbog slika 
        left = False 
        right = False 
        walkCount = 0 



    if not isJump: 
        if keys[pygame.K_SPACE]: 
            isJump = True
            # ovo smo dodali zbog slika  
            left = False 
            right = False 
            walkCount = 0 

    else: 
            # ovdje se desava skok 
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5 
                jumpCount -= 1 
                
            else: 
                # ovdje treba da ga zaustavimo da skace 
                isJump = False 
                jumpCount = 10 



    
    redrawGameWindow()
    # pygame.draw.rect(WIN, (255, 0,0), (x,y, width, height)) 
   
    

pygame.quit()






