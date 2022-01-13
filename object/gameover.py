import pygame
import time
from os import path
from object import start
from object.const import *
def gameover(self):
                newGame = False
                res = (WIDTH, HEIGHT)
                screen = pygame.display.set_mode(res)
                bg = pygame.image.load("./data/gameoverbg.bmp") # background
                pygame.mixer.stop()
                self.music("./data/Game Over Sound Effect.wav",0)                
                while(True):
                    screen.blit(bg, (0, 0))
                    for event in pygame.event.get():   # Nếu nhấn
                        if event.type == pygame.QUIT    :  # Thoát
                            self.gamerunning = False
                            newGame = True
                            break
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                pygame.mixer.stop()                           
                                newGame = True
                                break
                            if event.key == pygame.K_q:
                                newGame = False
                                pygame.quit()
                                s = start.Start()
                                s.init()                           
                                break
                    if(newGame == True):
                        break
                    self.text(
                            WIDTH/2 - 100, HEIGHT/2, 
                            "Scores:{}".format(self.scores),
                            25,
                            './data/font/ARCADE_R.TTF',
                            WHITE)
                    self.text(
                            200, HEIGHT * 3 / 4,
                            "Press R to try again",
                            25,
                            './data/font/Quicksand-Bold.ttf',
                            RETRY_COLOR)
                    self.text(
                            WIDTH - 400, HEIGHT * 3 / 4,
                            "Press Q to quit",
                            25,
                            './data/font/Quicksand-Bold.ttf',
                            QUIT_COLOR)
                    self.draw_text(f"Mode: {self.level()}", 25, WHITE,100,50)
                    if self.scores > self.highscore:
                        self.highscore = self.scores
                        self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2 + 150, HEIGHT / 2 + 40)
                        with open(path.join(self.dir, f"./level/{self.level()}.txt"), 'w') as f:
                            f.write(str(self.scores))                           
                    else:
                        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
                    pygame.display.update()
                self.scores = 0      # Trả các biến về giá trị ban đầu
                self.listBullet = []
                self.listEnemy = []
                self.YGameOver = 0
                self.xPlanes, self.yPlanes = self.xScreen / \
            2, self.yScreen-100
                self.K_DOWN = False                    
                self.K_UP = False
                self.K_LEFT = False                   
                self.K_RIGHT = False
                self.music("./data/musictheme.ogg",-1)
