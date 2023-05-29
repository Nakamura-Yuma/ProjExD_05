import sys
import time
import random

import pygame as pg


WIDTH = 1600
HEIGHT = 900


class Player(pg.sprite.Sprite):
    """
    操作キャラクターに関するクラス
    """
    
    def __init__(self):
        super().__init__()
        self.imgs = [pg.transform.rotozoom(pg.image.load(f"ex05/fig/run{i}.png"), 0, 0.4) for i in range(1, 4)] 
        self.num = 1
        self.image = self.imgs[self.num]
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 185
        self.rect.centerx = WIDTH/2
        self.num_r = 0
        self.tmr = 0
        self.jump = False
        self.jump_tmr = 0
        self.sliding = False
    
    def update(self, screen: pg.Surface, num=0):
        if self.jump:
            if self.jump_tmr < 20:
                self.rect.move_ip(0, -15) #上にジャンプ
            else:
                self.rect.move_ip(0, 15) #ジャンプ後、降下
            self.jump_tmr += 1
            if self.jump_tmr >= 40:
                self.jump = False
                self.jump_tmr = 0
            screen.blit(self.image, self.rect) #ジャンプしているキャラクターを描画

        elif self.sliding:
            self.image = self.imgs[2]
            self.rect = self.image.get_rect() 
            self.rect.centerx = WIDTH/2
            self.rect.bottom = HEIGHT-185
            self.sliding_tmr = 0
            screen.blit(self.image, self.rect) #スライディングしているキャラクターを描画

        else:
            self.tmr += 1
            if self.tmr % 5 == 0:
                self.num_r += 1
                self.image = self.imgs[self.num_r%2] #キャラクターを交互に表示
            self.rect = self.image.get_rect()
            self.rect.bottom = HEIGHT - 185
            self.rect.centerx = WIDTH/2
            screen.blit(self.image, self.rect) #走っているキャラクターを描画


class Object(pg.sprite.Sprite):
    """
    障害物に関するクラス
    """
    
    def __init__(self, player: pg.Surface):
        super().__init__()
        self.image = pg.Surface((50, 100))
        pg.draw.rect(self.image, (0, 0, 0), pg.Rect(0, 0, 50, 100))
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 194
        self.rect.left = WIDTH
        
    def update(self, screen: pg.Surface):
        self.rect.move_ip(-10, 0) #障害物を動かす
        screen.blit(self.image, self.rect) #障害物を描画

class Object2(pg.sprite.Sprite):
    """
    障害物2(空中)に関するクラス
    """
    
    def __init__(self, player: pg.Surface):
        super().__init__()
        self.image = pg.Surface((50, 100))
        pg.draw.rect(self.image, (0, 0, 0), pg.Rect(0, 0, 50, 100))
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 350
        self.rect.left = WIDTH
        
    def update(self, screen: pg.Surface):
        self.rect.move_ip(-10, 0) #障害物2を動かす
        screen.blit(self.image, self.rect) #障害物2を描画

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("Run on Fence") 
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg = pg.transform.rotozoom(pg.image.load("ex05/fig/background.png"), 0, 1.25)
    
    objs = pg.sprite.Group()
    objs2 = pg.sprite.Group()
    player = Player()
    
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return #×ボタンで終了
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player.jump = True #スペースキーでジャンプする
                if event.key == pg.K_DOWN:
                    player.sliding = True #下キーでスライディング
            else:
                player.sliding = False


        screen.blit(bg, [0, 0]) #背景を描画
        
        if tmr % 250 == 0:
            objs.add(Object(player)) #障害物呼び出し
        else:
            if tmr % 150 == 0:
                objs2.add(Object2(player)) #障害物2呼び出し
        
        for obj in objs:
            obj.update(screen) #障害物をアップデート

        for obj in objs2:
            obj.update(screen) #障害物をアップデート
        
        for obj in pg.sprite.spritecollide(player, objs, True): #障害物との接触判定
            time.sleep(2)
            return
    
        for obj in pg.sprite.spritecollide(player, objs2, True): #障害物2との接触判定
            time.sleep(2)
            return


        player.update(screen)
        pg.display.update()
        tmr += 1
        clock.tick(50)
        
        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()