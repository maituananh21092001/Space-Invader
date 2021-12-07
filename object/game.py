import pygame
import time
import random
from pygame import mixer
from object import start
from pygame.time import Clock
from object.const import *
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from object.gameover import gameover
from object.level import *
import sys


from os import path

from object.level.easy import Easy
from object.level.hard import Hard
from object.level.medium import Medium


class Game:
    def __init__(self, Espeed, NumberEnemy):

        pygame.init()  # Init pygame
        self.xScreen, self.yScreen = WIDTH,HEIGHT  # Screen create
        self.VBullet = 15  # Tốc độ Bullet
        self.VPlanes = 15  # Tốc độ Planes
        self.VEnemy = Espeed  # Tốc độ Enemy
        self.scores = 0  # Điểm số
        self.numberEnemy = NumberEnemy  # Số lượng enemy trong một screen
        self.numberBullet = 6  # Số bullet trong một screen
        linkBackGround = './data/background.bmp'  # Đường dẫn ảnh background
        self.linkEnemy = './data/enemy.bmp'  # Đường dẫn ảnh Enemy
        self.linkPlanes = './data/planes.bmp'  # Đường dẫn ảnh Planes
        self.linkEnemyKilled = './data/enemykilled.bmp' # Đường dẫn ảnh EnemyKilled
        self.sizexPlanes, self.sizeyPlanes = 80, 80
        self.xPlanes, self.yPlanes = self.xScreen / \
            2, self.yScreen-100  # Khởi tao vị trí ban đầu planes
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen))  # Khởi tao kích thước màn hình
        pygame.display.set_caption("Space Invaders - Group 3")
        self.background = pygame.image.load(linkBackGround)
        icon = pygame.image.load(self.linkPlanes)
        pygame.display.set_icon(icon)  # Set icon cho screen
        self.gamerunning = True
        pause = False
        self.listBullet = []
        self.listEnemy = []
        self.YGameOver = 0
        self.K_DOWN = self.K_UP = self.K_LEFT = self.K_RIGHT = False
        self.load_data()
        self.font_name = pygame.font.match_font(FONT_NAME)
    #clock = pygame.time.Clock()
    #clock.tick(60)    
    def level(self):
        if self.VEnemy == Easy.speed(self):
            return Easy.level(self)
        elif self.VEnemy == Medium.speed(self):
            return Medium.level(self)
        else:
            return Hard.level(self)
    def music(self, url, x):  # Âm thanh bắn với tham số x là số lần lặp lại, mặc định 0 là không lặp, -1 là luôn lặp
        sound = mixer.Sound(url)
        sound.play(x)

    def text(self, x, y, text, size,font,color):  # Hiển thị điểm
        font = pygame.font.Font(font, size)
        txt = font.render(str(text), True, color)
        self.screen.blit(txt, (x, y))

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def image_draw(self, url, xLocal, yLocal, xImg, yImg):  # In ra hình ảnh
        Img = pygame.image.load(url).convert_alpha()
        Img = pygame.transform.scale(Img, (xImg, yImg))  # change size image
        self.screen.blit(Img, (xLocal, yLocal))

    def enemy(self):  # Quản lý Enemy
        for count, i in enumerate(self.listEnemy):
            xEnemy = i["xEnemy"]  # Lấy toạ độ X
            yEnemy = i["yEnemy"]  # Lấy toạ độ Y
            self.YGameOver
            # print("đổi")
            if xEnemy < 0 or xEnemy > self.xScreen-self.sizexPlanes:  # Nếu chạm vào hai bên phải trái
                # thì đổi hướng
                self.listEnemy[count]["direction"] = not self.listEnemy[count]["direction"]
            self.image_draw(self.linkEnemy, xEnemy, yEnemy, self.sizexPlanes,
                            self.sizeyPlanes)  # In enemy ra màn hình
            self.listEnemy[count]["xEnemy"] = xEnemy + \
                (self.VEnemy if self.listEnemy[count]
                 ["direction"] == False else -self.VEnemy)
            self.listEnemy[count]["yEnemy"] = yEnemy + \
                self.VEnemy/2.5  # Toạn độ x xông tốc độ Enemy/3
            # Gán giá trị lớn nhất của Enemy theo y
            self.YGameOver = yEnemy if yEnemy > self.YGameOver else self.YGameOver

    def bullet(self):
        for count, i in enumerate(self.listBullet):
            xBullet = i["xBullet"]  # Lấy trục tọa độ theo X
            yBullet = i["yBullet"]  # Lấy trục tọa độ theo Y
            self.image_draw('./data/bullet.bmp', xBullet,
                            yBullet, 50, 50)  # In ra bullet
            self.listBullet[count]["yBullet"] = yBullet - \
                self.VBullet  # Tiến y vè phía trước
            if yBullet <= 5:  # nếu toạn độ Y phía trên nàm hình thì xóa
                self.listBullet.remove(self.listBullet[count])

    def load_data(self):
        # load high score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, f"./level/{self.level()}.txt"), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
    def pause(self):
        loop = 1
        self.text(300, HEIGHT / 2 - 100, "GAME PAUSE", 80, './data/font/Cuprum-Bold.ttf', WHITE)
        self.text(WIDTH / 2 - 300, HEIGHT / 2 + 40, "Press space to continue", 22, './data/font/Quicksand-Bold.ttf', WHITE)
        self.text(WIDTH / 2 + 100, HEIGHT / 2 + 40, "Press Q to quit game", 22, './data/font/Quicksand-Bold.ttf', WHITE)
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = 0
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loop = 0
                    if event.key == pygame.K_SPACE:
                        self.screen.fill((0, 0, 0))
                        loop = 0
                    if event.key == pygame.K_q:
                        loop = 0
                        pygame.quit()
                        s = start.Start()
                        s.init()
            pygame.display.update()
            # screen.fill((0, 0, 0))
            clock = pygame.time.Clock()
            clock.tick(60)
    def run(self):

        self.music("./data/musictheme.ogg",-1)
        while self.gamerunning:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():  # Bắt các sự kiện
                if event.type == pygame.QUIT:  # sự kiện nhấn thoát
                    self.gamerunning = False
                if event.type == pygame.KEYDOWN:  # sự kiện có phím nhấn xuống
                    if event.key == pygame.K_DOWN:
                        self.K_DOWN = True
                    if event.key == pygame.K_UP:
                        self.K_UP = True
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = True
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = True
                    if event.key == pygame.K_q:
                       self.pause()
                    if event.key == pygame.K_SPACE:
                        if len(self.listBullet) < self.numberBullet:

                            self.music("./data/laser.ogg",0)
                            self.listBullet.append({  # Add Thêm bullet
                                "xBullet": self.xPlanes+self.sizexPlanes/2 - 25,
                                "yBullet": self.yPlanes-self.sizexPlanes/2,
                            })
                        # print(self.listBullet)
                if event.type == pygame.KEYUP:  # sự kiện thả phím
                    if event.key == pygame.K_DOWN:
                        self.K_DOWN = False
                    if event.key == pygame.K_UP:
                        self.K_UP = False
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = False
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = False
            if self.K_DOWN:
                self.yPlanes = self.yPlanes+self.VPlanes/2  # Tiến lên
            if self.K_UP:
                self.yPlanes = self.yPlanes-self.VPlanes/2  # Tiến xuống
            if self.K_LEFT:
                self.xPlanes = self.xPlanes-self.VPlanes  # Tiến trái
            if self.K_RIGHT:
                self.xPlanes = self.xPlanes+self.VPlanes  # Tiến phải
            
            # Kiểm tra có vượt quá giới hạn màn hình  và sét về lề màn hình
            self.xPlanes = 0 if self.xPlanes < 0 else self.xPlanes
            self.xPlanes = self.xScreen-self.sizexPlanes if self.xPlanes + \
                self.sizexPlanes > self.xScreen else self.xPlanes
            self.yPlanes = 0 if self.yPlanes < 0 else self.yPlanes
            self.yPlanes = self.yScreen-self.sizeyPlanes if self.yPlanes + \
                self.sizeyPlanes > self.yScreen else self.yPlanes

            # nếu số lượng Enemy ít hơn self.numberEnemy thì tạo thêm
            if len(self.listEnemy) < self.numberEnemy:
                self.listEnemy.append({
                    "xEnemy": random.randint(0, self.xScreen-self.sizexPlanes),
                    "yEnemy": random.randint(-50, self.yScreen/6),
                    "direction": random.choice((True, False))
                })
            listEnemy2 = self.listEnemy
            # Kiểm tra có trúng bullet
            for countEnemy, enemyIteam in enumerate(listEnemy2):
                xEnemy = enemyIteam["xEnemy"]
                yEnemy = enemyIteam["yEnemy"]
                for countBullet, bulletIteam in enumerate(self.listBullet):
                    xBullet = bulletIteam["xBullet"]
                    yBullet = bulletIteam["yBullet"]
                    # Kiểm tra bullet có nằm giữa Enemy theo trục x không
                    isInX = xEnemy <= xBullet <= xEnemy+self.sizexPlanes
                    # Kiểm tra bullet có nằm giữa Enemy theo trục y không
                    isInY = yEnemy <= yBullet <= yEnemy+self.sizexPlanes/1.2
                    if(isInX and isInY):  # nếu nằm giữa
                        self.music('./data/invaderkilled.ogg',0)
                        self.image_draw(self.linkEnemyKilled, xEnemy, yEnemy, self.sizexPlanes, self.sizeyPlanes)
                        self.listEnemy.remove(
                            self.listEnemy[countEnemy])  # Xóa Enemy
                        self.listBullet.remove(
                            self.listBullet[countBullet])  # Xóa Bullet
                        self.scores = self.scores + 1  # Cộng thêm điểm
                        # print(scores)
                        break
            if self.numberEnemy < 7:
                self.numberEnemy = (self.scores/15) + 2

            if self.YGameOver > self.yScreen-50: # Nếu Enemy về đích 
                gameover(self)
            listEnemy3 = self.listEnemy
            rectPlane = pygame.Rect(self.xPlanes,self.yPlanes,self.sizexPlanes,self.sizeyPlanes).inflate(-25,-25)
            #pygame.draw.rect(self.screen, WHITE, rectPlane)
            for enemycount in listEnemy3:
                rectEnemy = pygame.Rect(enemycount.get("xEnemy"),enemycount.get("yEnemy"),self.sizexPlanes,self.sizeyPlanes).inflate(-25,-25)
                collide = rectPlane.colliderect(rectEnemy)
                if collide:
                    gameover(self)
                #pygame.draw.rect(self.screen,RED,rectEnemy)
            self.text(10, 10, "Scores:{}".format(self.scores), 20,'./data/font/ARCADE_N.TTF',WHITE)
            self.enemy()
            self.bullet()
            self.image_draw(self.linkPlanes, self.xPlanes,
                            self.yPlanes, self.sizexPlanes, self.sizeyPlanes)           
            pygame.display.update()  # Update

