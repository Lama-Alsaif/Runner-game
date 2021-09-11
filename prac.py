import pygame 
from sys import exit

from pygame.time import Clock
pygame.init()

Screen = pygame.display.set_mode((800, 400))#width , height
pygame.display.set_caption("first game")
clock = pygame.time.Clock()
test_font  = pygame.font.Font('font/Pixeltype.ttf' , 50)#(font type , font size)

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface=pygame.image.load('graphics/ground.png').convert_alpha()
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600 , 300))
player_surf = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80 , 300))

text_surface= test_font.render('My game', False , 'Black')#text , AA ,color
#surface= pygame.Surface((100,200)) #W,H (display surface and regular surface have alot of things in commen)
#surface.fill('Red')


while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    snail_rect.left -= 5
    if snail_rect.right <= 0 : snail_rect.left = 800
    
    Screen.blit(sky_surface,(0,0))
    Screen.blit(ground_surface,(0,300))
    Screen.blit(text_surface , (300 ,50))
    Screen.blit(snail_surface, snail_rect)
    Screen.blit(player_surf, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    mouse = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse)):
        print('collide')
    

    pygame.display.update() #updates the 'screen' above 
    clock.tick(60) #max frame rate

