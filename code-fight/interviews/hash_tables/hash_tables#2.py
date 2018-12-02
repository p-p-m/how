def areFollowingPatterns(strings, patterns):
    pattern_as_key = {}
    string_as_key = {}
    for string, pattern in zip(strings, patterns):
        if pattern in pattern_as_key and pattern_as_key[pattern] != string:
            return False
        if string in string_as_key and string_as_key[string] != pattern:
            return False
        pattern_as_key[pattern] = string
        string_as_key[string] = pattern
    return True


strings = ["cat", "dog", "dog"]
patterns = ['a', 'b', 'c']


print areFollowingPatterns(strings, patterns)
