Implemented a program to play the game of Othello using AI. The game is played between a human and a computer and between a computer and computer. We had to make an agent that will work on 3 parts – Random, Minimax and Minimax + Alpha-Beta Pruning.

In random, we let 2 AI play against each other with random moves and a winner is declared in the end.
>> sh run.sh random random

In minimax, we play Othello with the minimax algorithm where our agent wins against the random agent.
>> sh run.sh minimax random 1

In alpha beta pruning we uses alpha-beta search. The agent's constructor should accept the depth up to which we want to search.
>> sh run.sh alphabeta random 1