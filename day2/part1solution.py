import functools

file = list(map(lambda x: x.split(' '), open('input.txt').read().split('\n')))


def get_main_score(round):
    winnings = ['A Y', 'B Z', 'C X']
    round_txt = ' '.join(round)
    if round_txt in winnings:
        return 6
    if abs(ord(round[0]) - ord(round[1])) == 23:
        return 3
    return 0


def get_secondary_score(round):
    return ord(round[1]) - 87


print(functools.reduce(lambda acc, round: acc + get_main_score(round) + get_secondary_score(round), file, 0))
