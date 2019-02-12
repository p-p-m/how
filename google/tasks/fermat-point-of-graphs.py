# XXX: THIS IS NOT A PROPER SOLUTION
# XXX: THIS TASK IS STILL IN PROGRESS

# [1,1,3,3,1,6,6,6,6,10,11,11,10,14,14]
# [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# [4732,17826,30531,722,14784,5975,2523,6433,23757,2943,26551,23002,28669,9502,10133]


class Solution:
    """
    @param x: The end points set of edges
    @param y: The end points set of edges
    @param d: The length of edges
    @return: Return the index of the fermat point
    """
    def getFermatPoint(self, x, y, d):
        self.distances = [{} for i in range(max(x + y))]  # format: <vertex-index, {distances}>
        for index, edge_value in enumerate(d):
            print 'x,y', x[index], y[index]
            print self.distances
            self.connect(x[index] - 1, y[index] - 1, edge_value)
        maxes = []
        for dist in self.distances:
            maxes.append(sum(dist.values()))
        return maxes.index(max(maxes)) + 1

    def connect(self, index_a, index_b, edge_value):
        self._connect_one_way(index_a, index_b, edge_value)
        for child_index, child_value in self.distances[index_a].items():
            self._connect_one_way(child_index, index_b, child_value + edge_value)
        self._connect_one_way(index_b, index_a, edge_value)
        for child_index, child_value in self.distances[index_b].items():
            self._connect_one_way(child_index, index_a, child_value + edge_value)

    def _connect_one_way(self, index_a, index_b, edge_value):
        print index_a, index_b
        try:
            current_distance = self.distances[index_a][index_b]
        except KeyError:
            current_distance = 10 ** 5 + 1  # more then available input maximum
        self.distances[index_a][index_b] = min(current_distance, edge_value)

    def get_children_indexes(self, parent_index):
        return self.distances[parent_index].keys()


s = Solution()
print s.getFermatPoint([1, 1, 2, 3, 4, 2], [2, 4, 3, 4, 5, 6], [1, 1, 1, 1, 1, 1])