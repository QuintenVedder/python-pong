import pygame as pg
import random
import time

pg.init()
clock = pg.time.Clock()
windowwidth = 1000
windowheight = 500
window = pg.display.set_mode((windowwidth, windowheight))


black = (0,0,0)
white = (255,255,255)
font = pg.font.SysFont('Corbel',35)
pointfont = pg.font.SysFont('Corbel',50)
#button variables
buttonwidth = 150
buttonheight = 50
buttonquitposX = (windowwidth - buttonwidth)/2
buttonquitposY = ((windowheight + 200) - buttonheight)/2

button1v1posX = (windowwidth - buttonwidth)/2
button1v1posY = ((windowheight - 100) - buttonheight)/2

buttonplayervsAIposX = (windowwidth - buttonwidth)/2 - 10
buttonplayervsAIposY = ((windowheight + 50) - buttonheight)/2

#player(s) variables
playerwidth = 10
playerheight = 75
playerposX = (windowwidth - windowwidth) + 200
playerposY = (windowheight/2) - playerheight

player2width = 10
player2height = 75
player2posX = windowwidth - 200
player2posY = (windowheight/2) - player2height

speed = 4

touch = True

#ball variables
ballwidth = 20
ballheight = 20
ballposX = (windowwidth/2) - ballwidth
ballposY = (windowheight/2) - ballheight

ballstartposX = round((windowwidth/2) - ballwidth)
ballstartposY = round((windowheight/2) - ballheight)

ballspeedX = 3
ballspeedY = 2
extraspeed = 0
ballcolorcount = 0
ballcolor = (255, 255, 255)

p1wintext = font.render("player1 won!" , True , white)
p2wintext = font.render("player2 won!" , True , white)
aiwintext = font.render("AI won!" , True , white)

win = False

ballcolor = (255,255,255)

timer = True

runplayervsAI = False
run1v1 = False
mainmenu = True
while mainmenu:
    clock.tick(60)
    window.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if buttonquitposX <= mouse[0] <= buttonquitposX+buttonwidth and buttonquitposY <= mouse[1] <= buttonquitposY+buttonheight:
                pg.quit()

            if button1v1posX <= mouse[0] <= button1v1posX+buttonwidth and button1v1posY <= mouse[1] <= button1v1posY+buttonheight:
                run1v1 = True
                mainmenu = False

            if buttonplayervsAIposX <= mouse[0] <= buttonplayervsAIposX+buttonwidth and buttonplayervsAIposY <= mouse[1] <= buttonplayervsAIposY+buttonheight:               
                runplayervsAI = True
                mainmenu = False



    mouse = pg.mouse.get_pos()

    if buttonquitposX <= mouse[0] <= buttonquitposX+buttonwidth and buttonquitposY <= mouse[1] <= buttonquitposY+buttonheight:
        pg.draw.rect(window,white,[buttonquitposX,buttonquitposY,buttonwidth,buttonheight])
        textquit = font.render('quit' , True , black)

    else:
        pg.draw.rect(window,black,[buttonquitposX,buttonquitposY,buttonwidth,buttonheight])
        textquit = font.render('quit' , True , white)
    
    if button1v1posX <= mouse[0] <= button1v1posX+buttonwidth and button1v1posY <= mouse[1] <= button1v1posY+buttonheight:
        pg.draw.rect(window,white,[button1v1posX,button1v1posY,buttonwidth,buttonheight])
        text1v1 = font.render('1v1' , True , black)

    else:
        pg.draw.rect(window,black,[button1v1posX,button1v1posY,buttonwidth,buttonheight])
        text1v1 = font.render('1v1' , True , white)
    
    if buttonplayervsAIposX <= mouse[0] <= buttonplayervsAIposX+buttonwidth and buttonplayervsAIposY <= mouse[1] <= buttonplayervsAIposY+buttonheight:
        pg.draw.rect(window,white,[buttonplayervsAIposX,buttonplayervsAIposY,buttonwidth + 20,buttonheight])
        textAI = font.render('player vs AI' , True , black)

    else:
        pg.draw.rect(window,black,[buttonplayervsAIposX,buttonplayervsAIposY,buttonwidth + 20,buttonheight])
        textAI = font.render('player vs AI' , True , white)

    window.blit(textquit , (buttonquitposX+50,buttonquitposY))
    window.blit(text1v1 , (button1v1posX+50,button1v1posY))
    window.blit(textAI , (buttonplayervsAIposX+5,buttonplayervsAIposY))


    if event.type == pg.QUIT:
        mainmenu = False

    #end event handling
    pg.display.flip()

