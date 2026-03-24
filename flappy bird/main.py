import pygame
from pygame.locals import  *
import sys
import random

FPS=40
SCREENWIDTH=360
SCREENHEIGHT=640
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY=SCREENHEIGHT*0.8
gameSounds={}
gameImages={}
img="images/flappybird.png"
BG="images/background.png"
PIPE="images/pipe.png"
clock=pygame.time.Clock()

def homeScreen():
    playerx=SCREENWIDTH//5
    playery=(SCREENHEIGHT-gameImages['player'].get_height())//2
    startx=(SCREENWIDTH-gameImages['start'].get_width())//2
    starty=int(SCREENHEIGHT*0.13)
    basex=-50
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and (event.key==K_ESCAPE or event.key==K_BACKSPACE)):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return
            else:
                SCREEN.blit(gameImages['bg'],(0,0))
                SCREEN.blit(gameImages['player'],(playerx,playery))
                SCREEN.blit(gameImages['start'],(startx,starty))
                SCREEN.blit(gameImages['base'],(basex,GROUNDY))
                pygame.display.update()
                clock.tick(FPS)


def mainGame():
    score=0
    basex=0
    playerx=SCREENWIDTH//5
    playery=SCREENHEIGHT//2

    newPipe1=getRandomPipe()
    newPipe2=getRandomPipe()
     
    upperPipes=[
         {"x": SCREENWIDTH+200,"y":newPipe1[0]['y']},
         {"x": SCREENWIDTH+200+ SCREENWIDTH//2,"y":newPipe2[0]['y']}
     ]
    lowerPipes=[
        {"x":SCREENWIDTH+200,"y":newPipe1[1]['y']},
        {"x": SCREENWIDTH+200+ SCREENWIDTH//2,"y":newPipe2[1]['y']}
    ]

    pipeVelX=-4

    playerVelY=-9
    playerMaxVelY= 10
    playerMinVel=-8
    playerAccY=1

    playerFlapVel=-8  #velocity while flapping
    playerFlapped=False #it is true only when the bird is flapping 
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and (event.key==K_UP or event.key==K_SPACE):
                if playery>0:
                    playerVelY=playerFlapVel
                    playerFlapped=True
                    gameSounds['wing'].play()

            crashTest=isCollide(playerx,playery,upperPipes,lowerPipes)
            if crashTest:
                return
            
            #check for score
            playerMidPos=playerx+gameImages['player'].get_width()//2
            for pipe in upperPipes:
                pipeMidPos=pipe['x']+(gameImages['pipe'][0].get_width()//2)
            if pipeMidPos<=playerMidPos<pipeMidPos+4:
                score+=1
                print("your score is : ",score)
                gameSounds['point'].play()

            if playerVelY<playerMaxVelY and not playerFlapped:
                playerVelY+=playerAccY
            if playerFlapped:
                playerFlapped=False
            playerHeight=gameImages['player'].get_height()
            playery+=min(playerVelY,GROUNDY-playery-playerHeight)

            #pipe movement to the left 
            for u,l in zip(upperPipes,lowerPipes):
                u['x']+=pipeVelX
                l['x']+=pipeVelX
            
            if 0<upperPipes[0]['x']<5:
                newPipe=getRandomPipe()
                upperPipes.append(newPipe[0])
                lowerPipes.append(newPipe[1])
            
            if upperPipes[0]['x']<-gameImages['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)

            #bliting part
            SCREEN.blit(gameImages['bg'],(0,0))
            for u,l in zip(upperPipes,lowerPipes):
                SCREEN.blit(gameImages['pipe'][0],(u['x'],u['y']))
                SCREEN.blit(gameImages['pipe'][1],(l['x'],l['y']))
            SCREEN.blit(gameImages['base'],(basex,GROUNDY))
            SCREEN.blit(gameImages['player'],(playerx,playery))
            myDigits=[int(i) for i in list(str(score))]
            width=0
            for digit in myDigits:
                width+=gameImages['numbers'][digit].get_width()
            Xoffset=(SCREENWIDTH-width)//2
            
            for digit in myDigits:
                SCREEN.blit(gameImages['numbers'][digit],(Xoffset,SCREENHEIGHT*0.14))
                Xoffset+=gameImages['numbers'][digit].get_width()
            pygame.display.update()
            clock.tick(FPS)


def isCollide(playerx,playery,upperPipes,lowerPipes):
    if playery>GROUNDY or playery<0:
        return True
    return False
    
    

            


    


def getRandomPipe():
    pipeHeight=gameImages['pipe'][0].get_height()
    pipeX=SCREENWIDTH+10
    offset=SCREENHEIGHT//3
    y2=offset+ random.randint(0, SCREENHEIGHT-gameImages['base'].get_height()-int(offset*1.3))
    y1=pipeHeight-y2+offset
    pipe=[{"x": pipeX,"y":-y1}, #for upper pipe
          {"x":pipeX,"y":y2}] #for lower pipe
    return pipe



if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption('Flappy Bird by Sk8')
    gameImages['numbers']=(
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha(),
    )
    gameImages['base']=pygame.image.load('images/base.png').convert_alpha()
    gameImages['start']=pygame.image.load('images/start.png').convert_alpha()
    gameImages['end']=pygame.image.load('images/game_over.png').convert_alpha()
    gameImages['pipe']=(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
        pygame.image.load(PIPE).convert_alpha()
    )
    gameImages['bg']=pygame.image.load(BG).convert()
    gameImages['player']=pygame.transform.scale(pygame.image.load(img).convert_alpha(),(50,50))



    gameSounds['die']=pygame.mixer.Sound('sounds/die.wav')
    gameSounds['hit']=pygame.mixer.Sound('sounds/hit.wav')
    gameSounds['point']=pygame.mixer.Sound('sounds/point.wav')
    gameSounds['swooshing']=pygame.mixer.Sound('sounds/swooshing.wav')
    gameSounds['wing']=pygame.mixer.Sound('sounds/wing.wav')
    while True:
        homeScreen()
        mainGame()