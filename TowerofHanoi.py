import pygame, os

#Tower of Hanoi

#initialize game
pygame.init()

#parameters/settings for window
screenW = 840
screenH = 500
wn = pygame.display.set_mode((screenW, screenH))
bg = ((255, 255, 255))
pygame.display.set_caption("Tower of Hanoi Puzzle")
arrowimg = pygame.image.load(os.path.join('C:\\Game','arrow.png')).convert()

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
        self.size = x * y
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
    arrowS.draw(wn)
    towerA.draw(wn)
    towerB.draw(wn)
    towerC.draw(wn)
    diskB.draw(wn)
    diskM.draw(wn)
    diskT.draw(wn)
    pygame.draw.line(wn, (0,0,0), (170,0), (170,500))
    #pygame.draw.line(wn, (0,0,0), (200,0), (200,500))
    pygame.draw.line(wn, (0,0,0), (420,0), (420,500))
    #pygame.draw.line(wn, (0,0,0), (450,0), (450,500))
    pygame.draw.line(wn, (0,0,0), (670,0), (670,500))
    #pygame.draw.line(wn, (0,0,0), (700,0), (700,500))

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
print(move)
diskY = [diskB.y, diskM.y, diskT.y]
while run:
    wnDraw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if inDelay > 0:
        inDelay += 1
        if inDelay > 100:
            inDelay = 0

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and inDelay == 0:
        
        if move == True:
            pass
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
                    diskB.x = 663
                elif arrowS.x == 413:
                    arrowS.x = 163
                elif arrowS.x == 663:
                    arrowS.x = 413

            if diskM.active == True:
                if arrowS.x == 163:
                    arrowS.x = 663
                elif arrowS.x == 413:
                    arrowS.x = 163
                elif arrowS.x == 663:
                    arrowS.x = 413

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


    if keys[pygame.K_SPACE]:    #IN REAL LIFE THIS SHOULD NOT WORK AND ACTUALLY IT WONT WORK LOL RIP // IM DOING SO MUCH WORK BUT IT WONT WORK BC OF MY MIN IM SO OOF oh well this is a learninf thingy
        sel = min(diskY)
    
        if move == True:
            if diskT.active == True:
                diskT.y = 472
                diskT.active = False
                move = False
            elif diskM.active == True:
                pass
            elif diskB.active == True:
                pass
        else:
            if sel == diskY[0]:
                diskB.y = 210
                move = True
                diskB.active = True
            if sel == diskY[1]:
                diskM.y = 210
                move = True
                diskM.y = True
            if sel == diskY[2]:
                diskT.y = 210
                move = True
                diskT.active = True

        inDelay = 1
