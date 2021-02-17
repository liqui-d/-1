 
import pygame
import sys
import random
import time
 
BLACK = (0, 0, 0)
LBLUE = (0, 192, 255)
PINK = (255, 0, 225)


# main関数
def main():
    # 前処理
    pygame.init()
    pygame.display.set_caption("ゲームテストプログラム")
    screen = pygame.display.set_mode((1280, 640))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("hg正楷書体pro", 32)
    img_pic = pygame.image.load("main1.png") #メインキャラ
    fx=600
    fy=500
    enemmy_pic = pygame.image.load("enemmy1.png") #敵キャラ
    ex1=600
    ey1=100
    ex2=300
    ey2=300
    ex3=900
    ey3=400

    while True:  # ゲームループ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("KEY_UP")
                fy -= 10
            elif event.key == pygame.K_DOWN:
                print("KEY_DOWN")
                fy += 10
            elif event.key == pygame.K_RIGHT:
                print("KEY_RIGHT")
                fx += 10
            elif event.key == pygame.K_LEFT:
                print("KEY_LEFT")
                fx -= 10

        if fx == ex1 and fy == ey1:
            print("当たり！")
        elif fx == ex2 and fy == ey2:
                print("当たり！")
        elif fx == ex3 and fy == ey3:
                print("当たり！")
 
        # ゲーム画面描画
        screen.fill(BLACK)
        screen.blit(img_pic,[fx,fy])
        screen.blit(enemmy_pic,[ex1,ey1])
        screen.blit(enemmy_pic,[ex2,ey2])
        screen.blit(enemmy_pic,[ex3,ey3])
        pygame.display.update()
        clock.tick(10)
        
    '''
    while True:
        print("")
        if fx = ex1 and fy = ey1:
            print("HIT!!")
        elif fx = ex2 and fy = ey2:
            print("HIT!!")
        elif fx = ex3 and fy = ey3:
            print("HIT!!")
    '''    

if __name__ == '__main__':
    main()