def get_level_professions(level):
    professions = 0
    for i in range(level):
        if i == 0:
            professions = 1
        elif i == 1:
            professions = 2
        else:
            half_level_bits = int(2 ** i) / 2
            _reversed = professions ^ (2 ** half_level_bits - 1)
            professions = (professions << half_level_bits) + _reversed
    return bin(professions)[2:]


print get_level_professions(6)
# print bin(9)
# print bin(9 ^ 15)

print '0101'.count('1')
