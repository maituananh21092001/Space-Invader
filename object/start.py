import pygame

import sys
from object.const import DARK_MODE_COLOR, HEIGHT, LIGHT_MODE_COLOR, WHITE, WIDTH

from object.game import Game
from object.level.easy import Easy
from object.level.medium import Medium
from object.level.hard import Hard

class Start:
    
    easy = Easy()
    med = Medium()
    hard = Hard()
    status = []
    def init(self):
        
        pygame.init()
        game = Game(6, 2)
        res = (WIDTH, HEIGHT)
        screen = pygame.display.set_mode(res)

        bg = pygame.image.load("./data/start.bmp") # background
        mode_font = pygame.font.SysFont('Corbel', 20) # font và size chữ của nút chế độ chơi
        
        # văn bản hiển thị nút chế độ chơi
        text = mode_font.render('easy', True, WHITE)
        text1 = mode_font.render('medium', True, WHITE)
        text2 = mode_font.render('hard', True, WHITE)
        
        while True:

            screen.blit(bg, (0, 0)) # in background

            mouse = pygame.mouse.get_pos() # lưu tọa độ chuột vào biến dưới kiểu tuple

            # thay đổi màu của nút tối hơn khi di chuột đến nút
            if WIDTH / 3 + 100 <= mouse[0] <= WIDTH / 3 + 240 and HEIGHT / 3 + 150 <= mouse[1] <= HEIGHT / 3 + 190:
                pygame.draw.rect(screen, DARK_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 150, 140, 40])
                pygame.draw.rect(screen, LIGHT_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 200, 140, 40])
                pygame.draw.rect(screen, LIGHT_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 250, 140, 40])
            elif WIDTH/3+100 <= mouse[0] <= WIDTH/3+240 and HEIGHT/3+200 <= mouse[1] <= HEIGHT/3+240:
                pygame.draw.rect(screen, DARK_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 200, 140, 40])
                pygame.draw.rect(screen, LIGHT_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 150, 140, 40])
                pygame.draw.rect(screen, LIGHT_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 250, 140, 40])
            elif WIDTH/3+100 <= mouse[0] <= WIDTH/3+240 and HEIGHT/3+250 <= mouse[1] <= HEIGHT/3+290:
                pygame.draw.rect(screen, LIGHT_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT /3 + 200, 140 ,40])
                pygame.draw.rect(screen, LIGHT_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 150, 140, 40])
                pygame.draw.rect(screen, DARK_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 250, 140, 40])
            else:
                pygame.draw.rect(screen, LIGHT_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 150, 140, 40])
                pygame.draw.rect(screen, LIGHT_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 200, 140, 40])
                pygame.draw.rect(screen, LIGHT_MODE_COLOR, [WIDTH / 3 + 100, HEIGHT / 3 + 250, 140, 40])
            
            for ev in pygame.event.get():
                
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    
                if ev.type == pygame.MOUSEBUTTONDOWN:  # kiểm tra có nhấp chuột hay không
                    
                    # nếu nhấp chuột vào nút thì game bắt đầu với chế độ tương ứng
                    if WIDTH / 3 + 100 <= mouse[0] <= WIDTH / 3 + 240 and HEIGHT / 3 + 150 <= mouse[1] <= HEIGHT / 3 + 190:
                        self.status = [self.easy.speed(), self.easy.numberEnemy()]
                        game = Game(self.status[0], self.status[1])
                        game.run()
                        pygame.quit()
                    if WIDTH / 3 + 100 <= mouse[0] <= WIDTH / 3 + 240 and HEIGHT / 3 + 200 <= mouse[1] <= HEIGHT / 3 + 240:
                        self.status = [self.med.speed(), self.med.numberEnemy()]
                        game = Game(self.status[0], self.status[1])
                        game.run()
                        pygame.quit()
                    if WIDTH / 3 + 100 <= mouse[0] <= WIDTH / 3 + 240 and HEIGHT / 3 + 250 <= mouse[1] <= HEIGHT / 3 + 290:
                        self.status = [self.hard.speed(), self.hard.numberEnemy()]
                        game = Game(self.status[0], self.status[1])
                        game.run()
                        pygame.quit()

            # ghi tên chế độ chơi lên nút
            screen.blit(text, (WIDTH / 3 + 150, HEIGHT / 3 + 150 + 10))
            screen.blit(text1, (WIDTH / 3 + 140, HEIGHT/ 3 + 200 + 10))
            screen.blit(text2, (WIDTH / 3 + 150, HEIGHT / 3 + 250 + 10))

            pygame.display.update() # cập nhật