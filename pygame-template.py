import pygame, sys, os, math
from pygame.locals import *
from random import randint




WINDOWWIDTH = 800
WINDOWHEIGHT = 600
GAMENAME = "AWESOME GAME"
FRAMERATE = 60
BGCOLOR = (255,255,255)

class Game:
    ##########CLASS VARIABLES##########
    
    
    ##########CONSTRUCTOR##########
    def __init__(self):
        pass
    
    ##########MAIN FUNCTION##########
    def main(self):
        playing = True
        pygame.init()
        clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
        pygame.display.set_caption(GAMENAME)
        
        ##########GAME LOOP##########
        while playing:
            delta = clock.tick(FRAMERATE)
            
            ##########EVENT HANDLING##########
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
            ##################################
                    
            self.processLogic()
            self.drawScreen()
            pygame.display.flip()
    
    ##########MAKES CHANGES FROM LAST FRAME##########
    def processLogic(self):
        pass
    
    ##########DRAWS THE FRAME##########
    def drawScreen(self):
        self.surface.fill(BGCOLOR)
    def quit(self):
        pygame.quit()
        sys.exit()
        
##########STARTS EVERYTHING##########
if __name__=='__main__':
    game = Game()
    game.main()
