#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" This is the data base for the sudoku solver , contain different template for Sudoku"

__author__ = "Austin Wei"



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

b1 = [
    [8, 6, 1, 7, 0, 4, 3, 5, 2],
    [3, 5, 2, 1, 6, 8, 7, 4, 9],
    [4, 9, 7, 2, 5, 3, 1, 0, 6],
    [2, 1, 0, 9, 7, 5, 6, 3, 4],
    [6, 7, 5, 3, 4, 1, 9, 2, 8],
    [9, 3, 4, 6, 8, 0, 5, 1, 7],
    [5, 2, 6, 8, 1, 9, 0, 7, 3],
    [7, 4, 0, 5, 2, 6, 8, 9, 1],
    [1, 8, 9, 4, 3, 7, 2, 6, 5]
]

level = [b]
