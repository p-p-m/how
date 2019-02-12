# https://www.lintcode.com/problem/reverse-pairs/description

class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """

    def reversePairs(self, A):
        self.pairs_count = 0
        self.mergeSort(A)
        return self.pairs_count

    def sort(self, array):
        if len(array) < 2:
            return array
        left, right = self.sort(array[:len(array) // 2]), self.sort(array[len(array) // 2:])
        left_pointer, rigth_pointer = 0, 0
        result = []
        while True:

            try:
                left_value = left[left_pointer]
            except IndexError:
                result += right[rigth_pointer:]
                break

            try:
                rigth_value = right[rigth_pointer]
            except IndexError:
                result += left[left_pointer:]
                break

            if left_value > rigth_value:
                self.pairs_count += len(left[left_pointer:])
                rigth_pointer += 1
                result.append(rigth_value)
            else:
                left_pointer += 1
                result.append(left_value)

        return result

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # Finding the mid of the array
            L = arr[:mid]  # Dividing the array elements
            R = arr[mid:]  # into 2 halves

            self.mergeSort(L)  # Sorting the first half
            self.mergeSort(R)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] > R[j]:
                    arr[k] = R[j]
                    self.pairs_count += len(L[i:])
                    j += 1
                else:
                    arr[k] = L[i]
                    i += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

s = Solution()
print s.reversePairs([2, 4, 1, 3, 5])