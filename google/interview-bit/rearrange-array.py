a = [4, 0, 2, 1, 3]
# a2 = [None] * 5

# for i in range(5):
#     a2[i] = a[a[i]]

# print a2

# def get_old(a, i):
#     return a[i] % 5

# for i in range(5):
#     a[i] += get_old(a, get_old(a, i)) * 5
# for el in a:
#     print el // 5


class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        for i in range(len(A)):
            A[i] += self.get_old(A, self.get_old(A, i)) * len(A)
        for i in range(len(A)):
            A[i] = A[i] // len(A)
        return A

    def get_old(self, A, i):
        return A[i] % len(A)

s = Solution()
print s.arrange(a)
