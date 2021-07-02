#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" This is the board for a soduku solver "

__author__ = "Austin Wei"


class Board(object):
    __slots__ = ("_board", "_length")


    '''
    This is the contructor of the board
    Arguments: Board = int[][]
    attributes: _board = int[][]
                _length = int
    '''
    def __init__(self, board):
        self._board = board
        self._length = len(board)


    '''
    Purpose: Board.get_length() return the length of the board
    Contract: -> int
    '''
    @property
    def length(self):
        return self._length


    '''
    Purpose: Board.get_board() return the board in 2D array
    Contract: -> int[][]
    '''
    @property
    def board(self):
        return self._board


    '''
    Purpose: Board.set_cell(row, col, val) set the cell value at row, col to val
    Effect: modify the selected cell 
    '''
    def set_cell(self, row, col, val):
        self._board[row][col] = val


    '''
    Purpose: Board.set_length(length) set the length of the board
    Effect: modify Board._length
    '''
    @length.setter
    def length(self, length):
        if 0 < length:
            self._length = length
        else:
            raise ValueError('Invalid Length')
  

    '''
    Purpose: Board.check_valid(row, col, num) check if a number can be written down validly in a position
             row and col are the row and column position we are looking for
             num is the number you are trying
             Return a Boolean Value
    Contract: int, int, int -> bool
    '''
    def check_valid(self, row, col, num):
        # check the row:
        for i in range(self.length):
            if (self.board[row][i] == num):
                return False

        # check the column:
        for i in range(self.length):
            if (self.board[i][col] == num):
                return False

        #check each individual box
        '''
        br = block row
        bc = block column
        '''
        for br in range(row//3 * 3, (row//3 + 1) * 3):
            for bc in range(col//3 * 3, (col//3 + 1) * 3):
                if (self.board[br][bc] == num):
                    return False
        
        #if there are no conflict in row, column and cell, then it is valid
        return True


    '''
    Purpose: Board.find_empty() return the first empty cell 
    Contract: -> [row, col]
    '''
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if (self.board[row][col] == 0):
                    return [row, col]
        # if the board is full
        return None


    '''
    Purpose: step_by_step() solve one step of the Sudoku, for present step by step solution
    effect: modify board
    '''
    def step_by_step(self):
            cell = self.find_empty()
            # if the board is full
            if cell is None:
                return self
            row = cell[0]
            col = cell[1]
            
            # Try 1 - 9 on the empty cell
            for val in range(1, 10):
                #if it is a valid number
                if self.check_valid(row, col, val):
                    # set it to the valid number
                    self.set_cell(row, col, val)
                    # try to solve the next sudoku this the value set
                    temp_sol = self.step_by_step()
                    # if you find a solution, just return it
                    if temp_sol is not None:
                        return temp_sol       
                    # Important step: back track to set it back to 0, if the try we have did not work
                    self.set_cell(row, col, 0)

            # If no solution, return None to indicate that
            return None 


    '''
    Purpose: Board.solve() Use backtrack to solve the soduku by modify the existing board
             if there is no solution, will return the board with most of the part solved
    effect modify board
    '''
    def solve(self):

        # step_by_step(board) try to solve the board use backtrack recursion, while modify the board
        result = self.step_by_step()
                  



    '''
    Purpose: Board.print_board() print the board in a good way
    Effect: Produce Outputs
    '''
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
                    val = self.board[row][col]

                    if (val != 0):
                        s = s + str(val) # print the value
                    else :
                        s = s + " "# If it is zero (means blank), then print nothing, but use space to format

                    if (col % 3 == 2):
                        s = s + " |" # Vertical line seperate the cell
                print(s) # Print each line
            print(break_line) # Print horizontal break line between cells
