import pygame
import time

"""
hoi 
"""

clock=pygame.time.Clock()
background_image = pygame.image.load("battleship_045.jpg")
pygame.init()
game_width = 1280
game_height = 720
size = (game_width, game_height)
game_display = pygame.display.set_mode(size)

gridY = 20
gridX = 20
gridSize = 25
tileSize = 20

White = (255,255,255)
Black = (0,0,0)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)

def grid(g_height, g_width, s_height, s_width,gap):
    for y in range(g_height):
        for x in range(g_width):
            rect = pygame.Rect(x*(s_width+gap), y*(s_height+gap), s_height, s_width)
            pygame.draw.rect(game_display, White, rect)
            return grid
def Menu():
    game_intro()

def instructies():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display.blit(background_image, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        pygame.display.flip()
        clock.tick(60)

def highscores():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display.blit(background_image, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        pygame.display.flip()
        clock.tick(60)

def instellingen():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display.blit(background_image, [0,0])

    while not process_events():
        pygame.display.update()
        button("Menu",1120,10,150,60,White,Green,5,Menu)
        pygame.display.flip()
        clock.tick(60)

def quit_game():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, White)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,l,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_display, ac,(x,y,w,h),l)
        if click[0] == 1 and action != None:
            action()
    else:     
        pygame.draw.rect(game_display, ic,(x,y,w,h),l)

    smallText = pygame.font.SysFont("Bauhaus93",20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    game_display.blit(TextSurf, TextRect)

mouse = pygame.mouse.get_pos()

def game_intro(): 

    intro = False

    while not intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = True
                 
        game_display.blit(background_image, [0,0])
        largeText = pygame.font.SysFont('Bauhaus93',155)
        TextSurf, TextRect = text_objects("Battleport", largeText)
        TextRect.center = ((game_width/2),(game_height/2.5))
        game_display.blit(TextSurf, TextRect)
                                          
        largeText = pygame.font.SysFont('Bauhaus93',150)
        TextSurf, TextRect = text_objects1("Battleport", largeText)
        TextRect.center = ((game_width/2),(game_height/2.5))
        game_display.blit(TextSurf, TextRect)
        
        button("Start Spel",170,540,150,60,White,Green,5,program)
        button("Instellingen",770,540,150,60,White,Green,5,instellingen)
        button("Instructies",370,540,150,60,White,Green,5,instructies)
        button("Highscores",570,540,150,60,White,Green,5,highscores)
        button("Stop Spel",970,540,150,60,White,Green,5,quit_game)

        pygame.display.update()
        clock.tick(15)


def process_events():
    lead_x = 100
    lead_y = 100
    lead_x_change = 0
    lead_y_change = 0

    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True                 # Vanaf deze line is er een code met het nog niet werkende, bewegende vierkantje.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0

            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0 #stopt het vierkantje als je de knop omhoog doet.

        if lead_x >= 1280 or lead_x < 0 or lead_y >= 720 or lead_y < 0:
            return True

    lead_x += lead_x_change 
    lead_y += lead_y_change
    pygame.draw.rect(game_display, Red, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(30)                      # Hier stopt de code van het niet werkende, bewegende vierkantje.

    return False

'''
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((game_width/2), (game_height/2))
    game_display.blit (TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    program()
'''

def program():
    game_width = 1280
    game_height = 720
    size = (game_width, game_height)
    pygame.init()
    game_display = pygame.display.set_mode(size)
    while not process_events():
        pygame.display.update()
        for y in range(gridY):
            for x in range(gridX):
                rect = pygame.Rect(x * gridSize + game_width / 2 - gridX * gridSize / 2, y * gridSize + game_height / 2 - gridY * gridSize / 2, tileSize, tileSize)
                pygame.draw.rect(game_display, White, rect)
        button("Menu",1120,10,150,60,White,Green,5,Menu) 
    

    pygame.display.flip()
    clock.tick(60)

game_intro()        
program()