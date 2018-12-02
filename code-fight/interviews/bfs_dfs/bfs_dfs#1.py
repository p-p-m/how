t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": None,
            "right": None
        },
        "right": None
    }
}


def traverseTree(t):
    if t is None:
        return []

    def _get_children(v):
        return [c for c in [v['left'], v['right']] if c is not None]

    to_review = [t]
    result = []
    for vertex in to_review:
        result.append(vertex['value'])
        to_review += _get_children(vertex)

    return result


print traverseTree(t)
