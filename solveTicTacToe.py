import copy
import numpy as np

aiTurn = 1
manTurn = 0
a = 2
b = 3
c = 5
d = 7
namesForBoard = ['A', 'B', 'C']


class GameBoard:
    def __init__(self, name):
        self.name = name
        self.board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]   # indicate the 3*3 board

    def gameOver(self):
        for row in self.board:
            if row[0] == 'X' and row[1] == 'X' and row[2] == 'X':
                return True

        for i in range(0, 3):
            if self.board[0][i] == 'X' and self.board[1][i] == 'X' and self.board[2][i] == 'X':
                return True

        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            return True

        if self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X':
            return True

        return False

    def transferStringToInt(self, aBoard):
        for i in range(0, 3):
            for j in range(0, 3):
                if aBoard[i][j] != 'X':
                    aBoard[i][j] = int(0)
        return aBoard

    def rotateBoard(self, aBoard):
        nparray = np.array(aBoard)
        nparray = np.rot90(nparray)
        board = nparray.tolist()
        board = self.transferStringToInt(board)
        return board

    def fliplr(self, aBoard):
        nparray = np.array(aBoard)
        nparray = np.fliplr(nparray)
        board = nparray.tolist()
        board = self.transferStringToInt(board)
        return board

    def flipud(self, aBoard):
        nparray = np.array(aBoard)
        nparray = np.flipud(nparray)
        board = nparray.tolist()
        board = self.transferStringToInt(board)
        return board

    def getValue(self):
        board = copy.deepcopy(self).board

        # rotate the board to check every possibility
        for i in range(0, 4):
            board = self.rotateBoard(board)
            testBoard = copy.deepcopy(board)
            for j in range(0, 3):
                if j == 1:
                    testBoard = self.fliplr(board)
                elif j == 2:
                    testBoard = self.flipud(board)

                if testBoard == [[0,0,0],[0,0,0],[0,0,0]]:
                    return c
                elif testBoard == [[0,0,0],[0,'X',0],[0,0,0]]:
                    return c**2
                elif testBoard == [['X','X',0],[0,0,0],[0,0,0]]:
                    return a*d
                elif testBoard == [['X',0,'X'],[0,0,0],[0,0,0]]:
                    return b
                elif testBoard == [['X',0,0],[0,'X',0],[0,0,0]]:
                    return b
                elif testBoard == [['X',0,0],[0,0,'X'],[0,0,0]]:
                    return b
                elif testBoard == [['X',0,0],[0,0,0],[0,0,'X']]:
                    return a
                elif testBoard == [[0,'X',0],['X',0,0],[0,0,0]]:
                    return a
                elif testBoard == [[0,'X',0],[0,'X',0],[0,0,0]]:
                    return b
                elif testBoard == [[0,'X',0],[0,0,0],[0,'X',0]]:
                    return a
                elif testBoard == [['X','X',0],['X',0,0],[0,0,0]]:
                    return b
                elif testBoard == [['X','X',0],[0,'X',0],[0,0,0]]:
                    return a*b
                elif testBoard == [['X','X',0],[0,0,'X'],[0,0,0]]:
                    return d
                elif testBoard == [['X','X',0],[0,0,0],['X',0,0]]:
                    return a
                elif testBoard == [['X','X',0],[0,0,0],[0,'X',0]]:
                    return d
                elif testBoard == [['X','X',0],[0,0,0],[0,0,'X']]:
                    return d
                elif testBoard == [['X',0,'X'],[0,'X',0],[0,0,0]]:
                    return a
                elif testBoard == [['X',0,'X'],[0,0,0],['X',0,0]]:
                    return a*b
                elif testBoard == [['X',0,'X'],[0,0,0],[0,'X',0]]:
                    return a
                elif testBoard == [['X',0,0],[0,'X','X'],[0,0,0]]:
                    return a
                elif testBoard == [[0,'X',0],['X','X',0],[0,0,0]]:
                    return a*b
                elif testBoard == [[0,'X',0],['X',0,'X'],[0,0,0]]:
                    return b
                elif testBoard == [['X','X',0],['X','X',0],[0,0,0]]:
                    return a
                elif testBoard == [['X','X',0],['X',0,'X'],[0,0,0]]:
                    return a
                elif testBoard == [['X','X',0],['X',0,0],[0,0,'X']]:
                    return a
                elif testBoard == [['X','X',0],[0,'X','X'],[0,0,0]]:
                    return b
                elif testBoard == [['X','X',0],[0,'X',0],['X',0,0]]:
                    return b
                elif testBoard == [['X','X',0],[0,0,'X'],['X',0,0]]:
                    return b
                elif testBoard == [['X','X',0],[0,0,'X'],[0,'X',0]]:
                    return a*b
                elif testBoard == [['X','X',0],[0,0,'X'],[0,0,'X']]:
                    return a*b
                elif testBoard == [['X','X',0],[0,0,0],['X','X',0]]:
                    return b
                elif testBoard == [['X','X',0],[0,0,0],['X',0,'X']]:
                    return b
                elif testBoard == [['X','X',0],[0,0,0],[0,'X','X']]:
                    return a
                elif testBoard == [['X',0,'X'],[0,'X',0],[0,'X',0]]:
                    return b
                elif testBoard == [['X',0,'X'],[0,0,0],['X',0,'X']]:
                    return a
                elif testBoard == [['X',0,0],[0,'X','X'],[0,'X',0]]:
                    return b
                elif testBoard == [[0,'X',0],['X',0,'X'],[0,'X',0]]:
                    return a
                elif testBoard == [['X','X',0],['X',0,'X'],[0,0,'X']]:
                    return b
                elif testBoard == [['X','X',0],[0,'X','X'],['X',0,0]]:
                    return a
                elif testBoard == [['X','X',0],[0,0,'X'],['X','X',0]]:
                    return a
                elif testBoard == [['X','X',0],[0,0,'X'],['X',0,'X']]:
                    return a
                elif testBoard == [['X','X',0],['X',0,'X'],[0,'X','X']]:
                    return a
                elif testBoard == [['X','X',0],['X',0,'X'],[0,'X',0]]:
                    return b

        return 1

    def getLegalMoves(self):
        legalMoves = []
        for x in range(0, 3):
            for y in range(0, 3):
                if self.board[x][y] != 'X':
                    legalMoves.append((x, y))

        return legalMoves


