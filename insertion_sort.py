import pygame as pg
import random as rd

# Insertion Sort Algorithm

WIDTH = 1300
HEIGHT = 700

nums = []
solved_arr = []
n = 300

for i in range(n):
    nums.append((i + 1) * 2)
    solved_arr.append((i + 1) * 2)

rd.shuffle(nums)

pg.init()
win = pg.display.set_mode((WIDTH, HEIGHT))

myfont = pg.font.SysFont('Comic Sans MS', 40)
textsurface = myfont.render('Insertion Sort Algorithm Basic Visualizer', False, (0, 0, 0))
solved = False


run = True
row = 1
maxnum = 0
while run:
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    win.fill((255, 255, 255))
    win.blit(textsurface, (20, 20))
    for barHeight in range(len(nums)):
        pg.draw.rect(win, (255, 0, 0), ((barHeight * 4)+10, HEIGHT - nums[barHeight], 3, HEIGHT))

    if solved == False:
        if row == len(nums):
            row = 1

        current = nums[row]
        j = row-1
        pg.draw.rect(win, (0, 0, 255), ((row * 4)+10, HEIGHT - current, 3, HEIGHT))
        while j >= 0 and nums[j] > current:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            pg.time.delay(10)
            pg.draw.rect(win, (0, 255, 0), ((j * 4)+10, HEIGHT - nums[j], 3, HEIGHT))
            pg.display.update()
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = current
        row += 1

    if nums == solved_arr:
        solved = True

    pg.display.update()

pg.quit()