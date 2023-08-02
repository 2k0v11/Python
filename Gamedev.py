import pygame
pygame.init()

window_x=1000
window_y=700
window=pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("Game development")

icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

spaceship=pygame.image.load("icon.png")
spaceship_x=200
spaceship_y=300

bg = pygame.image.load("Background.jpg");
def display_spaceship(x,y):
    window.blit(spaceship,(x,y))

game=True
while game:
    window.blit(bg,(0,0))
    for even in pygame.event.get():
        if even.type==pygame.QUIT:
         game=False;
    keys= pygame.key.get_pressed()
    #if left arrow is pressed
    if keys[pygame.K_LEFT] and spaceship_x>10:
        spaceship_x-=1
    #if right arrow is pressed   
    if keys[pygame.K_RIGHT] and spaceship_x<700:
        spaceship_x+=1
    if keys[pygame.K_UP]:
        spaceship_y-=1
    if keys[pygame.K_DOWN]:
        spaceship_y+=1
         
   
    display_spaceship(spaceship_x,spaceship_y)
    pygame.display.update()
pygame.quit()
