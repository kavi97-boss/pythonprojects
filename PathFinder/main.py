import random as rd
import pygame as pg
from queue import PriorityQueue as PQ


WIDTH = 800
WIN = pg.display.set_mode((WIDTH, WIDTH))
pg.display.set_caption("Pathfinding Algo Visualizer")


CLOSED = (88, 201, 222)
GREEN = (94, 214, 196)
WHITE = (255, 255, 255)
BARRIER = (15, 46, 64)
GREY = (128, 128, 128)
START = (255, 165, 0)
PATH = (255, 255, 95)
END = (70, 114, 196)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return (self.row, self.col)

    def is_closed(self):
        return self.color == CLOSED

    def is_open(self):
        return self.color == GREEN

    def is_obstacle(self):
        return self.color == BARRIER

    def is_start(self):
        return self.color == START

    def is_end(self):
        return self.color == END

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = START

    def make_closed(self):
        self.color = CLOSED

    def make_open(self):
        self.color = GREEN

    def make_obstacle(self):
        self.color = BARRIER

    def make_end(self):
        self.color = END

    def make_path(self):
        self.color = PATH

    def draw(self, win):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []
        # down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_obstacle():
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle():  # up
            self.neighbours.append(grid[self.row - 1][self.col])

        # right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_obstacle():
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.row > 0 and not grid[self.row][self.col - 1].is_obstacle():  # left
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2)+abs(y1-y2)


def algo(draw, grid, start, end):
    count = 0
    open_set = PQ()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True
        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + \
                    h(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
        draw()

        if current != start:
            current.make_closed()
    return False


def make_grid(rows, width):
    grid = []
    gap = width//rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            if i == 0 or j == 0 or i == rows-1 or j == rows-1:
                spot.make_obstacle()

            grid[i].append(spot)
    return grid


def draw_grid(win, rows, width):
    gap = width//rows
    for i in range(rows):
        pg.draw.line(win, GREY, (0, i*gap), (width, i*gap))
    for i in range(rows):
        pg.draw.line(win, GREY, (i*gap, 0), (i*gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pg.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y//gap
    col = x//gap

    return row, col


def total_spots(grid):
    c = 0
    for row in grid:
        for sp in row:
            c += 1

    return c


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    all_spots = total_spots(grid)
    print(all_spots)
    random_generated_spots = 0.4

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, WIDTH)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if started:
                continue
            if pg.mouse.get_pressed()[0]:  # left click
                pos = pg.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_obstacle()

            elif pg.mouse.get_pressed()[2]:  # right click
                pos = pg.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()

                if spot == start:
                    start = None
                if spot == end:
                    end = None
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not started:
                    started = True
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    started = not algo(lambda: draw(
                        win, grid, ROWS, width), grid, start, end)
                if event.key == pg.K_c and not started:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pg.quit()


main(WIN, WIDTH)
