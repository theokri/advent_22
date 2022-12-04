import csv
from enum import Enum
from dataclasses import dataclass

class OpponentMove(Enum):
    Rock = 'A'
    Paper = 'B'
    Scissors = 'C'

class MyCommandedMove(Enum):
    Loss = 'X'
    Draw = 'Y'
    Win = 'Z'

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
    my_commanded_move: MyCommandedMove
    my_move: str = None

    def determine_my_move(self):
        """
        Function to help determine my move based on whether I should
        win, lose, or draw. Iterates the rules dictionary and returns
        a matching move for each condition.
        """
        if self.my_commanded_move == MyCommandedMove.Draw:
            return self.opponent_move.name
        for winning_move, losing_move in move_beats.items():
            if winning_move == self.opponent_move.name:
                if self.my_commanded_move == MyCommandedMove.Loss:
                    return losing_move
            elif losing_move == self.opponent_move.name:
                if self.my_commanded_move == MyCommandedMove.Win:
                    return winning_move

    def score_round(self):
        self.my_move = self.determine_my_move()
        opponent_score = move_score[self.opponent_move.name]
        my_score = move_score[self.my_move]
        
        if move_beats[self.opponent_move.name] == self.my_move:
            opponent_score += 6
        elif move_beats[self.my_move] == self.opponent_move.name:
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
        round = Round(OpponentMove(opponent_move_encoded), MyCommandedMove(my_move_encoded))
        opponent_score, my_score = round.score_round()
        opponent_total_score += opponent_score
        my_total_score += my_score
        

print(f'Opponent total score: {opponent_total_score}\nMy total score: {my_total_score}')
