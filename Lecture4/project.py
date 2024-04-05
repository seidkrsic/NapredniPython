import pygame
import os 

def main(): 
    global walkCount, left, right 
    pygame.init()
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("First Game")
    clock = pygame.time.Clock()
    folder_name = "/Users/seidkrsic/Desktop/Python_Pygame/Lecture4/Game"
    # Define lists to hold the loaded images
    walkRight = []
    walkLeft = []

    # Load images for walkRight
    for i in range(1, 10):
        image_path = os.path.join(folder_name, f'R{i}.png')
        walkRight.append(pygame.image.load(image_path))

    # Load images for walkLeft
    for i in range(1, 10):
        image_path = os.path.join(folder_name, f'L{i}.png')
        walkLeft.append(pygame.image.load(image_path))
    bg = pygame.image.load(os.path.join(folder_name,'bg.jpg'))
    char = pygame.image.load(os.path.join(folder_name,'standing.png'))

    vel = 5
    width = 64
    height = 64
    x = 480 - vel - width
    y = 480 - vel - height
    run = True
    isJump = False
    jumpCount = 10
    left = False
    right = False
    walkCount = 0


    def redrawGameWindow(): 
        global walkCount
        win.blit(bg,(0,0))
        if walkCount + 1 >= 27:
            walkCount = 0
            
        if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            win.blit(char, (x, y))
            walkCount = 0
        

        pygame.display.update() 

    while run:
        clock.tick(60) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > vel: # We can check if a key is pressed like this
            x -= vel 
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
            x += vel 
            left = False
            right = True
        else: 
            # If the character is not moving we will set both left and right false and reset the animation counter (walkCount)
            left = False
            right = False
            walkCount = 0

        if not isJump:
            if keys[pygame.K_SPACE]: 
                isJump = True 
        else: 
            if jumpCount >= -10:
                neg = 1 
                if jumpCount < 0: 
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else: 
                # This will execute if our jump is finished
                jumpCount = 10
                isJump = False
        redrawGameWindow()

    pygame.quit()  # If we exit the loop this will execute and close our game


main()