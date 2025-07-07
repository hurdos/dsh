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

    def addShip(self, ship: Ship):
        c = 1
        while (c < 10):
            coords = ship.genCoords()

            isBusy = False
            for coord in coords:
                (x, y) = coord
                if self.matrix[x][y] != 0:
                    isBusy = True
                    break

            if isBusy:
                print(f"isBusy Count: {c}")
                c += 1
                continue

            for coord in coords:
                (x, y) = coord
                self.matrix[x][y] = ship.getSize()

            print('Added ship [' + str(ship.getSize()) + ']')
            return 1
        print('Can not add ship [' + str(ship.getSize()) + ']')
        return 0


def genMatrix():
    map1 = MapField()

    # add 1 crusader
    map1.addShip(Ship(4))
    # add 2 destroyers
    map1.addShip(Ship(3))
    map1.addShip(Ship(3))
    # add 3 frigates
    map1.addShip(Ship(2))
    map1.addShip(Ship(2))
    map1.addShip(Ship(2))

    # add 4 corvettes
    map1.addShip(Ship(1))
    map1.addShip(Ship(1))
    map1.addShip(Ship(1))
    map1.addShip(Ship(1))

    return map1.getMatrix()

def main(args):
    matrix = genMatrix()
    for row in matrix:
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