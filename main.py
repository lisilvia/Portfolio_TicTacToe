from tkinter import *
import turtle
from turtle import *
from players import Player_x
from players import Player_o
from score import Infotext

row_one = ["   ", "|", "   ", "|", "   ",]
row_two = ["   ", "|", "   ", "|", "   ",]
row_three = ["   ", "|", "   ", "|", "   ",]
lines = ["----------------"]
board = [row_one, row_two, row_three]
score_board = [["", "", "",],["", "", "",],["", "", "",]]


def show_board():
    row_one_end = ""
    row_two_end = ""
    row_three_end = ""
    lines_end = ""
    for char in row_one:
        row_one_end += " " + char + " "
    for char in row_two:
        row_two_end += " " + char + " "
    for char in row_three:
        row_three_end += " " + char + " "
    for char in lines:
        lines_end += char
    return f"{row_one_end}\n{lines_end}\n{row_two_end}\n{lines_end}\n{row_three_end}"


def play():
    turtle.onscreenclick(get_mouse_click_coor)


def get_mouse_click_coor(x, y):
    turtle.onscreenclick(None)
    coordinates = (x, y)
    print(coordinates)
    print(coordinates[0])
    print(coordinates[1])
    coordinate_x = int(coordinates[0])
    coordinate_y = int(coordinates[1])
    global x_turn
    if coordinate_x < -38.0 and coordinate_x > -111.0 and coordinate_y < 130.0 and coordinate_y > 55.0:
        if score_board[0][0] == "":
            if x_turn:
                player_x = Player_x()
                player_x.goto(-85, 90)
                player_x.draw_x()
                score_board[0][0] = "X"
                x_turn = False
            else:
                if score_board[0][0] == "":
                    player_o = Player_o()
                    player_o.goto(-78, 75)
                    player_o.draw_o()
                    score_board[0][0] = "O"
                    x_turn = True
        else:
            pass
    elif coordinate_x < 50.0 and coordinate_x > -32.0 and coordinate_y < 130.0 and coordinate_y > 55.0:
        if score_board[0][1] == "":
            if x_turn:
                player_x = Player_x()
                player_x.goto(2, 90)
                player_x.draw_x()
                score_board[0][1] = "X"
                x_turn = False
            else:
                if score_board[0][1] == "":
                    player_o = Player_o()
                    player_o.goto(10, 75)
                    player_o.draw_o()
                    score_board[0][1] = "O"
                    x_turn = True
        else:
            pass
    elif coordinate_x < 132.0 and coordinate_x > 56.0 and coordinate_y < 130.0 and coordinate_y > 55.0:
        if score_board[0][2] == "":
            if x_turn:
                player_x = Player_x()
                player_x.goto(90, 90)
                player_x.draw_x()
                score_board[0][2] = "X"
                x_turn = False
            else:
                player_o = Player_o()
                player_o.goto(95, 75)
                player_o.draw_o()
                score_board[0][2] = "O"
                x_turn = True
        else:
            pass
    elif coordinate_x < -38.0 and coordinate_x > -111.0 and coordinate_y < 47.0 and coordinate_y > -40.0:
        if score_board[1][0] == "":
            if x_turn:
                player_x = Player_x()
                player_x.goto(-85, -3)
                player_x.draw_x()
                score_board[1][0] = "X"
                x_turn = False
            else:
                player_o = Player_o()
                player_o.goto(-78, -15)
                player_o.draw_o()
                score_board[1][0] = "O"
                x_turn = True
        else:
            pass
    elif coordinate_x < 50.0 and coordinate_x > -32.0 and coordinate_y < 47.0 and coordinate_y > -40.0:
        if score_board[1][1] == "":
            if x_turn:
                player_x = Player_x()
                player_x.goto(2, -3)
                player_x.draw_x()
                score_board[1][1] = "X"
                x_turn = False
            else:
                player_o = Player_o()
                player_o.goto(10, -15)
                player_o.draw_o()
                score_board[1][1] = "O"
                x_turn = True
        else:
            pass
    elif coordinate_x < 132.0 and coordinate_x > 56.0 and coordinate_y < 47.0 and coordinate_y > -40.0:
        if score_board[1][2] == "":
            if x_turn:
                player_x = Player_x()
                player_x.goto(90, -3)
                player_x.draw_x()
                score_board[1][2] = "X"
                x_turn = False
            else:
                player_o = Player_o()
                player_o.goto(95, -15)
                player_o.draw_o()
                score_board[1][2] = "O"
                x_turn = True
        else:
            pass
    elif coordinate_x < -38.0 and coordinate_x > -111.0 and coordinate_y < -47.0 and coordinate_y > -122:
        if score_board[2][0] == "":
            if x_turn:
                player_x = Player_x()
                player_x.goto(-85, -95)
                player_x.draw_x()
                score_board[2][0] = "X"
                x_turn = False
            else:
                player_o = Player_o()
                player_o.goto(-78, -110)
                player_o.draw_o()
                score_board[2][0] = "O"
                x_turn = True
        else:
            pass
    elif coordinate_x < 50.0 and coordinate_x > -32.0 and coordinate_y < -47.0 and coordinate_y > -122:
        if score_board[2][1] == "":
            if x_turn:
                player_x = Player_x()
                player_x.goto(2, -95)
                player_x.draw_x()
                score_board[2][1] = "X"
                x_turn = False
            else:
                player_o = Player_o()
                player_o.goto(10, -110)
                player_o.draw_o()
                score_board[2][1] = "O"
                x_turn = True
        else:
            pass
    elif coordinate_x < 132.0 and coordinate_x > 56.0 and coordinate_y < -47.0 and coordinate_y > -122:
        if score_board[2][2] == "":
            if x_turn:
                player_x = Player_x()
                player_x.goto(90, -95)
                player_x.draw_x()
                score_board[2][2] = "X"
                x_turn = False
            else:
                player_o = Player_o()
                player_o.goto(95, -110)
                player_o.draw_o()
                score_board[2][2] = "O"
                x_turn = True
        else:
            pass
    else:
        print('choose again')

    winning_combinations = [
        [score_board[0][0], score_board[0][1], score_board[0][2]],
        [score_board[1][0], score_board[1][1], score_board[1][2]],
        [score_board[2][0], score_board[2][1], score_board[2][2]],
        [score_board[0][0], score_board[1][0], score_board[2][0]],
        [score_board[0][1], score_board[1][1], score_board[2][1]],
        [score_board[0][2], score_board[1][2], score_board[2][2]],
        [score_board[0][0], score_board[1][1], score_board[2][2]],
        [score_board[0][2], score_board[1][1], score_board[2][0]]
    ]
    for combination in winning_combinations:
        global game
        if combination == ['X', 'X', 'X']:
            print("Player X wins!")
            infotext = Infotext()
            infotext.xwins()
            game = OFF

        elif combination == ['O', 'O', 'O']:
            print("Player O wins!")
            infotext = Infotext()
            infotext.owins()
            game = OFF


x_turn = True
game = ON
while game is ON:
    screen = turtle.Screen()
    screen.title("Tic-Tac-Toe")
    screen.setup(width=500, height=500)
    screen.bgcolor("#303030")
    hideturtle()
    penup()
    turtle.goto(10, -110)
    turtle.color("white")
    turtle.write(show_board(),
                 align="center",
                 font=('Helvetica', '31', 'bold'))

    play()
