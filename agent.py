import math
import random

import game

class HumanPlayer(game.Player):

    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()

        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        response = input('Please choose a move: ')
        return moves[int(response)]

class RandomAgent(game.Player):

    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        moves = state.generateMoves()
        moveList = []

        if state.game_over():
            print("Game Over")
            return
        
        if len(moves) == 0:
            print("Out of Moves")
            return
        
        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
            moveList.append(i)
        response = random.choice(moveList)
        return moves[int(response)]
    


class MinimaxAgent(game.Player):
    def __init__(self, depth):
        self.depth = depth
        super().__init__()        

    def minmax(self, state, depth):
        if depth == 0:
            # print("Depth Limit")
            return state.score()
        
        if state.game_over():
            print("Game Over")
            return state.score()

        if state.nextPlayerToMove == 0:
            upperLimit = -math.inf 
            moves = state.generateMoves()
            for action in moves: 
                freshState = state.applyMoveCloning(action)
                currentValue = self.minmax(freshState, depth-1)
                if currentValue > upperLimit:
                    upperLimit = currentValue
            return upperLimit 
        
        else:
            lowerLimit = math.inf 
            moves = state.generateMoves()
            for action in moves: 
                freshState = state.applyMoveCloning(action)
                currentValue = self.minmax(freshState, depth-1)
                if currentValue < lowerLimit:
                    lowerLimit = currentValue
            return lowerLimit 

    def choose_move(self, state):
        moves = state.generateMoves()
        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))

        if state.game_over():
            print("Game Over")
            return
        
        if len(moves) == 0:
            print("Out of Moves")
            return

        if state.nextPlayerToMove == 0:
            upperLimit = -math.inf 
            lastMove = 0
            for i, action in enumerate(moves):
                freshState = state.applyMoveCloning(action)
                currentValue = self.minmax(freshState, self.depth)
                if currentValue > upperLimit:
                    lastMove = i
                    upperLimit = currentValue
            return moves[lastMove]

        else:
            lowerLimit = math.inf 
            lastMove = 0
            for i, action in enumerate(moves):
                freshState = state.applyMoveCloning(action)
                currentValue = self.minmax(freshState, self.depth)
                if currentValue < lowerLimit:
                    lastMove = i
                    lowerLimit = currentValue
            return moves[lastMove]


class AlphaBeta(game.Player):
    def __init__(self, depth):
        self.depth = depth
        super().__init__()

    def minmaxPrune(self, state, alpha, beta, depth):
        if depth == 0:
            # print("Depth Reached")
            return state.score()

        if state.game_over():
            print("Game Over!")
            return state.score()
        
        if state.nextPlayerToMove != 0:
            lowerLimit = math.inf 
            moves = state.generateMoves()
            for action in moves: 
                freshState = state.applyMoveCloning(action)
                currentValue = self.minmaxPrune(freshState, alpha, beta, depth-1)
                if currentValue < lowerLimit:
                    lowerLimit = currentValue
                if currentValue < beta:
                    beta = currentValue
            return lowerLimit
            
        
        else:
            upperLimit = -math.inf 
            moves = state.generateMoves()
            for action in moves: 
                freshState = state.applyMoveCloning(action)
                currentValue = self.minmaxPrune(freshState, alpha, beta, depth-1)
                if currentValue > upperLimit:
                    upperLimit = currentValue
                if currentValue > alpha:
                    alpha = currentValue
            return upperLimit 

    def compare(alpha,beta):
        if alpha >= beta:
            return 
             
        
    def choose_move(self, state):
        moves = state.generateMoves()
        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))

        if state.game_over():
            print("Game Over")
            return
        
        if len(moves) == 0:
            print("Out of Moves")
            return

        if state.nextPlayerToMove != 0:
            lowerLimit = math.inf 
            lastMove = 0
            for i, action in enumerate(moves):
                freshState = state.applyMoveCloning(action)
                currentValue = self.minmaxPrune(freshState, -math.inf, math.inf, self.depth)
                if currentValue < lowerLimit:
                    lastMove = i
                    lowerLimit = currentValue
            return moves[lastMove]
            

        else:
            upperLimit = -math.inf 
            lastMove = 0
            for i, action in enumerate(moves):
                freshState = state.applyMoveCloning(action)
                currentValue = self.minmaxPrune(freshState, -math.inf, math.inf, self.depth)
                if currentValue > upperLimit:
                    lastMove = i
                    upperLimit = currentValue
            return moves[lastMove]