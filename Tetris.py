#Nikky Nandipati
#5/4/2022
#GameDesignCBlock

#Credits/References:
#Ms. Suarez: 
#TechWithTim: https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/ (video series)
#KidsCanCode: https://www.youtube.com/watch?v=MFv1Ew_nGG0&ab_channel=KidsCanCode
#StackOverflow: https://stackoverflow.com/questions/70990741/falling-objects-game-in-pygame

import pygame as pg
import os, random, time, math, datetime
from turtle import screensize
os.system('cls')
name=input("Enter name: ")
#initialize pg
pg.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
s_width=800
s_height=800
play_width=300
play_height=600
block_size=30

top_left_x= (s_width - play_width) // 2
top_left_y= s_height - play_height

xMs=50
yMs=250
wb=30
hb=30

MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False

#List f messages
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size']
sizeList=['1000 x 1000','950 x 950','900 x 900']
check=True #for the while loop
score=0

#create screen
screen=pg.display.set_mode((s_width,s_height))
pg.display.set_caption('ShapeStack')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'blue':[175,166, 247],'pink':[200,3,75], 'electric':[2,27,245],}
#Get colors
background= (175,166,247)
randColor=''
sqM_color=(2,27,245)
BLACK=(0,0,0)
#create fifferent type 
TITLE_FNT=pg.font.SysFont('aharoni', 100)
MENU_FNT=pg.font.SysFont('aharoni', 60)
INST_FNT=pg.font.SysFont('aharoni', 50)
#Create square fr menu

squareM=pg.Rect(xMs,yMs,wb,hb)
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (2, 27, 245))
    screen.fill((background))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=s_width/2-text.get_width()/2
    screen.blit(text,(xt,50))
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(255,255,255))
        screen.blit(text,(90,txty))
        pg.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pg.display.update()
    pg.time.delay(10)

def instr(): 
     
    txt=INST_FNT.render("Stack up as many shapes as you can before", 1,(5, 31, 64))
    xt= s_width/2-txt.get_width()/2
    screen.blit(txt,(xt,200))
    txt=INST_FNT.render("you reach the top of the line. Try to arrange", 1, (5, 31, 64)) 
    screen.blit(txt,(xt,240))
    txt=INST_FNT.render("the shapes in the best possible way, using the",1, (5, 31, 64))
    screen.blit(txt, (xt,280))
    txt=INST_FNT.render("arrow keys to move/rotate them into position",1, (5, 31, 64))
    screen.blit(txt, (xt,320)) 
    txt=INST_FNT.render("The shapes will start to fall faster in each level,",1, (5, 31, 64))
    screen.blit(txt, (xt,360)) 
    txt=INST_FNT.render("and if you clear a line, you will get 5 points,",1, (5, 31, 64))
    screen.blit(txt, (xt,360)) 

#function creating string for the score and then writing in file
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"/t"+name+"/t"+date.strftime('%m/%d/%Y'+'/n')
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('C:/Users/nandipatin24/Documents/nikky_game_design/ShapeStack/scoreboard.txt','a') 
    myFile.write(scoreLine)
    myFile.close()

#function for reading scoreboard lines
def scoreBoard():
    myFile=open('C:/Users/nandipatin24/Documents/nikky_game_design/ShapeStack/scoreboard.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=0
    for i in range(N, -1, -1):
        print(i,stuff[i])

#function to display scoreboard lines from file onto pygame screen
def displayScoreboard():
    height = 170
    myScoreboard=open('C:/Users/nandipatin24/Documents/nikky_game_design/Final Project/scoreboard.txt','r') #opens the file
    for line in myScoreboard.readlines():   #Reads the file and prints each letter on the screen
        text = INST_FNT.render(line,1,(175,166,247))
        gameScreen.blit(text, (s_width/2-text.get_width()/2,height))
        pg.display.update()
        pg.time.delay(100)
        height+=60
    myScoreboard.close()

#function for establishing screen size for game
def screenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        HEIGHT=1000
        WIDTH=1000

    if ((xm >20 and xm <80) and (ym >300 and ym <330)):
        HEIGHT=950
        WIDTH=950
        
    if ((xm >20 and xm <80) and (ym >350 and ym <380)):
        HEIGHT=900
        WIDTH=900
    screen=pg.display.set_mode((WIDTH,HEIGHT))

gameScreen = pg.display.set_mode((s_width, s_height))
pg.image.load("C:/Users/nandipatin24/OneDrive - Greenhill School/Game Design 10/Picture1.png")

#establishing the shapes
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

#index for the shapes
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 255), (0, 255, 255),
                (255, 255, 0), (255, 165, 0), (0, 0, 255),
                (128, 0, 128)]

#organizing each shape into classes
class shape(object):
    rows = 20
    columns = 10

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

#generates the grid for the in game screen
def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

# ensures that all the shapes are working properly (valid)
def proper_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True

#ensures that all pieces are within the board and not out of limits
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

#randomly selects a shape, calling back from index
def get_shape():
    global shapes, shape_colors

    return shape(5, 0, random.choice(shapes))

# creates the necessary text
def draw_text_middle(text, size, color, surface):
    font = pg.font.SysFont('aharoni', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (
        top_left_x + play_width / 2 - (label.get_width() / 2), top_left_y + play_height / 2 - label.get_height() / 2))

