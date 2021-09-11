import pygame 
from sys import exit

from pygame.time import Clock

def display_score():
    current_time=int(pygame.time.get_ticks()/1000) - satrt_time 
    score_surf = test_font.render(f'Score {current_time}', False, ((64),(64),(64)))
    score_rect = score_surf.get_rect(center = (400,50))
    Screen.blit(score_surf, score_rect)

pygame.init()




Screen = pygame.display.set_mode((800, 400))#width , height
pygame.display.set_caption("first game")
clock = pygame.time.Clock()
test_font  = pygame.font.Font('font/Pixeltype.ttf' , 50)#(font type , font size)
game_active = True
satrt_time = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface=pygame.image.load('graphics/ground.png').convert_alpha()
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600 , 300))
player_surf = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80 , 300))
player_gravity = 0

# score_surf= test_font.render('My game', False , (64 , 64 , 64))#text , AA ,color
# score_rect = score_surf.get_rect( center = (400 , 50))

#surface= pygame.Surface((100,200)) #W,H (display surface and regular surface have alot of things in commen)
#surface.fill('Red')


while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active =True
                snail_rect.left = 600
                satrt_time = int(pygame.time.get_ticks()/1000)

        



    
    if game_active:
        Screen.blit(sky_surface,(0,0))
        Screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(Screen , '#c0e8ec' , score_rect )
        # pygame.draw.rect(Screen , '#c0e8ec' , score_rect, 10 )
        # Screen.blit(score_surf , score_rect)

        display_score()

        snail_rect.left -= 4
        if snail_rect.right <= 0 : snail_rect.left = 800

        #snail
        Screen.blit(snail_surface, snail_rect)

        #player
        player_gravity +=1
        player_rect.bottom +=   player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        Screen.blit(player_surf, player_rect )

        #collisions 
        if snail_rect.colliderect(player_rect):
            game_active = False
    else: Screen.fill('Yellow')
        
        
    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse)):
    #     print('collide')

    
    

    pygame.display.update() #updates the 'screen' above 
    clock.tick(60) #max frame rate

#rectangles are used for positioning, collision and drawing   