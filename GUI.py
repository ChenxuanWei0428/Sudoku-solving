#!/usr/bin/env python3
# -*- coding: utf-8 -*-

" This is the gui implemecation of the Sudoku solver "

__author__ = "Austin Wei"

import Board, tkinter, Temp_board

main_board = tkinter.Tk()
main_board.title("Sudoku Solver")
main_board.geometry('750x700')

current_board = Temp_board.b

# the board that is showed in the game
init_board = Board.Board(current_board)

# this is a 2d list of tkinter.Entry
sudoku_board = []


'''
Purpose: input_row(board_row) Return a 1D array of entry in tk which include one row of the board
Contract: list[] -> list[]
'''
def input_row (board_row):
    temp_row = []
    l = len(board_row)
    for i in range(l):
        temp_row.append(tkinter.Entry(main_board, font = 10, width = 3))
        if board_row[i] != 0:
            temp_row[i].insert(0, board_row[i])
    return temp_row


'''
Purpose: input_board(board) Modify the 2D array of entry to make a entry of the board
effect: modify sudoku_board
Contarct: Board -> 
'''
def input_board (board):
    for board_row in board.board:
        sudoku_board.append(input_row(board_row))


'''
Purpose: add_to_screen(loe) Put everything is the list of entry to the screen
effect: modify the main_board
'''
def add_to_screen(loe):
    l = len(loe)
    for row in range(l):
        for entry in range(l):
            sudoku_board[row][entry].grid(row = row, column = entry, padx = 10, pady = 10, ipadx = 10, ipady = 10)


'''
Purpose: solve() is a tkinter command for solve the sudoku
effect: edit the entrys and displace the solved board
'''
def solve():
    l = len(init_board.board)
    for row in range(l):
        for entry in range(l):
            sudoku_board[row][entry].delete(0, 'end')
            sudoku_board[row][entry].insert(0, init_board.board[row][entry])


''' 
Purpose: submit() is a tikinter command to check if the answer matches the given answer
effect: edit the entrys and indicate weather it is true or not
'''
def submit():
    l = len(init_board.board)
    for row in range(l):
        for entry in range(l):
            # If it is not blank and it does not match the solution board, remove it
            if (len(sudoku_board[row][entry].get()) != 0 and int(sudoku_board[row][entry].get()) != init_board.board[row][entry]):
                sudoku_board[row][entry].delete(0, 'end')


'''
Purpose: add_solve_botton_to_screen() add the solve botton to the screen
effect: modify main_board()
'''
def add_solve_botton_to_screen():
    solve_botton = tkinter.Button(main_board, text = "solve!", command = (lambda: solve()), height = 1, width = 1)
    solve_botton.grid(row = 10, column = 6, padx = 10, pady = 10, ipadx = 10, ipady = 10)


'''   
Purpsoe: add_submit button to screen() add the submit botton for user to the screen
effect: modify main_board()
'''
def add_submit_botton_to_screen():
    submit_botton = tkinter.Button(main_board, text = "submit!", command = (lambda: submit()), height = 1, width = 1)
    submit_botton.grid(row = 10, column = 2, padx = 10, pady = 10, ipadx = 10, ipady = 10)


'''
Purpose: add_status_text_to_screen() add a status bar to the screen, shows, weather you win, or still need to try or solved it
effect: modify main_board()
'''
def add_status_text_to_screen():
    status_text = tkinter.Entry(main_board, state = 'disabled')
    status_text.insert(0, "Welcome to Sudoku Game!")
    status_text.grid(row = 11, column = 5, padx = 10, pady = 10, ipadx = 10, ipady = 10)



#start the Sudolu solver program
def start():
    input_board(init_board)
    add_to_screen(sudoku_board)
    add_solve_botton_to_screen()
    add_submit_botton_to_screen()
    add_status_text_to_screen()
    init_board.solve()
    main_board.mainloop()

    
