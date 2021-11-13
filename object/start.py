import pygame

import sys

from object.game import Game
from object.level.easy import Easy
from object.level.medium import Medium
from object.level.hard import Hard
# initializing the constructor
class Start:
    
    easy = Easy()
    med = Medium()
    hard = Hard()
    status=[]
    def init(self):
        
        pygame.init()
        game = Game(6,2)
        # screen resolution
<<<<<<< HEAD
        res = (1000,1000)
        
        # opens up a window
        screen = pygame.display.set_mode(res)
        
=======
        res = (1000,600)
        
        # opens up a window
        screen = pygame.display.set_mode(res)

        # background
        bg = pygame.image.load("./data/start.bmp")

>>>>>>> nhung
        # white color
        color = (255,255,255)
        
        # light shade of the button
<<<<<<< HEAD
        color_light = (170,170,170)
        
        # dark shade of the button
        color_dark = (100,100,100)
=======
        color_light = (177,117,255)
        
        # dark shade of the button
        color_dark = (164,108,241)
>>>>>>> nhung
        
        # stores the width of the
        # screen into a variable
        width = screen.get_width()
        
        # stores the height of the
        # screen into a variable
        height = screen.get_height()
        
        # defining a font
        smallfont = pygame.font.SysFont('Corbel',20)
        
        # rendering a text written in
        # this font
        text = smallfont.render('easy' , True , color)
        text1 = smallfont.render('medium', True, color)
        text2 = smallfont.render('hard',True,color)
        while True:
            
            for ev in pygame.event.get():
                
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    
                #checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    
                    #if the mouse is clicked on the
                    # button the game is terminated
<<<<<<< HEAD
                    if width/3 <= mouse[0] <= width/3+140 and height/3 <= mouse[1] <= height/3+40:
=======
                    if width/3+100 <= mouse[0] <= width/3+240 and height/3+150 <= mouse[1] <= height/3+190:
>>>>>>> nhung
                        self.status = [self.easy.speed(),self.easy.numberEnemy()]
                        game = Game(self.status[0],self.status[1])
                        game.run()
                        pygame.quit()
<<<<<<< HEAD
                    if width/3 <= mouse[0] <= width/3+140 and height/3+50 <= mouse[1] <= height/3+90:
=======
                    if width/3+100 <= mouse[0] <= width/3+240 and height/3+200 <= mouse[1] <= height/3+240:
>>>>>>> nhung
                        self.status = [self.med.speed(),self.med.numberEnemy()]
                        game = Game(self.status[0],self.status[1])
                        game.run()
                        pygame.quit()
<<<<<<< HEAD
                    if width/3 <= mouse[0] <= width/3+140 and height/3+100 <= mouse[1] <= height/3+140:
=======
                    if width/3+100 <= mouse[0] <= width/3+240 and height/3+250 <= mouse[1] <= height/3+290:
>>>>>>> nhung
                        self.status = [self.hard.speed(),self.hard.numberEnemy()]
                        game = Game(self.status[0],self.status[1])
                        game.run()
                        pygame.quit()
                        
<<<<<<< HEAD
            # fills the screen with a color
            screen.fill((255,255,60))
=======
            # print background
            screen.blit(bg, (0, 0))
>>>>>>> nhung
            
            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()
            
            # if mouse is hovered on a button it
            # changes to lighter shade 
<<<<<<< HEAD
            if width/3 <= mouse[0] <= width/3+140 and height/3 <= mouse[1] <= height/3+40:
                pygame.draw.rect(screen,color_light,[width/3,height/3,140,40])
                pygame.draw.rect(screen,color_dark,[width/3,height/3+50,140,40])
                pygame.draw.rect(screen,color_dark,[width/3,height/3+100,140,40])
            elif(width/3<=mouse[0]<=width/3+140 and height/3+50 <= mouse[1]<= height/3+90):
                pygame.draw.rect(screen,color_light,[width/3,height/3+50,140,40])
                pygame.draw.rect(screen,color_dark,[width/3,height/3,140,40])
                pygame.draw.rect(screen,color_dark,[width/3,height/3+100,140,40])
            elif(width/3<=mouse[0]<=width/3+140 and height/3+100 <= mouse[1]<= height/3+140):
                pygame.draw.rect(screen,color_dark,[width/3,height/3+50,140,40])
                pygame.draw.rect(screen,color_dark,[width/3,height/3,140,40])
                pygame.draw.rect(screen,color_light,[width/3,height/3+100,140,40])
            else:
                pygame.draw.rect(screen,color_dark,[width/3,height/3,140,40])
                pygame.draw.rect(screen,color_dark,[width/3,height/3+50,140,40])
                pygame.draw.rect(screen,color_dark,[width/3,height/3+100,140,40])
            
            # # superimposing the text onto our button
            screen.blit(text , (width/3+50,height/3))
            screen.blit(text1 , (width/3+50,height/3+50))
            screen.blit(text2,(width/3+50,height/3+100))
=======
            if width/3+100 <= mouse[0] <= width/3+240 and height/3+150 <= mouse[1] <= height/3+190:
                pygame.draw.rect(screen,color_light,[width/3+100,height/3+150,140,40])
                pygame.draw.rect(screen,color_dark,[width/3+100,height/3+200,140,40])
                pygame.draw.rect(screen,color_dark,[width/3+100,height/3+250,140,40])
            elif(width/3+100<=mouse[0]<=width/3+240 and height/3+200 <= mouse[1]<= height/3+240):
                pygame.draw.rect(screen,color_light,[width/3+100,height/3+200,140,40])
                pygame.draw.rect(screen,color_dark,[width/3+100,height/3+150,140,40])
                pygame.draw.rect(screen,color_dark,[width/3+100,height/3+250,140,40])
            elif(width/3+100<=mouse[0]<=width/3+240 and height/3+250 <= mouse[1]<= height/3+290):
                pygame.draw.rect(screen,color_dark,[width/3+100,height/3+200,140,40])
                pygame.draw.rect(screen,color_dark,[width/3+100,height/3+150,140,40])
                pygame.draw.rect(screen,color_light,[width/3+100,height/3+250,140,40])
            else:
                pygame.draw.rect(screen,color_dark,[width/3+100,height/3+150,140,40])
                pygame.draw.rect(screen,color_dark,[width/3+100,height/3+200,140,40])
                pygame.draw.rect(screen,color_dark,[width/3+100,height/3+250,140,40])
            
            # # superimposing the text onto our button
            screen.blit(text , (width/3+150,height/3+150+10))
            screen.blit(text1 , (width/3+140,height/3+200+10))
            screen.blit(text2,(width/3+150,height/3+250+10))
>>>>>>> nhung
            # updates the frames of the game
            pygame.display.update()