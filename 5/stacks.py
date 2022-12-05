import csv

def parse_file() -> tuple[list[str]]:
    moves: list[str] = []
    board_state: list[str] = []
    with open('stacks.csv', newline='') as csvfile:
        parsing_state = True    
        reader = csv.reader(csvfile)
        """
        The first lines denote the initial state, so we parse it (until the empty row):

                    ['        [C] [B] [H]                ']
                    ['[W]     [D] [J] [Q] [B]            ']
                    ['[P] [F] [Z] [F] [B] [L]            ']
                    ['[G] [Z] [N] [P] [J] [S] [V]        ']
                    ['[Z] [C] [H] [Z] [G] [T] [Z]     [C]']
                    ['[V] [B] [M] [M] [C] [Q] [C] [G] [H]']
                    ['[S] [V] [L] [D] [F] [F] [G] [L] [F]']
                    ['[B] [J] [V] [L] [V] [G] [L] [N] [J]']
                    [' 1   2   3   4   5   6   7   8   9 ']
                    []
                    ['move 5 from 4 to 7']    
        """
        for row in reader:
            if len(row) == 0:
                parsing_state = False
                continue
            if parsing_state:
                board_state.append(row)
            else:
                moves.append(row)

    return (board_state, moves)        

def setup_stacks(board_state: list[str]) -> list[list[str]]:
    cleaned_state = []
    for i in range(len(board_state)):
        line = board_state[i][0]
        cleaned_state.append(line[1::4])
    
    stacks: list[list, str] = [[] for _ in range(len(cleaned_state[-1]))] # initializing empty queues/stacks

    for i in range(len(cleaned_state)-2, -1, -1): # starting at the bottom of the pile, and skipping bottom enumerator
        row = cleaned_state[i]
        for j in range(len(row)): # j is the appropriate stack (horizontally in the picture above)
            if row[j] != ' ': # don't bother counting empty string, as they never represent any data
                stacks[j].append(row[j])

    return stacks

def print_state(stacks: list[str], moved_from: int | None = None, moved_to: int | None = None):
    print('-'*64)
    for i in range(len(stacks)):
        stack_str = ''
        for item in stacks[i]:
            stack_str += item
        if i == moved_from:
            stack_str += ' -->'
        if i == moved_to:
            stack_str += ' <--'
        print(stack_str)
    print('-'*64)

def parse_move(move: str) -> tuple[int, int, int]:
    split_move = move.split(' ')
    n, from_stack, to_stack = int(split_move[1]), int(split_move[3]) -1, int(split_move[5]) -1 # minusing one as 1 is zeroth stack etc
    return (n, from_stack, to_stack)

def perform_move(stacks: list[list[str]], move: tuple[int, int, int]) -> list[list[str]]:
    n, from_stack, to_stack = move
    for _ in range(n):
        cargo = stacks[from_stack].pop()
        stacks[to_stack].append(cargo)
    return stacks

def main() -> None:
    board_state, moves = parse_file()
    stacks = setup_stacks(board_state)
    print("Done parsing initial stacks (this way up -->)...")
    print_state(stacks)

    for move_command in moves:
        move = parse_move(move_command[0])
        stacks = perform_move(stacks, move)
        print_state(stacks, move[1], move[2])

if __name__ == '__main__':
    main()