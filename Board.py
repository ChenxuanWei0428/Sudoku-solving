#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" This is the board for a soduku solver "

__author__ = "Austin Wei"


class Board(object):

    '''
    This is the contructor of the board
    Arguments: Board = int[][]
    attributes: _board = int[][]
                _length = int
    '''
    def __init__(self, board):
        self._board = board
        self._length = len(board)


    # get_length() return the length of the board
    #  -> int
    def get_length(self):
        return self._length


    # get_board() return the board in 2D array
    #  -> int[][]
    def get_board(self):
        return self._board


    # set_cell(row, col, val) set the cell value at row, col to val
    # int, int, int -> 
    def set_cell(self, row, col, val):
        self._board[row][col] = val


    # set_length(length) set the length of the board
    # int ->
    def set_length(self, length):
        if 0 < length:
            self._length = length
        else:
            raise ValueError('Invalid Length')
  

    # check_valid(row, col, num) check if a number can be written down validly in a position
    '''
    row and col are the row and column position we are looking for
    num is the number you are trying
    Return a Boolean Value
    '''
    # int, int, int -> bool
    def check_valid(self, row, col, num):
        # check the row:
        for i in range(self.get_length()):
            if (self.get_board()[row][i] == num):
                return False

        # check the column:
        for i in range(self.get_length()):
            if (self.get_board()[i][col] == num):
                return False

        #check each individual box
        '''
        br = block row
        bc = block column
        '''
        for br in range(row//3 * 3, (row//3 + 1) * 3):
            for bc in range(col//3 * 3, (col//3 + 1) * 3):
                if (self.get_board()[br][bc] == num):
                    return False
        
        #if there are no conflict in row, column and cell, then it is valid
        return True


    # find_empty() return the first empty cell 
    #  -> [row, col]
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if (self.get_board()[row][col] == 0):
                    return [row, col]
        # if the board is full
        return None

    # solve() Use backtrack to solve the soduku by modify the existing board
    # -> Board
    def solve(self):

        # solve_board(board) try to solve the board use backtrack recursion, while modify the board
        def solve_board(b):
            cell = b.find_empty()
            # if the board is full
            if cell is None:
                return b
            row = cell[0]
            col = cell[1]
            
            # Try 1 - 9 on the empty cell
            for val in range(1, 10):
                #if it is a valid number
                if b.check_valid(row, col, val):
                    # set it to the valid number
                    b.set_cell(row, col, val)
                    # try to solve the next sudoku this the value set
                    temp_sol = solve_board(b)
                    # if you find a solution, just return it
                    if temp_sol is not None:
                        return temp_sol       
                    # Important step: back track to set it back to 0, if the try we have did not work
                    b.set_cell(row, col, 0)

            # If no solution, return None to indicate that
            return None 
        
        result = solve_board(self)
        if result is None:
            print("No solution")
        else:
            print("There is a solution!")
        return self
    
    # print_board() print the board in a good way
    # effect: Produce Outputs
    def print_board(self):
        #this is the line at the top and bottom of the board, and for seperate the cells
        break_line = "-------------------------"
        
        print(break_line)
        #create the content
        for block_row in range(3):
            for row in range(block_row * 3, (block_row + 1) * 3):
                s = "|" # include the begin bar
                for col in range(9):
                    s = s + " "
                    val = self.get_board()[row][col]

                    if (val != 0):
                        s = s + str(val) # print the value
                    else :
                        s = s + " "# If it is zero (means blank), then print nothing, but use space to format

                    if (col % 3 == 2):
                        s = s + " |" # Vertical line seperate the cell
                print(s) # Print each line
            print(break_line) # Print horizontal break line between cells
