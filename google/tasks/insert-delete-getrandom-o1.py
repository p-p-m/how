# https://www.lintcode.com/problem/insert-delete-getrandom-o1/description

import random


class RandomizedSet:

    def __init__(self):
        self.values = [None] * 2
        self.added_count = 0

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        is_inserted = self._insert_value(val, self.values)
        if is_inserted:
            self.added_count += 1
        self.resize_up()
        return is_inserted

    def _insert_value(self, val, values):
        index = self._get_index(val, size=len(values))
        while True:
            if values[index] is None:
                values[index] = val
                return True
            if values[index] == val:
                return False
            index += 1

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        index = self._get_index(val)
        while True:
            if self.values[index] is None:
                return False
            if self.values[index] == val:
                self.values[index] = None
                self.added_count -= 1
                return True
            index += 1

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        result = None
        while result is None:
            result = random.choice(self.values)
        return result

    def _get_index(self, val, size=None):
        if size is None:
            size = len(self.values)
        return hash(val) & size - 1

    def resize_up(self):
        if self.added_count * 3 < len(self.values) * 2:
            return
        new_values = [None] * 2 * len(self.values)
        for value in self.values:
            self._insert_value(value, new_values)
        self.values = new_values


s = RandomizedSet()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
print s.getRandom()
s.remove(2)
s.remove(2)
s.remove(3)
s.remove(4)
print s.getRandom()
