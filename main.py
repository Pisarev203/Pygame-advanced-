import pygame
##импортируем пайгейм для графф движка
applex = 100
appley = 100
x = 0
y = 0
size = 80 ##размер клетки змейки
res = 800 ##размер окна
len = 1 ##индекс длинны змейки
snake = [(x, y)] ##массив для создания самой змейки
dx, dy = 0, 0 ##направление движения змейки по координатам
lenght = 1
speed = 2 ##скорость змейки
lvl=int(input("выберите лвл от 1 до 3"))
s=int(input("w"))
pygame.init()
okno = pygame.display.set_mode([res,res])
time = pygame.time.Clock()
if lvl==1 :
    while x==0 and y==0 or x==0 and y==80 or x==0 and y==160 or x==80 and y==160 or x==160 and y==160 or x==160 and y==80 or x==160 and y==0 or x==240 and y==0 or x==320 and y==0 or x==320 and y==80 or x==320 and y==160 or x==320 and y==240 or x==400 and y==80 or x==480 and y==80 or x==560 and y==80 or x==640 and y==80 or x==640 and y==0 or x==400 and y==320 or x==480 and y==320 or x==560 and y==320 or x==560 and y==240 or x==640 and y==240  or x==720 and y==240  or x==720 and y==320 or x==720 and y==400 or x==720 and y==480 or x==720 and y==560  or x==720 and y==640 or x==320 and y==400 or x==320 and y==320 or x==160 and y==240 or x==160 and y==320 or x==80 and y==320 or x==0 and y==320 or x==80 and y==400 or x==80 and y==480 or x==80 and y==560 or x==80 and y==640 or x==0 and y==640 or x==160 and y==640 or x==240 and y==640 or x==320 and y==640 or x==320 and y==720 or x==320 and y==560 or x==400 and y==560 or x==480 and y==560 or x==560 and y==560 or x==560 and y==640 or x==560 and y==720 or x==160 and y==480 or x==240 and y==480 or x==480 and y==480:
        okno.fill(pygame.Color('black'))
        [(pygame.draw.rect(okno, pygame.Color('green'), (x, y, size, size)))]
        pygame.draw.rect(okno, pygame.Color('white'), (0, 240, 160, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (240, 80, 80, 320))
        pygame.draw.rect(okno, pygame.Color('white'), (80, 0, 80, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (160, 400, 160, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (0, 400, 80, 240))
        pygame.draw.rect(okno, pygame.Color('white'), (320, 400, 320, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (160, 560, 160, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (0, 720, 320, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (400, 640, 160, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (640, 320, 80, 480))
        pygame.draw.rect(okno, pygame.Color('white'), (400, 0, 240, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (720, 0, 80, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (400, 160, 160, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (560, 160, 240, 80))
        pygame.draw.rect(okno, pygame.Color('red'), (720, 720, 80, 80))
        snake.append((x, y))
        print(x,y)
        snake = snake[-lenght:]
        pygame.display.flip()
        time.tick(speed)
        for event in pygame.event.get():
                if event.type == pygame.quit:
                    exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
                dx,dy=0,-1
                x += dx * size
                y += dy * size
        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
                dx, dy = 0, 1
                x += dx * size
                y += dy * size
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
                dx, dy = 1, 0
                x += dx * size
                y += dy * size
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
                dx, dy = -1,0
                x += dx * size
                y += dy * size
        key = pygame.key.get_pressed()
elif lvl==2:
    while x==0 and y==0 or x==0 and y==80 or x==0 and y==160 or x==0 and y==240 or x==0 and y==320 or x==0 and y==400 or x==0 and y==480 or x==80 and y==480 or x==80 and y==480 or x==160 and y==480 or x==160 and y==400 or x==160 and y==320 or x==160 and y==560 or x==160 and y==640 or x==160 and y==720 or x==80 and y==720 or x==240 and y==480 or x==320 and y==480 or x==320 and y==560 or x==400 and y==560 or x==480 and y==560 or x==400 and y==640 or x==400 and y==720 or x==320 and y==720 or x==480 and y==720 or x==480 and y==480 or x==560 and y==480 or x==640 and y==560 or x==640 and y==640:
        okno.fill(pygame.Color('black'))
        [(pygame.draw.rect(okno, pygame.Color('green'), (x, y, size, size)))]
        pygame.draw.rect(okno, pygame.Color('white'), (80, 0, 80, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (160, 240, 80, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (240, 80, 80, 240))
        pygame.draw.rect(okno, pygame.Color('white'), (80, 240, 80, 240))
        pygame.draw.rect(okno, pygame.Color('white'), (0, 560, 160, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (0, 720, 80, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (240, 560, 80, 240))
        pygame.draw.rect(okno, pygame.Color('white'), (0, 720, 80, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (320, 640, 80, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (400, 240, 80, 320))
        pygame.draw.rect(okno, pygame.Color('white'), (240, 400, 480, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (400, 0, 80, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (560, 80, 80, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (560, 240, 240, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (720, 80, 80, 160))
        pygame.draw.rect(okno, pygame.Color('white'), (560, 560, 80, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (480, 640, 240, 80))
        pygame.draw.rect(okno, pygame.Color('white'), (640, 720, 80, 80))
        pygame.draw.rect(okno, pygame.Color('red'), (560, 720, 80, 80))
        snake.append((x, y))
        print(x, y)
        snake = snake[-lenght:]
        pygame.display.flip()
        time.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.quit:
                exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            dx, dy = 0, -1
            x += dx * size
            y += dy * size
        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            dx, dy = 0, 1
            x += dx * size
            y += dy * size
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            dx, dy = 1, 0
            x += dx * size
            y += dy * size
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx, dy = -1, 0
            x += dx * size
            y += dy * size
        key = pygame.key.get_pressed()