
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


class Player: 
    def __init__(self, x, y,width, height):
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.speed = 5
        self.isJump = False 
        self.jumpCount = 10 
        self.left = False 
        self.right = True  
        self.walkCount = 0 
        self.standing = True 

    def draw(self, win): 
        if man.walkCount > 26: 
            man.walkCount = 0


        if man.left: 
            WIN.blit(walkLeft[man.walkCount//3],(man.x,man.y))
            man.walkCount +=1 
        elif man.right: 
            WIN.blit(walkRight[man.walkCount//3], (man.x,man.y)) 
            man.walkCount +=1 
        else: 
            if self.left: 
                WIN.blit(walkLeft[0], (man.x,man.y)) 
            else: 
                WIN.blit(walkRight[0], (man.x,man.y)) 


class Projectile:
    def __init__(self,x, y, radius, color, facing): 
        self.x = x 
        self.y = y 
        self.radius = radius 
        self.color = color 
        self.facing = facing 
    
    def draw(self, win): 
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius) 




def redrawGameWindow():
    # global walkCount 
    WIN.blit(bg, (0,0))
    man.draw(WIN)


    pygame.display.update() 



man = Player(0, 400,40, 60) 



while run: 
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and man.x > man.speed - man.width//2:
        man.x -= man.speed 
        # ovo smo dodali zbog slika 
        man.left = True 
        man.right = False 
        man.standing = False 
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.speed:
        man.x += man.speed 
        # ovo smo dodali zbog slika 
        man.right = True 
        man.left = False  
        man.standing = False 
    else: 
        # ovo smo dodali zbog slika 
        man.standing = True 
        man.walkCount = 0 



    if not man.isJump: 
        if keys[pygame.K_UP]: 
            man.isJump = True
            # ovo smo dodali zbog slika  
            man.walkCount = 0 

    else: 
            # ovdje se desava skok 
            if man.jumpCount >= -10:
                man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5 
                man.jumpCount -= 1 
                
            else: 
                # ovdje treba da ga zaustavimo da skace 
                man.isJump = False 
                man.jumpCount = 10 



    
    redrawGameWindow()
    # pygame.draw.rect(WIN, (255, 0,0), (x,y, width, height)) 
   
    

pygame.quit()






