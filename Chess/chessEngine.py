"""
this class is responsible for storing all the information about the current state of a chess game.
Will also be responsible for determining the valid moves at the current state
"""
class GameState():
    def __init__(self):

        # board is 8x8 2D list, each element of list has 2 characters
        # character 1 is color of piece (b=black, w = white), second character is typee
        # "--" represents an empty space
        self.board= [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []