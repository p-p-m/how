def _get_possible_moves(n, k):
        if n == 0:
            return []
        return [move for move in range(1, k + 1) if n - move >= 0]


def climbingStaircase(n, k):
    combinations = [([], n)]
    for combination, stairs_left in combinations:
        for move in _get_possible_moves(stairs_left, k):
            combinations.append((combination + [move], stairs_left - move))

    return sorted([
        combination for combination, stairs_left in combinations
        if stairs_left == 0
    ])


print climbingStaircase(4, 2)
