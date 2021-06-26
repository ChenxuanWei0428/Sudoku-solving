#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" This is the gui implemecation of the Sudoku solver "

__author__ = "Austin Wei"

import Board, pygame
from pygame.locals import *

from sys import exit

pygame.init()
title_font = pygame.font.SysFont("arial", 20)
Bottom_font = pygame.font.SysFont("arial", 15)

title_text = title_font.render("Welcome to Austin's Sudoku Solver", True, (0, 0, 0))
Strat_text = Bottom_font.render("Start", True, (0, 0, 0))
Quit_text = Bottom_font.render("Quit", True, (0, 0, 0))

# initialize screen
screen = pygame.display.set_mode((1400, 1400), 0, 32)
pygame.display.set_caption("Sudoku Solver")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    python.draw.rect
    pygame.display.update()
    