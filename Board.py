#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" This is the board for a soduku solver "

__author__ = "Austin Wei"


class Board(object):

    #Constructor of the class Board
    # board is a 2d array
    # the topleft corner is consider as(0, 0)
    # the bottom right is consider as (8, 8)
    # 0 on the suduku means it is a empty block
    def __init__(self, board):
        self._board = board
        self._length = len(board)
        
    #Get attribute length
    def get_length(self):
        return self._length

    def get_board(self):
        return self._board

    #Set attribute length
    def set_length(self, length):
        if 0 < length:
            self._length = length
        else:
            raise ValueError('Invalid Length')
  
    #check if a number can be written down validly in a position
    def check_valid(self, x, y, num):
        # check horizontal:
        for w in range(self.get_length()):
            if (self.get_board()[y][w] == num):
                return False

        # check vertical:
        for l in range(self.get_length()):
            if (self.get_board()[l][x] == num):
                return False

        #check each individual box
        for sl in range(x//3 * 3, (x//3 + 1) * 3):
            for sw in range(y//3 * 3, (y//3 + 1) * 3):
                if (self.get_board()[sw][sl] == num):
                    return False
        
        #if there are no conflict, then it is valid
        return True

    #use backtrack to solve the soduku
    def solve(self):
        pass
