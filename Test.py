#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" THis is the test clinet for the landmine game "

__author__ = "Austin Wei"

import Board, check

b = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]

board = Board.Board(b)

print(board.check_valid(4, 8, 1))
print(board.check_valid(4, 8, 2))
print(board.check_valid(4, 8, 3))
print(board.check_valid(4, 8, 4))
print(board.check_valid(4, 8, 5))
print(board.check_valid(4, 8, 6))
print(board.check_valid(4, 8, 7))
print(board.check_valid(4, 8, 8))
print(board.check_valid(4, 8, 9))