import pygame

"""
After finding put about the recursive algorithm for Tower of Hanoi,
I thought it would be a fun little project to program the game myself
and give myself a fairly simple starting point and get a better understanding
of how pygame works. Doing this on my own using only documentation and such
hope this goes well! I plan to add a button which will allow me to implement
the recursive algorithm and solve the puzzle for the user.

update 1: i did something, i added in my towers and my first disk, got them centered
and all. The math isn't difficult too far, I'm just worried about having to move all the disks.
Thinking I'll just have them teleport from disk to disk 
"""

#initialize game
pygame.init()

#parameters/settings for window
screenW = 840
screenH = 500
wn = pygame.display.set_mode((screenW, screenH))
bg = ((255, 255, 255))
pygame.display.set_caption("Tower of Hanoi Puzzle")

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

    def draw(self, wn):
        pygame.draw.rect(wn, self.color, (self.x, self.y, self.width, self.height))

#update(draw) objects in window
def wnDraw():
    wn.fill(bg)
    towerA.draw(wn)
    towerB.draw(wn)
    towerC.draw(wn)
    diskB.draw(wn)


    pygame.display.update()
   
#create the towers
towerA = tower((screenW/4 - 50), 230, 50, 270, (0, 0, 0))
towerB = tower(((screenW/4)*2), 230, 50, 270, (0, 0, 0))
towerC = tower(((screenW/4)*3 + 50), 230, 50, 270, (0, 0, 0))

#create the disks, currently limited to 3 disks, hopefully will allow creation based on user input
diskB =  disk(65, 475, 240, 25, (255, 0, 0))

#main loop
run = True
while run:
    wnDraw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False