class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        for i in B:
            ans.append(self.numk(A, i))
        return ans

    def numk(self, A, k):
        c = 1
        k -=1
        while k>0:
            step = self.get_steps(A, c)
            if step <= k:
                c+=1
                k-=step
            else:
                c*=10
                k-=1
        return c

    def get_steps(self, A, c):
        step = 0
        c1 = c
        c2 = c+1
        while c1 <= A:
            step += min(A+1, c2) - c1
            c1 *=10
            c2 *=10
        return step



s = Solution()
interval = s.get_interval(25, 0)
print interval

# f = ['1', '10', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '11', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '12', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '13', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '14', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '15', '16', '17', '18', '19']
# print len(f)
