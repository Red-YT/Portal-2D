#Import modules
from xmlrpc.client import ProtocolError
import pygame
from sys import exit
import random

#Pygame
pygame.init()

#Window settings
SCREEN = pygame.display.set_mode((800,600))
CLOCK = pygame.time.Clock()
TITLE = pygame.display.set_caption('Portal 2D Physic Test By Red')
ICON = random.randint(1,2)
if ICON == 1:
    ICON_SURF = pygame.image.load('./resources/portal1.png').convert_alpha()
else:
    ICON_SURF = pygame.image.load('./resources/portal2.png').convert_alpha()
ICON = pygame.display.set_icon(ICON_SURF)

#Portals
#Portal 1
PORTAL1_SURF = pygame.image.load('./resources/portal1.png').convert_alpha()
PORTAL1_SURF_SCALED = pygame.transform.rotozoom(PORTAL1_SURF, 270, 0.2)
PORTAL1_RECT = PORTAL1_SURF_SCALED.get_rect(center = (600,520))
#Portal 2
PORTAL2_SURF = pygame.image.load('./resources/portal2.png').convert_alpha()
PORTAL2_SURF_SCALED = pygame.transform.rotozoom(PORTAL2_SURF, 90, 0.2)
PORTAL2_RECT = PORTAL2_SURF_SCALED.get_rect(center = (200,45))

#Surfaces
BACKGROUND_SURF = pygame.image.load('./resources/background.jpg').convert()
GROUND_SURF = pygame.image.load('./resources/ground.png').convert()
GROUND_SURF_FLIPPED = pygame.transform.rotozoom(GROUND_SURF, 180, 1)

#Player
PLAYER_SURF = pygame.image.load('./resources/character.png').convert_alpha()
PLAYER_SURF_SCALED = pygame.transform.rotozoom(PLAYER_SURF, 0, 0.2)
PLAYER_RECT = PLAYER_SURF_SCALED.get_rect(midbottom = (400,500))
PLAYER_SURF_SCALED_FLIPPED = pygame.transform.flip(PLAYER_SURF_SCALED, True, False)
PLAYER_GRAVITY = 0
PLAYER_MOVE = False
PLAYER_MOVE_BACKWARDS = False
FLIP = False
FLOOR = True

while True:
    #Keybinds
        #ESC
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        #Quit button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Up arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and PLAYER_RECT.bottom >= 530:
                PLAYER_GRAVITY = -17
        #Right arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                FLIP = False
                PLAYER_MOVE = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                PLAYER_MOVE = False
        #Left arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                FLIP = True
                PLAYER_MOVE_BACKWARDS = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                PLAYER_MOVE_BACKWARDS = False

    #Portals
    if PLAYER_RECT.colliderect(PORTAL1_RECT):
        PLAYER_RECT.x = (PORTAL1_RECT.x + 30)
        PLAYER_RECT.y - 100
        FLOOR = False
        PLAYER_GRAVITY = 2
    if PLAYER_RECT.y >= 470:
        PLAYER_RECT.x = PORTAL2_RECT.x
        PLAYER_GRAVITY = 4
        PLAYER_RECT.y = (PORTAL2_RECT.y - 30)
        if PLAYER_RECT.colliderect(PORTAL2_RECT):
            FLOOR = True
    
    #Player
    if PLAYER_MOVE == True: PLAYER_RECT.x += 3
    if PLAYER_MOVE_BACKWARDS == True: PLAYER_RECT.x -= 3

    #Render
    SCREEN.fill((255,255,255))
    SCREEN.blit(BACKGROUND_SURF,(0,0))
    SCREEN.blit(GROUND_SURF,(0,500))
    if FLIP == False:
        SCREEN.blit(PLAYER_SURF_SCALED,PLAYER_RECT)
    else:
        SCREEN.blit(PLAYER_SURF_SCALED_FLIPPED,PLAYER_RECT)
    SCREEN.blit(GROUND_SURF_FLIPPED,(0,-130))
    SCREEN.blit(PORTAL1_SURF_SCALED,PORTAL1_RECT)
    SCREEN.blit(PORTAL2_SURF_SCALED,PORTAL2_RECT)
    
    #Limits
    if PLAYER_RECT.right >= 1050: PLAYER_RECT.right = 1050
    if PLAYER_RECT.left <= -5: PLAYER_RECT.left = -5
    
    #Gravity
    PLAYER_GRAVITY += 1
    PLAYER_RECT.y += PLAYER_GRAVITY
    if FLOOR == True:
        if PLAYER_RECT.bottom >= 530: PLAYER_RECT.bottom = 530
    
    #Updates
    pygame.display.update()
    CLOCK.tick(60)