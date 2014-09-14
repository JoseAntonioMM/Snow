'''
(C) Programmed by:
   	Jose Antonio Medina Martinez


*/

''' 
import pygame
import random
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

fallen_snow = pygame.sprite.Group()
falling_snow = pygame.sprite.Group()
fallen_snow_stop = pygame.sprite.Group()

class Snow(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls """
 
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = pygame.Surface([3, 3])
        self.image.fill(white)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def update(self):
        self.rect.y += 3

for i in range(750):
    x = random.randrange(0, 400) * 3
    y = random.randrange(-50, 225) * 3
    snow = Snow(x,y)
    falling_snow.add(snow)
    
 
pygame.init()
  
# Set the width and height of the screen [width,height]
size = [1200,750]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snow")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while done == False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
    falling_snow.update()
    for snow in falling_snow:
        snow_collided = pygame.sprite.spritecollide(snow, fallen_snow, False)
        for snow_collided in snow_collided:
            fallen_snow.remove(snow_collided)
            fallen_snow_stop.add(snow_collided)
            falling_snow.remove(snow)
            snow.rect.y = snow.rect.y - 3
            fallen_snow.add(snow)
            x = random.randrange(0, 400) * 3
            y = random.randrange(-50, -10) * 3
            snow = Snow(x,y)
            falling_snow.add(snow)
        if snow.rect.y >= 747:
            snow.rect.y = 747
            falling_snow.remove(snow)
            fallen_snow.add(snow)
            x = random.randrange(0, 400) * 3
            y = random.randrange(-50, -10) * 3
            snow = Snow(x,y)
            falling_snow.add(snow)
    
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
     
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(black)
    falling_snow.draw(screen)
    fallen_snow.draw(screen)
    fallen_snow_stop.draw(screen)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit to 30 frames per second
    clock.tick(30)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
