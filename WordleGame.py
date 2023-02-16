import struct, time, os
import cv2
import os
import numpy as np
from wordgenerator import generate_random_word

#colors
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
BG_Color = (200,200,200)
import pygame, sys
pygame.init()
widthS = 600
heightS = 600

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('R', True, Green)
text2 = font.render('T', True, Green)
charBoard = np.zeros(shape=(5,5), dtype='object')
for i in range(5):
    for j in range(5):
        charBoard[i,j] = (20,20)
def write(text, x,y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text2 = font.render(text, True, Green)
    textRect = text2.get_rect()
    textRect.center = (x, y)
    

def drawBox(screen, color, Coord1, size, thickness):
    pygame.draw.line( screen, color, Coord1, (Coord1[0] + size, Coord1[1]), thickness)
    pygame.draw.line(screen, color, Coord1, (Coord1[0], Coord1[1] + size), thickness)
    pygame.draw.line(screen, color, (Coord1[0], Coord1[1] + size), (Coord1[0] + size, Coord1[1] + size), thickness)
    pygame.draw.line(screen, color, (Coord1[0]+size, Coord1[1]), (Coord1[0] + size, Coord1[1] + size), thickness)





import enchant
d = enchant.Dict("en_US")


from os import system, name
board = np.empty(shape=(5,5), dtype='object')
charBoard = np.empty(shape=(5,5), dtype = 'object')


def cls():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')
def clearBoard(board):
    for i in range(5):
        for j in range(5):
            board[i,j] = " "


def askChar():
    val = input("Next Char?  ")
    if val == "":
        return 'del'
    if inAlphabet(val) == False or len(val) >1:
        print("invalid option, please use a single letter")
        val = input("Next Char?  ")
    return val

def inAlphabet(string):
    for char in str('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'):
        if string == char:
            return True
    return False

def turn(board, Row):
    numC = 0
    while numC < 5:
        val = askChar()
        if numC == 0 and val == 'del':
            print("Cannot delete nothing idiot, try again")

        elif val == 'del':
            board[Row, numC-1] = " "
            numC -= 1
            cls()
            print(numC)
            print(board)
        else:
            board[Row, numC] = val
            numC += 1
            cls()
            print(numC)
            print(board)

def wordCheck(board, row, answer):
    word = ''
    for i in range(5):
        word = word + board[row,i]
    if word == answer:
        return 2
    if d.check(word) == True:
        return 1
    else:
        return 0

def newWord():
    word = ''
    allLetters = True
    while len(word) != 5 or allLetters == False:
        word = generate_random_word()
        for i in range(len(word)):
            if inAlphabet(word[i]) == False:
                allLetters = False
    return word

def letterCheck(board,row,answer):
    correct = []
    inWord = []
    for i in range(5):
        if answer[i] == board[row,i]:
            correct.append(answer[i])
        for j in range(5):
            if answer[i] == board[row,j] and inWord.count(answer[i]) == 0:
                inWord.append(answer[i])
    return correct,inWord



gameOn = True
Row = 0
Word = newWord()
clearBoard(board)




C_Letters = []
C_Spot = []
gameOn = True
Row = 0
Word = newWord()
clearBoard(board)
while(gameOn):

    print(Word)
    turn(board, Row)


    if wordCheck(board, Row, Word) == 0:
        for i in range(5):
            board[Row,i] = ' '
        cls()
        print("Incredible how dumb you are")
        print(board)
    elif wordCheck(board,Row,Word) == 2:
        print("You got it!")
        playAgain = input("Play again? y/n  ")
        if playAgain == 'n':
            gameOn = False
        else:
            Row = 0
            Word = newWord()
            C_Letters = []
            C_Spot = []
            clearBoard(board)
    else:
        print("Wow thats actually a word, wrong tho")
        correct = letterCheck(board, Row, Word)
        for i in range(len(correct[0])):
            if C_Spot.count(correct[0][i]) == 0:
                C_Spot.append(correct[0][i])
        for i in range(len(correct[1])):
            if C_Letters.count(correct[1][i]) == 0:
                C_Letters.append(correct[1][i])
        Row += 1
        if Row > 4:
            playAgain = input("You Lost! Play again? y/n  ")
            if playAgain == 'n':
                gameOn = False
            else:
                Row = 0
                Word = newWord()
                C_Letters = []
                C_Spot = []
                clearBoard(board)

    print("These letters are in the word ", C_Letters)
    print("These letters are in the right spot ", C_Spot)


# print(val)
# img = cv2.imread(r'C:\Users\zrdra\OneDrive\Pictures\Screenshots\Screenshot (1).png')
