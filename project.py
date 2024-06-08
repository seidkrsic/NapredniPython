
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
        self.left = True 
        self.right = False   
        self.walkCount = 0 
        self.standing = True 
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

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
        
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) 

class Enemy: 
    # ovdje dodajemo slike 
    walkLeft = [pygame.image.load("L1E.png"),pygame.image.load("L2E.png"),pygame.image.load("L3E.png"),pygame.image.load("L4E.png"),pygame.image.load("L5E.png"),pygame.image.load("L6E.png"),pygame.image.load("L7E.png"),pygame.image.load("L8E.png"),pygame.image.load("L9E.png"),pygame.image.load("L10E.png"),pygame.image.load("L11E.png")]
    walkRight = [pygame.image.load("R1E.png"),pygame.image.load("R2E.png"),pygame.image.load("R3E.png"),pygame.image.load("R4E.png"),pygame.image.load("R5E.png"),pygame.image.load("R6E.png"),pygame.image.load("R7E.png"),pygame.image.load("R8E.png"),pygame.image.load("R9E.png"), pygame.image.load("R10E.png"),pygame.image.load("R11E.png")]

    def __init__(self, x, y, width, height, end): 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.end = end 
        self.path = [x, end] 
        self.walkCount = 0 
        self.speed = 2
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) 
    
    def draw(self, win): 
        self.move() 

        if self.walkCount + 1 > 32: 
            self.walkCount = 0 
        
        if self.speed > 0:
             # if we move right 
            WIN.blit(self.walkRight[self.walkCount//3], (self.x, self.y)) 
            self.walkCount += 1  
        else: 
            # if we move left 
            WIN.blit(self.walkLeft[self.walkCount//3], (self.x, self.y)) 
            self.walkCount += 1 

        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) 


    def move(self):
        if self.speed > 0: # this is when we move right 
            if self.x + self.speed < self.path[1]: 
                self.x += self.speed 
            else: # we change direction 
                self.speed = self.speed * (-1) 
                self.x += self.speed 
                self.walkCount = 0 

        else: # this is when we move left 
            if self.x + self.speed > self.path[0]: 
                self.x += self.speed 
            else: 
                self.speed = self.speed * (-1) 
                self.x += self.speed 
                self.walkCount = 0 

    def hit(self):
        print("Hit")  

class Projectile:
    def __init__(self, x, y, radius, color, facing): 
        self.x = x 
        self.y = y 
        self.radius = radius 
        self.color = color 
        self.facing = facing 
        self.speed = 8 * facing 
    
    def draw(self, win): 
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius) 



def redrawGameWindow():
    # global walkCount 
    WIN.blit(bg, (0,0))
    man.draw(WIN)
    goblin.draw(WIN) 
    for bullet in bullets:
        bullet.draw(WIN) 


    pygame.display.update() 



man = Player(450, 400,40, 60) 
goblin = Enemy(2, 400, 64, 64, 450) 
shootLoop = 0 
bullets = [] # list of projectiles 

while run: 
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 
    
    for bullet in bullets: 

        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit() 
                bullets.pop(bullets.index(bullet)) 


        if bullet.x < 500 and bullet.x > 0: 
            # here we move projectile left or right 
            bullet.x += bullet.speed 
        else: 
            # here we delete projectile
            bullets.pop(bullets.index(bullet)) 


    keys = pygame.key.get_pressed() 

    if shootLoop > 0: 
        shootLoop += 1 
    
    if shootLoop > 15: 
        shootLoop = 0 

    # here we create bullets 
    if keys[pygame.K_SPACE] and shootLoop == 0: 
        if man.right: 
            facing = 1 
        else: 
            facing = -1 

        if len(bullets) < 6:
            bullets.append(Projectile(round(man.x+man.width//2),round(man.y+man.height//2), 6, (0,0,0), facing))   

        shootLoop = 1 


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






