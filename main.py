import pygame
from pygame.locals import *


pygame.init()

screen_width=600
screen_height=600
line_width = 4
markers = []
clicked = False
pos = []
player = 1
pink = (255,105,180)
lavender = 	(128,0,128)
purple = (188,0,255)
red = (255,0,0)
screen = pygame.display.set_mode((screen_width,screen_height))
winner = 0
game_over = False
font = pygame.font.SysFont(None, 60)
fonts = pygame.font.SysFont(None, 30)

# create play again rectangle
again_rect = Rect(screen_width//3+ 3 , screen_height //2 + 30, 240, 60)

pygame.display.set_caption("TikTacToe")

def draw_grid():
    bg=	(255,247,0)
    grid=(50,50,50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0,x*200), (screen_width,x*200), line_width)  #for horizontal lines
        pygame.draw.line(screen, grid, (x*200, 0), (x*200, screen_height), line_width) #for vertical lines

for x in range(3):
    rows = [0]*3
    markers.append(rows)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,pink,(x_pos * 200 + 60, y_pos * 200 + 60),(x_pos * 200 + 120 ,y_pos * 200 + 120), line_width)
                pygame.draw.line(screen,pink,(x_pos * 200 + 60, y_pos * 200 + 120),(x_pos * 200 + 120 ,y_pos * 200 + 60), line_width)
            if y == -1:
                pygame.draw.circle(screen, lavender, (x_pos * 200 + 100, y_pos * 200 + 100), 50, line_width)
            y_pos +=1
        x_pos +=1

def run_winner():

    global winner
    global game_over
    y_pos = 0

    for x in markers:
        if sum(x) == 3:    # for columms
            winner = 1
            game_over = True

        if sum(x) == -3:    # for rows
            winner = 2
            game_over = True

            #check  rows

        if markers[0][y_pos]  + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True

        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True

        y_pos += 1

    # check crosss

    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True

    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True

def display_winner(winner, white=(255,255,255), black=(0,0,0)):
    win_Text = "Player " +  str(winner) + " wins!"
    win_img = font.render(win_Text,True,white)
    pygame.draw.rect(screen,red,(screen_width // 10 , screen_height // 6, 500 ,400))
    screen.blit(win_img,(screen_width//2 - 100, screen_height //2 - 40))

    again_text = "Play Again ?"
    again_img = fonts.render(again_text, True, white)
    pygame.draw.rect(screen, black, again_rect)
    screen.blit(again_img,(screen_width//2-30 , screen_height //2 + 50))


run = True
while run:

    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_over == 0:

            if event.type == pygame.MOUSEBUTTONDOWN and clicked == True:
                    clicked = False
            if event.type == pygame.MOUSEBUTTONUP and clicked == False:
                clicked = True
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]

                if markers[cell_x//200][cell_y//200] == 0: #dividing by 200 because 600/200 =3 and our rangge is also 0,1,2 which is euqal to index range(3)
                   markers[cell_x // 200][cell_y // 200] = player
                   player *= -1
                   run_winner()


    if game_over ==  True:
        display_winner(winner)

        #check for mouseclick if user has clicked the play again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):

                #reset variables
                markers =[]
                pos = []
                player =1
                winner =0
                game_over = False
                for x in range(3):
                     rows = [0] * 3
                     markers.append(rows)

    pygame.display.update()
pygame.quit()
