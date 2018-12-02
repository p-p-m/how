from collections import defaultdict

t = {
    "value": -1,
    "left": {
        "value": 5,
        "left": None,
        "right": None
    },
    "right": {
        "value": 7,
        "left": None,
        "right": {
            "value": 1,
            "left": None,
            "right": None
        }
    }
}


def largestValuesInTreeRows(t):
    if t is None:
        return []

    def _get_children(v, level):
        return [
            (c, level + 1) for c in [v['left'], v['right']] if c is not None]

    to_review = [(t, 0)]
    result = defaultdict(list)
    for vertex, level in to_review:
        result[level].append(vertex['value'])
        to_review += _get_children(vertex, level)

    return [max(result[key]) for key in sorted(result.keys())]


print largestValuesInTreeRows(t)
