import random
import pygame as pg

pg.init()

WIDTH = 800
HEIGHT = 552

white = (255, 255, 255)
black = (0, 0, 0)

font1 = pg.font.SysFont(None, 40)
font2 = pg.font.SysFont(None, 70)
font3 = pg.font.SysFont(None, 55)

win = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Pong")


def drawPause(lh, rh, bpos):
    run = True
    fx = WIDTH / 2 -155
    fy = HEIGHT/2 - 100
    fw = 310
    fh = 70

    while run:

        pg.time.delay(100)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                return False
                break

        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN]:
            if fy < 286:
                fy += 110
                fx += 30
                fw -= 70

        if keys[pg.K_UP]:
            if fy > 176:
                fy -= 110
                fx -= 30
                fw += 70

        if keys[pg.K_SPACE] and fy == 286:
            run = False
            return False
        if keys[pg.K_SPACE] and fy == 176:
            run = False
            return True

        pg.draw.rect(win, white, (0, lh, 20, 80))
        pg.draw.rect(win, white, (780, rh, 20, 80))
        pg.draw.circle(win, white, bpos, 15, 15)

        pg.draw.rect(win, white, (WIDTH / 2 - 205, HEIGHT / 2 - 125, 410, 250))
        pg.draw.rect(win, black, (WIDTH / 2 - 200, HEIGHT / 2 - 120, 400, 240))
        frame(fx, fy, fw, fh)
        text2 = font3.render('Resume Game', True, white)
        win.blit(text2, (WIDTH / 2-130, HEIGHT/2-80))

        text2 = font3.render('Exit Game', True, white)
        win.blit(text2, (WIDTH / 2-100, HEIGHT/2+30))



        pg.display.update()


def frame(x, y, w, h):
    pg.draw.rect(win, white, (x, y, w, h))
    pg.draw.rect(win, black, (x+5, y+5, w-10, h-10))


def home():
    run = True
    fx = 300
    fy = 180
    fw = 160
    fh = 85

    bx = 400
    by = random.randint(50, 450)

    bdir = random.randint(0, 2)

    bydir = bdir
    bxdir = bdir

    while run:
        pg.time.delay(10)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            if fy >= 200:
                fy = fy - 120
                fx = 300
                fw = fw + 40
                fh = 85

        if keys[pg.K_DOWN]:
            if fy < 300:
                fy = fy + 120
                fx = 320
                fw = fw - 40
                fh = 75

        if keys[pg.K_SPACE]:
            if fy == 180:
                run = False
                game()

            if fy == 300:
                run = False
                pg.quit()
                break

        win.fill(black)
        frame(fx, fy, fw, fh)
        text1 = font2.render('Play', True, white)
        win.blit(text1, (330, 200))
        text2 = font3.render('Quit', True, white)
        win.blit(text2, (340, 320))

        if by+15 >= 552:
            bydir = 0

        if by-15 <= 0:
            bydir = 1

        if bx+15 >= 800:
            bxdir = 0

        if bx-15 <= 0:
            bxdir = 1

        if bydir < 1:
            by = by - 2

        if bydir > 0:
            by = by + 2

        if bxdir < 1:
            bx = bx - 2

        if bxdir > 0:
            bx = bx + 2

        pg.draw.circle(win, white, (bx, by), 15, 15)

        pg.display.update()


def game():
    yl = 200
    yr = 200

    lscore = 0
    rscore = 0

    #bang = 4/3
    bx = 400
    by = random.randint(50, 450)

    bdir = random.randint(0, 2)

    bydir = bdir
    bxdir = bdir

    time = 0
    timer = 0
    ys = 5
    bs = 2
    run = True
    lenth = 80
    while run:
        pg.time.delay(20)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            if yl >= 0:
                yl -= ys

        if keys[pg.K_s]:
            if yl + lenth <= 500:
                yl += ys

        if keys[pg.K_UP]:
            if yr >= 0:
                yr -= ys

        if keys[pg.K_DOWN]:
            if yr + lenth <= 500:
                yr += ys

        if keys[pg.K_ESCAPE]:
            run = drawPause(yl, yr, (bx, by))

        win.fill(black)
        pg.draw.rect(win, white, (399, 0, 2, HEIGHT-48)) # line
        pg.draw.rect(win, white, (0, 504, WIDTH, 2))  # line

        pg.draw.rect(win, white, (0, yl, 20, lenth))
        pg.draw.rect(win, white, (780, yr, 20, lenth))



        if yr <= by <= yr+lenth:
            if bx+15+20 >= 800:
                bxdir = 0

        if yl <= by <= yl+lenth:
            if bx-15-20 <= 0:
                bxdir = 1

        if bx <= 0:
            bx = 400
            by = random.randint(50, 450)
            bdir = random.randint(0, 2)

            bydir = bdir
            bxdir = bdir
            rscore = rscore+1

        if bx >= 800:
            bx = 400
            by = random.randint(50, 450)
            bdir = random.randint(0, 2)

            bydir = bdir
            bxdir = bdir
            lscore = lscore+1

        if by+15 >= 500:
            bydir = 0

        if by-15 <= 0:
            bydir = 1

        if bydir < 1:
            by = by - bs

        if bydir > 0:
            by = by + bs

        if bxdir < 1:
            bx = bx - bs

        if bxdir > 0:
            bx = bx + bs

        pg.draw.circle(win, white, (bx, by), 15, 15)

        text1 = font1.render(str(lscore), True, white)
        text2 = font1.render(str(rscore), True, white)
        win.blit(text1, (100, 520))
        win.blit(text2, (700, 520))
        text5 = font1.render(str(time), True, white)
        win.blit(text5, (395, 520))
        pg.display.update()
        timer = timer + 1
        if timer == 3000:
            timer = 0
            bs = bs + 1

        if timer%50 == 0:
            time = time + 1



home()

pg.quit()