import pygame as pg
import random as rd

# Bubble Sort

WIDTH = 1300
HEIGHT = 700

nums = []
solved_arr = []
n = 300

for i in range(n):
    nums.append((i+1)*2)
    solved_arr.append((i+1)*2)


rd.shuffle(nums)

pg.init()
win = pg.display.set_mode((WIDTH, HEIGHT))
solved = False
run = True
row = 0

myfont = pg.font.SysFont('Comic Sans MS', 40)
textsurface = myfont.render('Bubble Sort Algorithm Basic Visualizer', False, (0, 0, 0))

while run:
    pg.time.delay(50)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    win.fill((255, 255, 255))
    win.blit(textsurface, (20, 20))
    for barHeight in range(len(nums)):
        pg.draw.rect(win, (255, 0, 0), ((barHeight*4)+20, HEIGHT-nums[barHeight], 3, HEIGHT))

    if row == len(nums):
        row = 0

    if solved == False:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                current = nums[i]
                nums[i] = nums[i-1]
                nums[i - 1] = current


        row +=1

    if nums == solved_arr:
        solved = True

    pg.display.update()