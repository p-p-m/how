def hasPathWithGivenSum(t, s):

    def _is_leaf(v):
        return v['left'] is None and v['right'] is None

    def _get_children(v):
        return [c for c in [v['left'], v['right']] if c is not None]

    to_review = [t]
    for vertex in to_review:
        value = vertex['value']
        if _is_leaf(vertex) and value == s:
            return True

        children = _get_children(vertex)
        for child in children:
            child['value'] += value
            to_review.append(child)

    return False


t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None
            }
        },
        "right": None
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": None,
                "right": None
            },
            "right": {
                "value": -3,
                "left": None,
                "right": None
            }
        }
    }
}

print(hasPathWithGivenSum(t, 9))
