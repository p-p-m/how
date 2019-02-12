class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sum = -1
        max_list = []
        current_sum = 0
        current_list = []
        for el in A + [-1]:
            if el >= 0:
                current_sum += el
                current_list.append(el)
            else:
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_list = current_list
                current_sum = 0
                current_list = []
        return max_list

s = Solution()
print s.maxset([0, 0, -1, 0])