while run1v1:

    pixelcolor = window.get_at((ballstartposX, ballstartposY))
    win = False
    clock.tick(60)
    window.fill((black))
    keys = pg.key.get_pressed()
    playerposY += (keys[pg.K_s] - keys[pg.K_w]) * speed
    player2posY += (keys[pg.K_DOWN] - keys[pg.K_UP]) * speed
    
    if(playerposY + playerheight >= windowheight):
        playerposY = windowheight - playerheight
    if(playerposY <= 0):
        playerposY = 0

    if(player2posY + player2height >= windowheight):
        player2posY = windowheight - player2height
    if(player2posY <= 0):
        player2posY = 0

    match ballcolorcount:
        case 0:
            ballcolor = (231, 179, 56)
        case 1:
            ballcolor = (226, 205, 109)
        case 3:
            ballcolor = (131, 183, 153)
        case 4:
            ballcolor = (194, 178, 143)
        case 5:
            ballcolor = (228, 216, 180)
        case 6:
            ballcolor = (232, 111, 104)
        case 7:
            ballcolor = (66, 11, 29)

    ballposY += ballspeedY
    ballposX += ballspeedX
    #ball x wall collision
    if(ballposY >= windowheight - ballheight):
        ballspeedY = -2
        ballcolorcount = random.randint(0, 7)
    if(ballposY <= 0):
        ballspeedY = 2
        ballcolorcount = random.randint(0, 7)

    #player x ball collision
    if(ballposX == playerposX + playerwidth and ballposY >= playerposY and ballposY <= playerposY + playerheight):
        ballspeedX = 3
        ballcolorcount = random.randint(0, 7)
        touch = True
    if(ballposX == player2posX - ballwidth and ballposY >= player2posY and ballposY <= player2posY + player2height):
        ballspeedX = -3
        ballcolorcount = random.randint(0, 7)
        touch = False

    if(ballposX >= windowwidth - ballwidth):
        win = True
        ballspeedX = 0
        ballspeedY = 0
        ballcolor = black
    if(ballposX <= 0):
        win = True
        ballspeedX = 0
        ballspeedY = 0
        ballcolor = black

    if(win == True):
        if(touch == True):
            window.blit(p1wintext , (buttonplayervsAIposX+5,buttonplayervsAIposY))
        if(touch == False):
            window.blit(p2wintext , (buttonplayervsAIposX+5,buttonplayervsAIposY))

    for event in pg.event.get(): 


        if event.type == pg.QUIT:
            run1v1 = False
    

    pg.draw.rect(window,white,[playerposX,playerposY,playerwidth,playerheight])
    pg.draw.rect(window,white,[player2posX,player2posY,player2width,player2height])
    pg.draw.rect(window,ballcolor,[ballposX,ballposY,ballwidth,ballheight])
    if(timer == True and pixelcolor != white):
        time.sleep(2)
        timer = False
    #end event handling
    pg.display.flip()
pointcounter = 0
while runplayervsAI:
    pointtext = pointfont.render(str(pointcounter) , True , white)
    pixelcolor = window.get_at((ballstartposX, ballstartposY))
    win = False
    clock.tick(60)
    window.fill((black))
    keys = pg.key.get_pressed()
    playerposY += (keys[pg.K_s] - keys[pg.K_w]) * speed
    
    if(playerposY + playerheight >= windowheight):
        playerposY = windowheight - playerheight
    if(playerposY <= 0):
        playerposY = 0
    
    if(player2posY + player2height >= windowheight):
        player2posY = windowheight - player2height
    if(player2posY <= 0):
        player2posY = 0

    match ballcolorcount:
        case 0:
            ballcolor = (231, 179, 56)
        case 1:
            ballcolor = (226, 205, 109)
        case 3:
            ballcolor = (131, 183, 153)
        case 4:
            ballcolor = (194, 178, 143)
        case 5:
            ballcolor = (228, 216, 180)
        case 6:
            ballcolor = (232, 111, 104)
        case 7:
            ballcolor = (66, 11, 29)

    ballposY += ballspeedY
    ballposX += ballspeedX
    #ball x roof collision
    if(ballposY >= windowheight - ballheight):
        ballspeedY = -2
        ballcolorcount = random.randint(0, 7)
    if(ballposY <= 0):
        ballspeedY = 2
        ballcolorcount = random.randint(0, 7)

    #player x ball collision
    if(ballposX == playerposX + playerwidth and ballposY >= playerposY and ballposY <= playerposY + playerheight):
        ballspeedX = 3
        ballcolorcount = random.randint(0, 7)
        touch = True
        pointcounter += 1
    if(ballposX + ballwidth == player2posX):
        ballspeedX = -3
        ballcolorcount = random.randint(0, 7)
        touch = False

    if(ballposX >= windowwidth - ballwidth):
        win = True
        ballspeedX = 0
        ballspeedY = 0
        ballcolor = black
    if(ballposX <= 0):
        win = True
        ballspeedX = 0
        ballspeedY = 0
        ballcolor = black

    if(win == True):
        if(touch == True):
            window.blit(p1wintext , (buttonplayervsAIposX+5,buttonplayervsAIposY))
        if(touch == False):
            window.blit(aiwintext , (buttonplayervsAIposX+5,buttonplayervsAIposY))

    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            runplayervsAI = False
    

    pg.draw.rect(window,white,[playerposX,playerposY,playerwidth,playerheight])
    pg.draw.rect(window,white,[player2posX,ballposY - (player2height/2),player2width,player2height])
    pg.draw.rect(window,ballcolor,[ballposX,ballposY,ballwidth,ballheight])
    window.blit(pointtext , ((windowwidth/2) - 25,25))
    if(timer == True and pixelcolor != white):
        time.sleep(2)
        timer = False
    #end event handling
    pg.display.flip()
    #end main loop
pg.quit()