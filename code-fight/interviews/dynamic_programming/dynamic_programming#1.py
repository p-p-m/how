# 1 - 1
# 2 - 2

# 3 - 1:1 + 2:2 = 3
# 4 - 3:3 + 2:2 = 5
# 5 - 4:5 + 3:3 = 8


def climbingStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    two_ago_value = 1
    one_ago_value = 2
    index = 2

    while index < n:
        current_value = one_ago_value + two_ago_value
        two_ago_value = one_ago_value
        one_ago_value = current_value
        index += 1

    return current_value


print climbingStairs(38)
