"""
This is the main drive file. It will handle user input and will display current GameState object
"""


import pygame as p
from Chess import chessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #dimensions of chess board 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animations later
IMAGES = {}

'''
initialize a global dictionary of images. This will be called exactly once in the main
'''
def loadImages():
    pieces = ['wp','wR','wN','wK','wQ','wB','bp','bR','bN','bK','bQ','bB']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+ piece + ".png"), (SQ_SIZE,SQ_SIZE))
    # note: we can acces an image by saying 'IMAGES['wp']'

'''
This will be the main driver. will handle user input and updating graphics

change
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState()
    print(gs.board)

main()