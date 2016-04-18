import copy
import numpy as np

aiTurn = 1
manTurn = 0
turn = aiTurn
boards = []
playCount = 1
a = 2
b = 3
c = 5
d = 7 # so a = 2, bc = 15, b^2 = 9, C^2 = 25
playerLastMove = (-1, -1)

class gameBoard:
    def __init__(self, name):
        self.name = name
        self.isGameOver = False  # indicate the game status, True for game over
        self.value = 0           # indicate the value of the board, that means a, b, c or their combination
        self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]   # indicate the 3*3 board
        self.width = 3
        self.height = 3
        self.depth = 3

    def gameOver(self):
        for row in self.board:
            if row[0] == 'X' and row[1] == 'X' and row[2] == 'X':
                return True

        if self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X':
            return True

        if self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X':
            return True

        if self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X':
            return True

        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            return True

        if self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X':
            return True

        return False


def resetTheData():
    global turn
    global boards

    turn = aiTurn
    names = ['A', 'B', 'C']
    boards = [gameBoard(name) for name in names]

def isGameOver(gameBoards):
    if len(gameBoards) == 0:
        return True
    else:
        return False

def printBoards(gameBoards):
    for gameBoard in gameBoards:
        print gameBoard.name + '    ',
    print '\n'

    for i in range(0, 3):
        thingsToPrint = []
        if len(gameBoards) == 1:
            thingsToPrint += gameBoards[0].board[i]
        elif len(gameBoards) == 2:
            thingsToPrint += gameBoards[0].board[i] + gameBoards[1].board[i]
        elif len(gameBoards) == 3:
            thingsToPrint += gameBoards[0].board[i] + gameBoards[1].board[i] + gameBoards[2].board[i]

        for object in thingsToPrint:
            print object,

        print '\n'


def transferStringToInt(board):
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] != 'X':
                board[i][j] = int(board[i][j])

    return board


def rotateBoard(board):
    nparray = np.array(board)
    nparray = np.rot90(nparray)
    board = nparray.tolist()
    board = transferStringToInt(board)
    return board


def fliplr(board):
    nparray = np.array(board)
    nparray = np.fliplr(nparray)
    board = nparray.tolist()
    board = transferStringToInt(board)
    return board


def flipud(board):
    nparray = np.array(board)
    nparray = np.flipud(nparray)
    board = nparray.tolist()
    board = transferStringToInt(board)
    return board


def getValue(gameBoard):
    copyOfGameBoard = copy.deepcopy(gameBoard)
    board = copyOfGameBoard.board

    # rotate the board to check every possibility
    for i in range(0, 4):
        board = rotateBoard(board)
        for j in range(0, 3):
            if j == 1:
                board = fliplr(board)
            elif j == 2:
                board = flipud(board)

            #c=5 a=2 d=7 b=3
            if board == [[0,1,2],[3,4,5],[6,7,8]]:
                return c
            elif board == [[0,1,2],[3,'X',5],[6,7,8]]:
                return c**2
            elif board == [['X','X',2],[3,4,5],[6,7,8]]:
                return a*d
            elif board == [['X',1,'X'],[3,4,5],[6,7,8]]:
                return b
            elif board == [['X',1,2],[3,'X',5],[6,7,8]]:
                return b
            elif board == [['X',1,2],[3,4,'X'],[6,7,8]]:
                return b
            elif board == [['X',1,2],[3,4,5],[6,7,'X']]:
                return a
            elif board == [[0,'X',2],['X',4,5],[6,7,8]]:
                return a
            elif board == [[0,'X',2],[3,'X',5],[6,7,8]]:
                return b
            elif board == [[0,'X',2],[3,4,5],[6,'X',8]]:
                return a
            elif board == [['X','X',2],['X',4,5],[6,7,8]]:
                return b
            elif board == [['X','X',2],[3,'X',5],[6,7,8]]:
                return a*b
            elif board == [['X','X',2],[3,4,'X'],[6,7,8]]:
                return d
            elif board == [['X','X',2],[3,4,5],['X',7,8]]:
                return a
            elif board == [['X','X',2],[3,4,5],[6,'X',8]]:
                return d
            elif board == [['X','X',2],[3,4,5],[6,7,'X']]:
                return d
            elif board == [['X',1,'X'],[3,'X',5],[6,7,8]]:
                return a
            elif board == [['X',1,'X'],[3,4,5],['X',7,8]]:
                return a*b
            elif board == [['X',1,'X'],[3,4,5],[6,'X',8]]:
                return a
            elif board == [['X',1,2],[3,'X','X'],[6,7,8]]:
                return a
            elif board == [[0,'X',2],['X','X',5],[6,7,8]]:
                return a*b
            elif board == [[0,'X',2],['X',4,'X'],[6,7,8]]:
                return b
            elif board == [['X','X',2],['X','X',5],[6,7,8]]:
                return a
            elif board == [['X','X',2],['X',4,'X'],[6,7,8]]:
                return a
            elif board == [['X','X',2],['X',4,5],[6,7,'X']]:
                return a
            elif board == [['X','X',2],[3,'X','X'],[6,7,8]]:
                return b
            elif board == [['X','X',2],[3,'X',5],['X',7,8]]:
                return b
            elif board == [['X','X',2],[3,4,'X'],['X',7,8]]:
                return b
            elif board == [['X','X',2],[3,4,'X'],[6,'X',8]]:
                return a*b
            elif board == [['X','X',2],[3,4,'X'],[6,7,'X']]:
                return a*b
            elif board == [['X','X',2],[3,4,5],['X','X',8]]:
                return b
            elif board == [['X','X',2],[3,4,5],['X',7,'X']]:
                return b
            elif board == [['X','X',2],[3,4,5],[6,'X','X']]:
                return a
            elif board == [['X',1,'X'],[3,'X',5],[6,'X',8]]:
                return b
            elif board == [['X',1,'X'],[3,4,5],['X',7,'X']]:
                return a
            elif board == [['X',1,2],[3,'X','X'],[6,'X',8]]:
                return b
            elif board == [[0,'X',2],['X',4,'X'],[6,'X',8]]:
                return a
            elif board == [['X','X',2],['X',4,'X'],[6,7,'X']]:
                return b
            elif board == [['X','X',2],[3,'X','X'],['X',7,8]]:
                return a
            elif board == [['X','X',2],[3,4,'X'],['X','X',8]]:
                return a
            elif board == [['X','X',2],[3,4,'X'],['X',7,'X']]:
                return a
            elif board == [['X','X',2],['X',4,'X'],[6,'X','X']]:
                return a
            #elif board == [['X','X',2],[3,4,'X'],['X','X',8]]:
            #    return a

    return 1

