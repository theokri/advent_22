import csv
from enum import Enum
from dataclasses import dataclass

class OpponentMove(Enum):
    Rock = 'A'
    Paper = 'B'
    Scissors = 'C'

class MyMove(Enum):
    Rock = 'X'
    Paper = 'Y'
    Scissors = 'Z'

move_score = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

move_beats = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}

@dataclass
class Round:
    opponent_move: OpponentMove
    my_move: MyMove

    def score_round(self):        
        opponent_score = move_score[self.opponent_move.name]
        my_score = move_score[self.my_move.name]
        
        if move_beats[self.opponent_move.name] == self.my_move.name:
            opponent_score += 6
        elif move_beats[self.my_move.name] == self.opponent_move.name:
            my_score += 6
        else:
            opponent_score += 3
            my_score += 3

        return opponent_score, my_score

opponent_total_score = 0
my_total_score = 0

with open('strategy_guide.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        opponent_move_encoded, my_move_encoded = line[0].split(' ')
        round = Round(OpponentMove(opponent_move_encoded), MyMove(my_move_encoded))
        opponent_score, my_score = round.score_round()
        opponent_total_score += opponent_score
        my_total_score += my_score
        

print(f'Opponent total score: {opponent_total_score}\nMy total score: {my_total_score}')
