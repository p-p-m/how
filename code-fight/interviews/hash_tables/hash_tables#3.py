from collections import defaultdict


def containsCloseNums(nums, k):
    d = defaultdict(list)
    for index, num in enumerate(nums):
        d[num].append(index)

    for num, indexes in d.items():
        is_close = any(
            second - first <= k
            for first, second in zip(indexes, indexes[1:])
        )
        if is_close:
            return True

    return False


print containsCloseNums([0, 1, 2, 3, 5, 2], 2)
