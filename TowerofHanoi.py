import pygame, os

#Tower of Hanoi

#initialize game
pygame.init()

#parameters/settings for window
screenW = 840
screenH = 500
moves = 0
count = 0
wn = pygame.display.set_mode((screenW, screenH))
bg = ((255, 255, 255))
pygame.display.set_caption("Tower of Hanoi Puzzle")
arrowimg = pygame.image.load(os.path.join('C:\\Game','arrow.png')).convert()

#experimentation
def deactB():
    diskB.active = False
    global move
    move = False

def deactM():
    diskM.active = False
    global move
    move = False

def deactT():
    diskT.active = False
    global move
    move = False

def win():
    win = font.render('haha u win congrats :)',1, (0,0,0))

    if ((diskB.y > diskM.y) and (diskM.y > diskT.y)) and ((diskT.x in range(560, 840)) and (diskM.x in range(560, 840)) and (diskB.x in range(560, 840))):
        wn.blit(win, (260, 175))


#OOP time to practice?
class tower(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, wn):
        pygame.draw.rect(wn, self.color, (self.x, self.y, self.width, self.height))

class disk(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.size = width * height
        self.active = False

    def draw(self, wn):
        pygame.draw.rect(wn, self.color, (self.x, self.y, self.width, self.height))

class arrow(object):
    #alright i'm not sure where I'm going with this but lets pray
    def __init__(self, x , y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, wn):
        wn.blit(arrowimg, (self.x, self.y))

#update(draw) objects in window
def wnDraw():
    wn.fill(bg)
    text = font.render('moves: ' + str(count), 1, (0, 0, 0))
    wn.blit(text, (690, 10))
    arrowS.draw(wn)
    towerA.draw(wn)
    towerB.draw(wn)
    towerC.draw(wn)
    diskB.draw(wn)
    diskM.draw(wn)
    diskT.draw(wn)
    #pygame.draw.line(wn, (0,0,0), (170,0), (170,500))
    #pygame.draw.line(wn, (0,0,0), (200,0), (200,500))
    #pygame.draw.line(wn, (0,0,0), (420,0), (420,500))
    #pygame.draw.line(wn, (0,0,0), (450,0), (450,500))
    #pygame.draw.line(wn, (0,0,0), (670,0), (670,500))
    #pygame.draw.line(wn, (0,0,0), (700,0), (700,500))
    #pygame.draw.line(wn, (0,0,0), (85, 0), (85, 500))
    pygame.draw.line(wn, (255,0,0), (310,240), (310, 500),3)
    pygame.draw.line(wn, (255,0,0), (560, 240), (560,500),3)
    win()


    pygame.display.update()
   
#create arrow for moving mechanic
arrowS = arrow(163, 30, 45, 72)

#create the towers
towerA = tower((screenW/4 - 40), 240, 30, 270, (0, 0, 0))
towerB = tower(((screenW/4)*2), 240, 30, 270, (0, 0, 0))
towerC = tower(((screenW/4)*3 + 40), 240, 30, 270, (0, 0, 0))

#create the disks, currently limited to 3 disks, hopefully will allow creation based on user input
diskB =  disk(65, 472, 240, 25, (255, 0, 0))
diskM = disk(85, 445, 200, 25, (0, 255, 0))
diskT = disk(110, 418, 150, 25, (0, 0, 255))

#loop to delay input (without it, one press will go as like 3)
inDelay = 0

#main loop
run = True
move = False
font = pygame.font.SysFont('comicsans', 45)
while run:
    print()
    print(inDelay, move)

    wnDraw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if inDelay > 0:
        inDelay += 1
        if inDelay > 60:
            inDelay = 0

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and inDelay == 0:
        
        if move == True:
            if diskB.active == True:
                if arrowS.x == 163:
                    arrowS.x = 413
                    diskB.x = 315
                elif arrowS.x == 413:
                    arrowS.x = 663
                    diskB.x = 565
                elif arrowS.x == 663:
                    arrowS.x = 163
                    diskB.x = 65

            if diskM.active == True:
                if arrowS.x == 163:
                    arrowS.x = 413
                    diskM.x = 335   
                elif arrowS.x == 413:
                    arrowS.x = 663
                    diskM.x = 585   
                elif arrowS.x == 663:
                    arrowS.x = 163
                    diskM.x = 85   

            if diskT.active == True:
                if arrowS.x == 163:
                    arrowS.x = 413
                    diskT.x = 360
                elif arrowS.x == 413:
                    arrowS.x = 663
                    diskT.x = 610
                elif arrowS.x == 663:
                    arrowS.x = 163
                    diskT.x = 110           
        else:
            if arrowS.x == 163:
                arrowS.x = 413
            elif arrowS.x == 413:
                arrowS.x = 663
            elif arrowS.x == 663:
                arrowS.x = 163
        inDelay = 1

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and inDelay == 0:

        if move == True:
            if diskB.active == True:
                if arrowS.x == 163:
                    arrowS.x = 663
                    diskB.x = 565
                elif arrowS.x == 413:
                    arrowS.x = 163
                    diskB.x = 65
                elif arrowS.x == 663:
                    arrowS.x = 413
                    diskB.x = 315

            if diskM.active == True:
                if arrowS.x == 163:
                    arrowS.x = 663
                    diskM.x = 585
                elif arrowS.x == 413:
                    arrowS.x = 163
                    diskM.x = 85
                elif arrowS.x == 663:
                    arrowS.x = 413
                    diskM.x = 335

            if diskT.active == True:
                if arrowS.x == 163:
                    arrowS.x = 663
                    diskT.x = 610
                elif arrowS.x == 413:
                    arrowS.x = 163
                    diskT.x = 110
                elif arrowS.x == 663:
                    arrowS.x = 413
                    diskT.x = 360
        else:
            if arrowS.x == 163:
                arrowS.x = 663
            elif arrowS.x == 413:
                arrowS.x = 163
            elif arrowS.x == 663:
                arrowS.x = 413
        inDelay = 1

    if keys[pygame.K_SPACE] and inDelay == 0:

        moves += 1
        if moves > 0:
            count = moves // 2

        if arrowS.x in range(diskT.x, diskT.x + 120):
            sel = diskT
        elif arrowS.x in range(diskM.x, diskM.x + 170):
            sel = diskM
        elif arrowS.x in range(diskB.x, diskB.x + 210):
            sel = diskB 

        #many many many if statements to check whether the disks can be placed
        if move == True:
            if diskT.active == True:
                if (diskB.x in range(diskT.x - 65, diskT.x + 150)) or (diskM.x in range(diskT.x - 65, diskT.x + 150)):
                    if (diskB.y == 472 and diskB.size > diskT.size) and diskM.y != 445:
                        diskT.y = 445
                        deactT()
                    elif (diskM.y == 445 and diskM.size > diskT.size):
                        diskT.y = 418
                        deactT()
                else:
                    diskT.y = 472
                    deactT()

                #diskT.active = False
                #move = False
            elif diskM.active == True:

                if (diskB.x in range(diskM.x - 25, diskM.x + 200)) or (diskT.x in range(diskM.x - 25, diskM.x + 200)):
                    if ((diskB.y == 472 and (diskB.size > diskM.size))):
                        if (diskT.x in range(diskM.x, diskM.x + 100)) and diskT.y != 472:
                            diskM.y = 445
                            deactM()
                        elif (diskB.x in range(diskM.x - 30, diskM.x + 150)):
                            diskM.y = 445
                            deactM()
                    elif ((diskT.y == 445 and diskT.size > diskM.size) or (diskB.y == 445 and diskB.size > diskM.size)):
                        diskM.y = 418
                        deactM()
                else:
                    diskM.y = 472
                    deactM()

                #diskM.active = False
                #move = False
            elif diskB.active == True:

                if (diskT.x in range(diskB.x, diskB.x + 240)) or (diskM.x in range(diskB.x, diskB.x + 240)):
                    if ((diskT.y == 472 and diskT.size > diskB.size) or (diskM.y == 472 and diskM.size > diskB.size)):
                        diskB.y = 445
                        deactB()
                    elif ((diskT.y == 445 and diskT.size > diskB.size) or (diskM.y == 445 and diskM.size > diskB.size)):
                        diskB.y = 418
                        deactB()                    
                else:
                    diskB.y = 472
                    deactB()

                #diskB.active = False
                #move = False

            sel = None
        else:
            if sel == diskB:
                diskB.y = 210
                move = True
                diskB.active = True
            if sel == diskM:
                diskM.y = 210
                move = True
                diskM.active = True
            if sel == diskT:
                diskT.y = 210
                move = True
                diskT.active = True

        inDelay = 1