class GameBoards:
    def __init__(self):
        self.boards = [GameBoard(name) for name in namesForBoard]
        self.turn = aiTurn
        self.depth = 2

    def isGameOver(self):
        if len(self.boards) == 0:
            return True
        else:
            return False

    def isLegalMoveForPlayer(self, move):
        if len(move) != 2:
            print 'Invalid Move'
            return False

        try:
            nameOfBoard = move[0].upper()
            positionOfBoard = int(move[1])
        except Exception:
            print 'Invalid Move'
            return False

        if nameOfBoard not in [gameBoard.name for gameBoard in self.boards]:
            print "invalid move"
            return False

        if positionOfBoard < 0 or positionOfBoard > 8:
            print "invalid move"
            return False

        for gameBoard in self.boards:
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

    def checkAndDelete(self):
        # check if a board is over
        indexToDelete = -1
        for indexForBoard, gameBoard in enumerate(self.boards):
            if gameBoard.gameOver():
                indexToDelete = indexForBoard
                break

        # is a board is over, then delete it
        if indexToDelete != -1:
            del self.boards[indexToDelete]

    # generate the successor
    def generateNewBoards(self, indexForBoard, move):
        newBoards = copy.deepcopy(self)
        newBoards.makeMove(indexForBoard, move)
        return newBoards

    def makeMove(self, indexForBoard, move):
        self.boards[indexForBoard].board[move[0]][move[1]] = 'X'

    def printBoards(self):
        if self.isGameOver():
            return
        for gameBoard in self.boards:
            print gameBoard.name + '    ',
        print '\n'

        for i in range(0, 3):
            thingsToPrint = []
            if len(self.boards) == 1:
                thingsToPrint += self.boards[0].board[i]
            elif len(self.boards) == 2:
                thingsToPrint += self.boards[0].board[i] + self.boards[1].board[i]
            elif len(self.boards) == 3:
                thingsToPrint += self.boards[0].board[i] + self.boards[1].board[i] + self.boards[2].board[i]

            for object in thingsToPrint:
                print object,

            print '\n'

