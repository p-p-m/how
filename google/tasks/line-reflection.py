class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """
    def isReflected(self, points):
        if not points:
            return True
        sorted_points = sorted(points)
        n = len(sorted_points)
        left = sorted_points[:n // 2]
        right = sorted(sorted_points[(n + 1) // 2:], key=lambda x: [-x[0], x[1]])
        nearest_left = left[-1]
        neares_right = right[-1]
        middle_x = (nearest_left[0] + neares_right[0]) / 2.0 if nearest_left[0] != neares_right[0] else nearest_left[0]
        if n % 2 != 0:
            middle = sorted_points[(n - 1) // 2]
            if middle[0] != middle_x:
                return False
        for left_el, right_el in zip(left, right):
            if left_el[0] == right_el[0] == middle_x:
                continue
            distance = right_el[0] - left_el[0]
            if right_el[1] == left_el[1] and right_el[0] - distance / 2.0 == middle_x:
                continue
            print middle_x, right_el[0] - distance / 2.0, distance / 2, left_el, right_el
            return False
        return True

points = [[20,0],[21,2],[24,10],[29,18],[36,36],[45,55],[56,48],[69,98],[84,112],[101,153],[120,130],[141,132],[164,216],[189,221],[216,210],[245,345],[276,352],[309,374],[344,486],[381,551],[420,420],[461,525],[504,572],[549,690],[596,672],[645,875],[696,910],[749,999],[804,868],[861,1073],[920,930],[981,1054],[1044,1216],[1109,1419],[1176,1462],[1245,1435],[1316,1548],[1389,1665],[1464,1786],[1541,1638],[1620,1760],[1701,1722],[1784,1932],[1869,2279],[1956,2112],[2045,2070],[2136,2162],[2229,2585],[2324,2544],[2421,2891],[20,0],[19,2],[16,10],[11,18],[4,36],[-5,55],[-16,48],[-29,98],[-44,112],[-61,153],[-80,130],[-101,132],[-124,216],[-149,221],[-176,210],[-205,345],[-236,352],[-269,374],[-304,486],[-341,551],[-380,420],[-421,525],[-464,572],[-509,690],[-556,672],[-605,875],[-656,910],[-709,999],[-764,868],[-821,1073],[-880,930],[-941,1054],[-1004,1216],[-1069,1419],[-1136,1462],[-1205,1435],[-1276,1548],[-1349,1665],[-1424,1786],[-1501,1638],[-1580,1760],[-1661,1722],[-1744,1932],[-1829,2279],[-1916,2112],[-2005,2070],[-2096,2162],[-2189,2585],[-2284,2544],[-2381,2891]]
s = Solution()
print s.isReflected(points)
