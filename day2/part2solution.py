import functools

file = list(map(lambda x: x.split(' '), open('input.txt').read().split('\n')))

winner = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

loser = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

def get_score(round):
    if round[1] == 'X':
        return ord(loser[round[0]]) - 64
    if round[1] == 'Y':
        return 3 + ord(round[0]) - 64
    return 6 + ord(winner[round[0]]) - 64

print(functools.reduce(lambda acc, round: acc + get_score(round), file, 0))
