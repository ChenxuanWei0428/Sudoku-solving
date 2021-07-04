#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" This is the gui implemecation of the Sudoku solver "

__author__ = "Austin Wei"

import Board, tkinter, Temp_board, time

class GUI :

    def __init__(self):
        self.main_board = tkinter.Tk()

        # the two frame, one is for the board, other for the bottoms
        self.board_frame = tkinter.Frame(self.main_board, width = 200, height = 200)
        self.bottom_frame = tkinter.Frame(self.main_board)

        #edit main_board
        self.main_board.title("Sudoku Solver")
        self.main_board.geometry('750x700')


        # the board that is showed in the game
        self.boardset = Temp_board.next()
        self.current_board = self.boardset()
        self.level_board = Board.Board(self.current_board)

        # this is a 2d list of tkinter.Entry
        self.sudoku_entry = []

        # the two frame, one is for the board, other for the bottoms
        self.board_frame = tkinter.Frame(self.main_board, width = 200, height = 200)
        bottom_frame = tkinter.Frame(self.main_board)

        # the status_text
        self.status = tkinter.StringVar()
        self.status.set("Welcome to Sudoku Game")
        self.status_text = tkinter.Label(self.bottom_frame, textvariable=self.status)

        self.submit_botton = tkinter.Button(self.bottom_frame, text = "submit!", command = (lambda: self.submit()), height = 1, width = 1)
        self.solve_botton = tkinter.Button(self.bottom_frame, text = "solve!", command = (lambda: self.solve()), height = 1, width = 1)


    '''    
    Purpose input_level() input the level_board to the entrys
    effect: modify sudoku_entry
    '''
    def input_level(self,):
        l = len(self.sudoku_entry)
        for row in range(l):
            for cell in range(l):
                if (self.level_board.board[row][cell] != 0):
                    self.sudoku_entry[row][cell].insert(0, self.level_board.board[row][cell])
        self.level_board.solve()


    '''
    Purpose: solve() is a tkinter command for solve the sudoku, show the solution the input the next level
    effect: edit the entrys and displace the solved board
    '''
    def solve(self):
        l = len(self.level_board.board)
        for row in range(l):
            for entry in range(l):
                self.sudoku_entry[row][entry].delete(0, 'end')
                self.sudoku_entry[row][entry].insert(0, self.level_board.board[row][entry])

        self.status.set("The solution is presented")
        # need to learn why this is not working
        #time.sleep(5)
        self.next_level()


    ''' 
    Purpose: submit() is a tkinter command to check if the answer matches the given answer
    effect: edit the entrys and indicate weather it is true or not
    '''
    def submit(self):
        correct = True
        empty = False
        l = len(self.level_board.board)
        for row in range(l):
            for entry in range(l):
                # If it is not blank and it does not match the solution board, remove it
                if (len(self.sudoku_entry[row][entry].get()) != 0 and int(self.sudoku_entry[row][entry].get()) != self.level_board.board[row][entry]):
                    correct = False
                    self.sudoku_entry[row][entry].delete(0, 'end')
                elif (len(self.sudoku_entry[row][entry].get()) == 0 ):
                    empty = True
        
        if not correct:
            self.status.set("Please try again!")
        elif (empty):
            self.status.set("You still have empty space to fill!")
        else:
            self.status.set("Great job!")


    '''
    Purpose: Put the game into next level
    effect: modify entrys
    '''
    def next_level(self):
        l = len(self.sudoku_entry)
        self.status.set("Welcome to next level")
        for row in range(l):
            for entry in range(l):
                self.sudoku_entry[row][entry].delete(0, 'end')
        self.current_board = self.boardset()
        self.level_board = Board.Board(self.current_board)
        self.input_level()

     
    '''
    Purpose: init_row(board_row) Return a 1D array of entry in tk which include one row of the board
    Contract: list[] -> list[]
    '''
    def init_row (self, row_len):
        temp_row = []
        for i in range(row_len):
            temp_row.append(tkinter.Entry(self.board_frame, font = 10, width = 3))
        return temp_row


    '''
    Purpose: input_board(board) Modify the 2D array of entry to make a entry of the board
    effect: modify sudoku_entry
    Contarct: Board -> 
    '''
    def init_entry_array (self):
        l = self.level_board.length
        for board_row in range(l):
            self.sudoku_entry.append(self.init_row(l))


    '''
    Purpose: add_to_screen(loe) Put everything is the list of entry to the screen
    effect: modify the main_board
    '''
    def add_to_screen(self):
        l = len(self.sudoku_entry)
        for row in range(l):
            for entry in range(l):
                self.sudoku_entry[row][entry].grid(row = row, column = entry, padx = 10, pady = 10, ipadx = 10, ipady = 10)

    
    '''
    Purpose: add_solve_botton_to_screen() add the solve botton to the screen
    effect: modify main_board()
    '''
    def add_solve_botton_to_screen(self):
        self.solve_botton.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 10, ipady = 10)


    '''   
    Purpsoe: add_submit button to screen() add the submit botton for user to the screen
    effect: modify main_board()
    '''
    def add_submit_botton_to_screen(self):
        self.submit_botton.grid(row = 1, column = 2, padx = 10, pady = 10, ipadx = 20, ipady = 10)


    '''
    Purpose: add_status_text_to_screen() add a status bar to the screen, shows, weather you win, or still need to try or solved it
    effect: modify main_board()
    '''
    def add_status_text_to_screen(self):
        self.status_text.grid(row = 1, column = 3, padx = 10, pady = 10, ipadx = 10, ipady = 10)


    #start the Sudolu solver program
    def start(self):
        #init the game
        self.init_entry()
        self.init_game()


        self.input_level()
        self.main_board.mainloop()


    '''
    Purpose: initlize the entry and ready for inputting level
    effect: modify entry
    '''
    def init_entry(self):
        self.init_entry_array()
        self.add_to_screen()
        self.board_frame.pack()


    '''
    Purpose: initlize the bottom and status bar
    effect: modify entry
    '''
    def init_game(self):
        self.add_solve_botton_to_screen()
        self.add_submit_botton_to_screen()
        self.add_status_text_to_screen()
        self.bottom_frame.pack()
