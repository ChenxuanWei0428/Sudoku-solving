#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" This is the board for the landmine game "

__author__ = "Austin Wei"


class Board(object):

    _difficult_level = {'Easy': (5, 5), 'Medium': (10, 10), 'Hard': (20, 20)}
    _oppo_d = {(5, 5): 'Easy', (10, 10): 'Medium', (20, 20): 'Hard'}
    
    #Constructor of the class Board
    def __init__(self, length=5, width=5):
        self._length = length
        self._width = width
        self._difficulty = "customize"
        self._check_diff()
        
    #Get attribute length
    def get_length(self):
        return self._length

    #Get attribute width
    def get_width(self):
        return self._width

    #Get attribute width
    def get_difficulty(self):
        return self._difficulty

    #check which difficult it is with current dimension
    def _check_diff(self):
        dim = (self._length, self._width)
        if self._oppo_d.__contains__(dim):
            self._difficulty = self._oppo_d.get(dim)
        else:
            self._difficulty = "Customized"
    
    #Set attribute length
    def set_length(self, length):
        l = int(length)
        if 0 < l:
            self._length = l
            self._check_diff()
        else:
            raise ValueError('Invalid Length')

    #Set attribute width
    def set_width(self, width):
        w = int(width)
        if 0 < w:
            self._width = w
            self._check_diff()
        else:
            raise ValueError('Invalid Width')
    
    #Set difficult 
    def set_difficulty(self, diff):
        if self._difficult_level.__contains__(diff):
            self._length, self._width =self._difficult_level.get(diff)
            self._difficulty = diff
        else:
            raise ValueError('Invalid Difficulty')
            
        
        
