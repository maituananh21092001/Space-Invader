import pygame
from os import path
from object.const import *

def gameover(self):
                newGame = False
                self.screen.fill(BLACK)
                pygame.mixer.stop()
                self.music("./data/Game Over Sound Effect.wav",0)                
                while(True):
                    for event in pygame.event.get():   # Nếu nhấn
                        if event.type == pygame.QUIT    :  # Thoát
                            self.gamerunning = False
                            newGame = True
                            break
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:                           
                                newGame = True
                                break
                            if event.key == pygame.K_q:                           
                                newGame = False
                                pygame.quit()
                                break
                    if(newGame == True):
                        break
                    self.text(
                            WIDTH/2 - 75, HEIGHT/2, 
                            "Scores:{}".format(self.scores),
                            25,
                            './data/font/ARCADE_R.TTF',
                            WHITE)
                    self.text(
                            WIDTH/2-250, HEIGHT/2-100,
                            "GAME OVER", 
                            60,
                            './data/font/ARCADE_I.TTF',
                            WHITE)  # In Thông báo thua

                    self.draw_text("Press R to try again", 22, GREEN,100, HEIGHT * 3 / 4)
                    self.draw_text(f"Mode: ", 22, WHITE,50,50)
                    self.draw_text("Press Q to quit", 22, RED, WIDTH - 100, HEIGHT * 3 / 4)
                    if self.scores > self.highscore:
                            self.highscore = self.scores
                            self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 20)
                            with open(path.join(self.dir, HS_FILE), 'w') as f:
                                f.write(str(self.scores))
                    else:
                        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)

                    pygame.display.update()

                self.scores = 0      # Trả các biến về giá trị ban đầu
                self.listBullet = []
                self.listEnemy = []
                self.YGameOver = 0
                self.music("./data/musictheme.wav",-1)