# establishes the grid lines for the game screen
def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pg.draw.line(surface, (128, 128, 128), (sx, sy + i * 30),
                         (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pg.draw.line(surface, (128, 128, 128), (sx + j * 30, sy),
                             (sx + j * 30, sy + play_height))  # vertical lines

# allows a row to clear when full
def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

# shows the next shape when playing before it drops
def draw_upcoming_shape(shape, surface):
    font = pg.font.SysFont('aharoni', 30)
    label = font.render('Next Shape', 1, (255, 255, 255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pg.draw.rect(surface, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)
    surface.blit(label, (sx + 10, sy - 30))

titlePic=pg.image.load("C:/Users/nandipatin24/OneDrive - Greenhill School/Game Design 10/Picture1.png")
titlePic=pg.transform.scale(titlePic,(550,200))

# loads the title game logo for the game screen
def draw_window(surface):
    surface.fill((0, 0, 0))
    pg.image.load("C:/Users/nandipatin24/OneDrive - Greenhill School/Game Design 10/Picture1.png")

    

    surface.blit(titlePic, (top_left_x + play_width / 2 - (titlePic.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pg.draw.rect(surface, grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)

    draw_grid(surface, 20, 10)

#loop for the game   
def playGame():
    global grid

    locked_positions = {}
    grid = create_grid(locked_positions)

    change_shape = False
    run = True
    current_shape = get_shape()
    next_shape = get_shape()
    clock = pg.time.Clock()
    fall_time = 0

    while run:
        

        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= gravity:
            fall_time = 0
            current_shape.y += 1
            if not (proper_space(current_shape, grid)) and current_shape.y > 0:
                current_shape.y -= 1
                change_shape = True

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    current_shape.x -= 1
                    if not proper_space(current_shape, grid):
                        current_shape.x += 1

                elif event.key == pg.K_RIGHT:
                    current_shape.x += 1
                    if not proper_space(current_shape, grid):
                        current_shape.x -= 1
                elif event.key == pg.K_UP:
                    current_shape.rotation = current_shape.rotation + 1 % len(current_shape.shape)
                    if not proper_space(current_shape, grid):
                        current_shape.rotation = current_shape.rotation - 1 % len(current_shape.shape)

                if event.key == pg.K_DOWN:
                    current_shape.y += 1
                    if not proper_space(current_shape, grid):
                        current_shape.y -= 1

                if event.key == pg.K_SPACE:
                    while proper_space(current_shape, grid):
                        current_shape.y += 1
                    current_shape.y -= 1
                    print(convert_shape_format(current_shape))

        shape_pos = convert_shape_format(current_shape)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_shape.color

        if change_shape:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_shape.color
            current_shape = next_shape
            next_shape = get_shape()
            change_shape = False
            clear_rows(grid, locked_positions)

        draw_window(gameScreen)
        draw_upcoming_shape(next_shape, gameScreen)
        pg.display.update()

        if check_lost(locked_positions):
            run = False
        
        if clear_rows(grid, locked_positions):
                score += 5
                keepScore()

    draw_text_middle("Get it together. You suck.", 40, (255, 255, 255), gameScreen)

    pg.display.update()
    pg.time.delay(2000)

#==============================================
#
#Beginning  main prram
keys=pg.key.get_pressed()
mouse_pos=(0,0)
screCk=True
first=True
xm=0 
ym=0
f_SEET=True
sc_size=False
set_first=True
c_first=True
while check:
    for case in pg.event.get():
        if case.type==pg.QUIT:
            check=False
        if case.type ==pg.MOUSEBUTTONDOWN:
            mouse_pos=pg.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=pg.key.get_pressed() #this returns a list
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first=False
    if INST:
        if keys[pg.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True
    if SETT and f_SEET:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        f_SEET=False
    if SETT:
        if keys[pg.K_ESCAPE]:
            SETT=False
            MAIN=True
            f_SEET=True
    if LEV_I:
        gravity = 0.27
        playGame()
        if keys[pg.K_ESCAPE]:
            LEV_I=False
            MAIN=True
            xm=0
            ym=0
    if LEV_II:
        gravity = 0.17
        playGame()
        if keys[pg.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        gravity = 0.1
        playGame()
        if keys[pg.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCORE and screCk:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        displayScoreboard()
        #call funct t print scres
        screCk=False
    if SCORE:
        if keys[pg.K_ESCAPE]:
            SCORE=False
            MAIN=True
            screCk=True
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and MAIN:
        MAIN=False
        INST=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and MAIN:
        MAIN=False
        SETT=True  
    if ((xm >20 and xm <80) and (ym >350 and ym <380))and MAIN :
        MAIN=False
        LEV_I=True   
    if ((xm >20 and xm <80) and (ym >400 and ym <430))and MAIN :
        MAIN=False
        LEV_II=True   
    if ((xm >20 and xm <80) and (ym >450 and ym <480))and MAIN:
        MAIN=False
        LEV_III=True   
    if ((xm >20 and xm <80) and (ym >500 and ym <530))and MAIN:
        MAIN=False
        SCORE=True 
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and SETT and set_first:  
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        sc_size=True
        set_first=False
        f_SEET=True
        if keys[pg.K_ESCAPE]:
            sc_size=False
            set_first=True
    if sc_size and xm >0:
        screenSize(xm,ym)
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        if keys[pg.K_ESCAPE]:
            sc_size=False
            set_first=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and SETT and c_first:
        screen.fill(background)
        TitleMenu("Background Color")
        c_first=False
        if keys[pg.K_ESCAPE]:
            c_first=True
            set_first=True
    if ((xm >20 and xm <80) and (ym >550 and ym <580)) :
        screen.fill(background)
        keepScore(121)
        text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
        screen.blit(text, (40,200))
        text=INST_FNT.render("before you exit", 1, BLACK)
        screen.blit(text, (40,300))
        text=INST_FNT.render("Thank you for playing", 1, BLACK)
        screen.blit(text, (40,400))
        pg.display.update()
        pg.time.delay(50)
        MAIN=False
        SCORE=False 
        pg.time.delay(3000)
        check=False
    pg.display.update()
    pg.time.delay(10)

os.system('cls')
pg.quit()
