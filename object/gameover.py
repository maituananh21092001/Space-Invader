import pygame
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
                        if event.type == pygame.KEYDOWN:  # Thoát
                            newGame = True
                            break
                    if(newGame == True):
                        break
                    self.text(100, 100, "Scores:{}".format(
                        self.scores), 40,'./data/font/ARCADE_R.TTF',WHITE)  # In điểm
                    self.text(self.xScreen/2 - 100, self.yScreen - 100, "RETRY", 50,'./data/font/ARCADE_R.TTF',GREEN)  # In điểm
                    self.text(self.xScreen/2-100, self.yScreen/2-100,
                                    "GAME OVER", 50,'./data/font/ARCADE_I.TTF',WHITE)  # In Thông báo thua
                    pygame.display.update()
                self.scores = 0      # Trả các biến về giá trị ban đầu
                self.listBullet = []
                self.listEnemy = []
                self.YGameOver = 0
                self.music("./data/musictheme.wav",-1)
