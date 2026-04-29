from itertools import combinations_with_replacement, product

def normalize(state):
    p1 = tuple(sorted(state[:2]))
    p2 = tuple(sorted(state[2:]))
    return (*p1, *p2)

def get_winner(state):
    if state[0] == 0 and state[1] == 0:
        return 1
    if state[2] == 0 and state[3] == 0:
        return -1
    return 0

def get_possible_states():
    pairs = list(combinations_with_replacement(range(5), 2))
    pairs.pop(0)    
    states = [(a, b, c, d) for (a, b), (c, d) in product(pairs, repeat=2)]
    return states

def get_possible_moves(state):
    moves = set()
    state = normalize(state)

    #actions = ["LL", "LR", "RL", "RR"]

    for i in range(2):
        if state[i] == 0:
            continue
        for j in range(2, 4):
            if state[j] == 0:
                continue

            new_state = list(state)
            new_state[j] = (state[i] + state[j]) % 5
            moves.add(normalize(tuple(new_state)))

    if state[0] == 0 and state[1] in [2, 4]:
        split_state = (state[1]//2, state[1]//2, state[2], state[3])
        split_moves = get_possible_moves(split_state)
        moves.update(split_moves)

    #print(list(moves))
    return moves

def search(states):
    winners = []
    for state in states:
        next_states = get_possible_moves(state)
        for next_state in next_states:
            result = get_winner(next_state)
            if result == -1:
                winners.append(state)
                break
    print(winners)
    print(len(winners))

if __name__ == '__main__':
    states = get_possible_states()
    moves = get_possible_moves((1, 1, 1, 2))
    search(states)