def checkBoards(gameBoards):
    # check if a board is over
    indexToDelete = -1
    for indexForBoard, gameBoard in enumerate(gameBoards):
        if gameBoard.gameOver():
            indexToDelete = indexForBoard
            break

    if indexToDelete != -1:
        del gameBoards[indexToDelete]

    return gameBoards


def evaluationFunction(gameBoards, turn):
    score = 0

    if isGameOver(gameBoards):
        if turn == aiTurn:
            # it means AI lost the game
            return float('-inf')
        elif turn == manTurn:
            # it means AI wins the game
            return float('inf')

    valueOfBoards = 1
    for gameBoard in gameBoards:
        valueOfBoards *= getValue(gameBoard)

    if valueOfBoards in [c**2, a, b**2, b*c]:
        if turn == aiTurn:
            score += 100

    return score

def getLegalMoves(gameBoard):
    legalMoves = []
    for x in range(0, 3):
        for y in range(0, 3):
            if gameBoard.board[x][y] != 'X':
                legalMoves.append((x, y))

    return legalMoves


def getBestMove(gameBoard, lastMove):



def generateNewBoards(gameBoards,indexForBoard, move):
    newBoards = copy.deepcopy(boards)
    newBoards[indexForBoard].board[move[0]][move[1]] = 'X'
    return newBoards


def makeMove(indexForBoard, move):
    boards[indexForBoard].board[move[0]][move[1]] = 'X'


def maxValue(gameBoards, depth, turn, alpha, beta):
    if isGameOver(gameBoards):
        return (None, evaluationFunction(gameBoards, turn))

    maxEval = float('-inf')

    if len(gameBoards) > 1:
        # Get Legal Actions
        legalMoves = [getLegalMoves(gameBoard) for gameBoard in boards]
        for indexForBoard, moves in enumerate(legalMoves):
            for move in moves:
                newBoards = generateNewBoards(boards, indexForBoard, move)
                score = evaluationFunction(newBoards, turn)
                if score > maxEval:
                    maxEval = score
                    maxMove = (indexForBoard, move)
    else:
        indexForBoard = 0
        bestMove = getBestMove(gameBoards[0], playerLastMove)

    return maxMove


def minValue(gameBoards, depth, turn, alpha, beta):
    return 1


def aiPlay():
    global turn, boards
    (indexForBoard, move) = maxValue(boards, 1, turn, float('-inf'), float('inf'))
    makeMove(indexForBoard, move)
    print 'AI: %s%d' % (boards[indexForBoard].name, (move[0] * 3 + move[1]))
    boards = checkBoards(boards)
    printBoards(boards)

    turn = manTurn

def isLegalMove(gameBoards, move):
    if len(move) != 2:
        print 'Invalid Move'
        return False

    try:
        nameOfBoard = move[0].upper()
        positionOfBoard = int(move[1])
    except Exception:
        print 'Invalid Move'
        return False

    if nameOfBoard not in [gameBoard.name for gameBoard in gameBoards]:
        print "invalid move"
        return False

    if positionOfBoard < 0 or positionOfBoard > 8:
        print "invalid move"
        return False

    for gameBoard in gameBoards:
        if gameBoard.name == nameOfBoard:
            chosenBoard = gameBoard
            break

    # check if the position is valid
    x = positionOfBoard / 3
    y = positionOfBoard - 3 * x
    if chosenBoard.board[x][y] == 'X':
        print "invalid move"
        return False

    return True

def playerPlay():
    global turn, boards, playerLastMove
    move = raw_input("Your move: ")
    while not isLegalMove(boards, move):
        move = raw_input("Your move: ")

    nameOfBoard = move[0].upper()
    positionOfBoard = int(move[1])
    x = positionOfBoard / 3
    y = positionOfBoard - 3 * x
    for indexForBoard, gameBoard in enumerate(boards):
        if gameBoard.name == nameOfBoard:
            makeMove(indexForBoard, (x, y))
            playerLastMove = (x, y)
            break

    boards = checkBoards(boards)
    printBoards(boards)
    turn = aiTurn


def runGame():
    global playCount

    # reset the data
    resetTheData()

    print 'Game Start!'
    while not isGameOver(boards):
        if turn == aiTurn:
            aiPlay()
        elif turn == manTurn:
            playerPlay()

        playCount += 1

    if turn == aiTurn:
        # ai lose
        print 'You Lose'
    else:
        print 'You Win'


if __name__ == '__main__':
    runGame()