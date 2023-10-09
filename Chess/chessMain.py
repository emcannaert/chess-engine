"""
This is the main drive file. It will handle user input and will display current GameState object
"""


import pygame as p
from Chess import chessEngine

WIDTH = HEIGHT = 2*512
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
    # note: we can access an image by saying 'IMAGES['wp']'

'''
This will be the main driver. will handle user input and updating graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState() # calls the init in chessEngine.py to create the object
    loadImages()   # only needs to be done once
    running = True
    sqSelected = ()   #the selected square, nothing initially selected, last click of the user (row,col)
    playerClicks = []   #keep track of clicks the player has made [(6,4),(4,4)]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()    #(x,y) location of mouse (units?)
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE

                if sqSelected == (row,col):  # want to check if the same square was checked twice
                    sqSelected = ()  # deselect
                    playerClicks = []  #clear
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)   # append for both 1st and second clicks
                if len(playerClicks) == 2:  # after second click
                    move = chessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    sqSelected = ()   #reset clicks
                    playerClicks = []
                    gs.makeMove(move)
        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()
    print(gs.board)


"""
makes all the graphics for the current game state
"""
def drawGameState(screen, gs):
    drawBoard(screen)   # draws squares on board
    drawPieces(screen,gs.board)  # draw pieces on top of those squares

"""
draw the board squares. The top left square is always light - this is true from both black and white's perspective
"""
def drawBoard(screen):
    colors = [p.Color("White"), p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c)%2]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE, SQ_SIZE,SQ_SIZE))
    return

"""
draw pieces on the board using GameState.board
"""
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--": #not empty square
                screen.blit(IMAGES[piece], p.Rect(column*SQ_SIZE,row*SQ_SIZE, SQ_SIZE,SQ_SIZE))
    return
if __name__=='__main__':
    main()