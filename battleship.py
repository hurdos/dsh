#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math
from random import randint
from pyray import *

class Ship:
    def __init__(self, size: int):
        self.size = size
        self.coords = []
        self.horizontal = randint(0, 1)

    def getSize(self):
        return self.size
    
    def genCoords(self) -> list:
        self.coords = []
        x = randint(0, 9)
        left = 1 if x >= 7 else 0
        y = randint(0, 9)
        up = 1 if y >= 7 else 0

        for i in range(1, self.size + 1):
            self.coords.append((x, y))
            if self.horizontal:
                if left:
                    x -= 1
                else:
                    x += 1
            else:
                if up:
                    y -= 1
                else:
                    y += 1
        return self.coords
    
class MapField:
    def __init__(self):
        self.matrix = []
        for i in range(10):
            row = [0] * 10
            self.matrix.append(row)

    def getMatrix(self):
        return self.matrix

    def isBusy(self, x, y) -> bool:
        a = x if x == 0 else x - 1
        b = x if x == 9 else x + 1
        c = y if y == 0 else y - 1
        d = y if y == 9 else y + 1
        for i in range(a, b + 1):
            for j in range(c, d + 1):
                if self.matrix[i][j] != 0:
                    return True
        return False

    def addShip(self, ship: Ship):
        c = 1
        while (c < 100):
            coords = ship.genCoords()

            isBusy = False
            # if c > 1:
            #     print(coords[0])
            for coord in coords:
                (x, y) = coord
                isBusy = self.isBusy(x, y)
                if isBusy:
                    break

            if isBusy:
                # print(f"isBusy Count: {c}")
                c += 1
                continue

            for coord in coords:
                (x, y) = coord
                self.matrix[x][y] = ship.getSize()

            print(f"Added ship [{ship.getSize()}] attemps {c}")
            return 1
        print(f"Can not add ship [{ship.getSize()}]")
        return 0


def genMatrix():
    mf = MapField()

    # add 1 crusader
    mf.addShip(Ship(4))

    # add 2 destroyers
    mf.addShip(Ship(3))
    mf.addShip(Ship(3))

    # add 3 frigates
    mf.addShip(Ship(2))
    mf.addShip(Ship(2))
    mf.addShip(Ship(2))

    # add 4 corvettes
    mf.addShip(Ship(1))
    mf.addShip(Ship(1))
    mf.addShip(Ship(1))
    mf.addShip(Ship(1))

    return mf.getMatrix()

def main(args):
    map1 = genMatrix()
    for row in map1:
        print(' '.join(map(str, row)))

    print('-------------------------------------------------------')

    map2 = genMatrix()
    for row in map2:
        print(' '.join(map(str, row)))

    # v = Vector2;
    # set_config_flags(ConfigFlags.FLAG_VSYNC_HINT)

    # init_window(800, 450, "Привет RayLib!")

    # while not window_should_close():
    #     begin_drawing()
    #     clear_background(RAYWHITE)

    #     draw_fps(5, 5)
    #     end_drawing()
    # close_window()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))