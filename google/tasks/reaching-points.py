class Solution:
    """
    @param sx: x for starting point
    @param sy: y for starting point
    @param tx: x for target point
    @param ty: y for target point
    @return: if a sequence of moves exists to transform the point (sx, sy) to (tx, ty)
    """
    def reachingPoints(self, sx, sy, tx, ty):
        while True:
            if tx == sx and ty == sy:
                return True
            if tx == ty:
                return False
            if tx < sx or ty < sy:
                return False
            tx, ty = self.next_step(tx, ty)
            print tx, ty

    def next_step(self, tx, ty):
        if tx < ty:
            return tx, ty - tx
        else:
            return tx - ty, ty

# import collections


# class Solution:
#     """
#     @param sx: x for starting point
#     @param sy: y for starting point
#     @param tx: x for target point
#     @param ty: y for target point
#     @return: if a sequence of moves exists to transform the point (sx, sy) to (tx, ty)
#     """
#     def reachingPoints(self, sx, sy, tx, ty):
#         queue = collections.deque([(sx, sy)])
#         visited = set([(sx, sy)])
#         while queue:
#             result = queue.popleft()
#             if result == (tx, ty):
#                 return True
#             for variant in self.get_variants(result[0], result[1], tx, ty):
#                 if variant in visited:
#                     continue
#                 queue.append(variant)
#                 visited.add(variant)
#         return False

#     def get_variants(self, sx, sy, tx, ty):
#         variants = []
#         if sx + sy <= tx and sy <= ty:
#             variants.append((sx + sy, sy))
#         if sx <= tx and sx + sy <= ty:
#             variants.append((sx, sx + sy))
#         return variants

s = Solution()
print s.reachingPoints(1, 1, 12356, 12315)
