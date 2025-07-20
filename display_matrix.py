import sys
import pygame as pg

#この行列を好きなように変えてください。

matrix = [[0, 1, 1],
          [0, 1, 0],
          [0, 1, 0]]

def matrix_size(matrix, squaresize) -> tuple:

    x = 0
    y = len(matrix)

    for row in matrix:
        if len(row) > x:
            x = len(row)

    return (x*squaresize[0], y*squaresize[1])

def create_Square(screen, color, x, y, squaresize):
    pg.draw.rect(screen, color, [x, y, squaresize[0], squaresize[1]])

def scan_matrix(screen, matrix, squaresize):

    y = 0
    for row in matrix:
        x = 0
        for num in row:
            if num != 0:

                create_Square(screen, (255, 255, 255), x, y, squaresize)
            else:
                create_Square(screen, (0, 0, 0), x, y, squaresize)
            x += squaresize[0]
        y += squaresize[1]

def main():
    pg.init()

    square_size = (50, 50)

    screen_size = matrix_size(matrix, square_size)
    screen = pg.display.set_mode(screen_size)

    while True:

        screen.fill((100, 100, 100))
        scan_matrix(screen, matrix, square_size)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print('ended')
                pg.quit()
                sys.exit()

        pg.display.update()

if __name__ == '__main__':
    main()