# get the value of the boards
def evaluationFunction(aGameBoards):
    score = 0

    aGameBoards.checkAndDelete()
    if aGameBoards.isGameOver():
        if aGameBoards.turn == aiTurn:
            # it means AI lost the game
            return float('-inf')
        elif aGameBoards.turn == manTurn:
            # it means AI wins the game
            return float('inf')

    valueOfBoards = 1
    for gameBoard in aGameBoards.boards:
        valueOfBoards *= gameBoard.getValue()

    if valueOfBoards in [c**2, a, b**2, b*c]:
        if aGameBoards.turn == aiTurn:
            score += 100
        elif aGameBoards.turn == manTurn:
            score -= 100

    return score


def maxValue(aGameBoards, depth, alpha, beta):
    aGameBoards.checkAndDelete()
    if aGameBoards.isGameOver():
        return evaluationFunction(aGameBoards)

    maxEval = float('-inf')

    legalMoves = [gameBoard.getLegalMoves() for gameBoard in aGameBoards.boards]
    for indexForBoard, moves in enumerate(legalMoves):
        for indexForMove, move in enumerate(moves):
            #if indexForMove != 0 and aGameBoards.boards[indexForBoard].gameOver():
            #    break
            newBoards = aGameBoards.generateNewBoards(indexForBoard, move)
            newBoards.turn = aiTurn

            tempEval = minValue(newBoards, depth + 1, alpha, beta)

            if tempEval > maxEval:
                maxEval = tempEval
                maxMove = move
                maxIndexForBoard = indexForBoard

            # prune
            if maxEval > beta:
                return maxEval

            alpha = max(alpha, maxEval)

    if depth == 1:
        return (maxIndexForBoard, maxMove)
    else:
        return maxEval


def minValue(aGameBoards, depth, alpha, beta):
    aGameBoards.checkAndDelete()
    if aGameBoards.isGameOver():
        return evaluationFunction(aGameBoards)

    minEval = float('inf')
    legalMoves = [gameBoard.getLegalMoves() for gameBoard in aGameBoards.boards]
    for indexForBoard, moves in enumerate(legalMoves):
        for indexForMove, move in enumerate(moves):
            #if indexForMove != 0 and aGameBoards.boards[indexForBoard].gameOver():
            #    break
            newBoards = aGameBoards.generateNewBoards(indexForBoard, move)
            newBoards.turn = manTurn

            if depth == aGameBoards.depth:
                tempEval = evaluationFunction(aGameBoards)
            else:
                tempEval = maxValue(newBoards, depth + 1, alpha, beta)

            if tempEval < minEval:
                minEval = tempEval

            # prune
            if minEval < alpha:
                return minEval

            beta = min(beta, minEval)

    return minEval


def aiPlay(gameBoards):
    (indexForBoard, move) = maxValue(gameBoards, 1, float('-inf'), float('inf'))
    gameBoards.makeMove(indexForBoard, move)
    print 'AI: %s%d' % (gameBoards.boards[indexForBoard].name, (move[0] * 3 + move[1]))
    gameBoards.checkAndDelete()
    gameBoards.printBoards()
    gameBoards.turn = manTurn


def playerPlay(gameBoards):
    move = raw_input("Your move: ")
    while not gameBoards.isLegalMoveForPlayer(move):
        move = raw_input("Your move: ")

    nameOfBoard = move[0].upper()
    positionOfBoard = int(move[1])
    x = positionOfBoard / 3
    y = positionOfBoard - 3 * x
    for indexForBoard, gameBoard in enumerate(gameBoards.boards):
        if gameBoard.name == nameOfBoard:
            gameBoards.makeMove(indexForBoard, (x, y))
            break

    gameBoards.checkAndDelete()
    gameBoards.printBoards()
    gameBoards.turn = aiTurn


def runGame():
    gameBoards = GameBoards()

    print '----------Game Start!----------'
    while not gameBoards.isGameOver():
        if gameBoards.turn == aiTurn:
            aiPlay(gameBoards)
        elif gameBoards.turn == manTurn:
            playerPlay(gameBoards)

    if gameBoards.turn == aiTurn:
        print 'You Lose, Try Again\n'
    else:
        print 'You Win, Congratulations\n'

if __name__ == '__main__':
    while True:
        runGame()
