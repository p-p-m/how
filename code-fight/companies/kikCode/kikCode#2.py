def kikCode(userId):
    bits = _to_bits(userId)
    bits = bits[::-1]
    return sum(
        [list(circle.show_sectors()) for circle in _to_circles(bits)], [])


def _to_bits(userId):
    bits = bin(int(userId))[2:]
    return '0' * (52 - len(bits)) + bits


class Sector(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Circle(object):

    def __init__(self, index):
        self.index = index
        self.sectors = []

    def add_sector(self, sector):
        if self.sectors and self.sectors[-1].end == sector.start:
            self.sectors[-1].end = sector.end
        else:
            self.sectors.append(sector)

    def close(self):
        if (
            len(self.sectors) > 1 and
            self.sectors[0].start == 0 and
            self.sectors[-1].end == 360
        ):
            self.sectors[-1].end = self.sectors[0].end + 360
            self.sectors = self.sectors[1:]

    def show_sectors(self):
        for sector in self.sectors:
            yield [[self.index, sector.start], [self.index, sector.end]]


def _to_circles(bits):
    sectors_length = [3, 4, 8, 10, 12, 15]
    start = 0
    for index, end in enumerate(sectors_length, start=1):
        sector_bits = bits[start:start + end]
        step = 360 / len(sector_bits)
        circle = Circle(index)
        for bit_index, bit in enumerate(sector_bits):
            if not int(bit):
                continue
            circle.add_sector(
                Sector(
                    start=bit_index * step,
                    end=(bit_index + 1) * step,
                )
            )
        circle.close()
        yield circle
        start = start + end


userId = '1851027803204441'

print kikCode(userId)
