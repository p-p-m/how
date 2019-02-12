# This approach was wrong. It does not allow to pass books over stundents

# class Student:
#     def __init__(self, start, end, books):
#         self.start = start
#         self.end = end
#         self.books = books
#         self.pages = sum(books[i] for i in range(self.start, self.end))

#     def can_expand_left(self, left_student):
#         left_book_pages = self.books[self.start - 1]
#         current_max = max(self.pages, left_student.pages)
#         new_max = max(self.pages + left_book_pages, left_student.pages - left_book_pages)
#         return current_max > new_max

#     def can_expand_right(self, right_student):
#         if right_student.end - right_student.start <= 1:
#             return False

#         right_book_pages = self.books[self.end]
#         current_max = max(self.pages, right_student.pages)
#         new_max = max(self.pages + right_book_pages, right_student.pages - right_book_pages)
#         return current_max > new_max

#     def expand_left(self, left_student):
#         assert self.start == left_student.end, 'Cannot expand left'
#         left_book_pages = self.books[self.start - 1]
#         self.start -= 1
#         left_student.end -= 1
#         self.pages += left_book_pages
#         left_student.pages -= left_book_pages

#     def expand_right(self, right_student):
#         assert self.end == right_student.start, 'Cannot expand right'
#         right_book_pages = self.books[self.end]
#         self.end += 1
#         right_student.start += 1
#         self.pages += right_book_pages
#         right_student.pages -= right_book_pages

#     def __repr__(self):
#         return '{}-{}({})'.format(self.start, self.end, self.pages)


# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def books(self, A, B):
#         if B > len(A):
#             return -1

#         students = []
#         for i in range(B):
#             if i != B - 1:
#                 students.append(Student(i, i + 1, A))
#             else:
#                 students.append(Student(i, len(A), A))

#         move_was_done = True
#         while move_was_done:
#             move_was_done = False
#             for i in range(1, B):
#                 right_student = students[-i]
#                 student = students[-i-1]
#                 while student.can_expand_right(right_student):
#                     student.expand_right(right_student)
#                     move_was_done = True

#         for s in

#         move_was_done = True
#         while move_was_done:
#             move_was_done = False
#             for i in range(1, B):
#                 left_student = students[i-1]
#                 student = students[i]
#                 while student.can_expand_left(left_student):
#                     student.expand_left(left_student)
#                     move_was_done = True


#         return max(student.pages for student in students)


# s = Solution()
# # A = [12, 67, 89, 34, 65, 29, 31]
# # B = 3
# A = [ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ]
# B = 26
# print s.books(A, B)


# # To formulate: move pointer left and

# # 12 67 89 34 65 29 31
# # 3

# # 12|67|89 34 65 29 31
# # 12|67|248
# # move second right

# # 12|67 89|34 65 29 31
# # 12 156   159
# # do not move second
# # move first right

# # 12 67|89 34|65 29 31
# # 89    133   159


# # 12 67 89 34 65|29|31

# # 12 67 89 34|65 29|31

# # 12 67 89|34 65 29|31

# 12 67 89 34 65 29 31


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # def books(self, A, B):
    #     if len(A) < B:
    #         return -1
    #     pps = sum(A)
    #     students_count = 1
    #     maxA = max(A)
    #     while pps >= maxA and students_count <= B:
    #         pps -= 1
    #         students_count, _max = self.get_stundents_count(pps, A)

    #     return self.get_stundents_count(pps + 1, A)[1]

    # def get_stundents_count(self, pps, A):
    #     bucket = 0
    #     _max = 0
    #     students_count = 1
    #     for pages in A:
    #         if bucket + pages > pps:
    #             bucket = pages
    #             students_count += 1
    #         else:
    #             bucket = bucket + pages
    #         if bucket > _max:
    #             _max = bucket
    #     return students_count, _max

    def books(self, A, B):
        if len(A) < B:
            return -1
        pps = max(A)
        step = sum(A) // 2
        while True:
            current_fit = self.fit(pps, A, B)
            previous_fit = self.fit(pps - 1, A, B)
            if current_fit and not previous_fit:
                return pps
            elif current_fit and previous_fit:
                pps -= step
            elif not current_fit and not previous_fit:
                pps += step
            else:
                raise Exception('Something is wrong')
            step = max(step // 2, 1)


    def fit(self, pps, A, B):
        count = B
        bucket = pps
        for pages in A:
            if pps < pages:
                return False
            if bucket - pages < 0:
                bucket = pps
                count -= 1
            bucket -= pages
            if count == 0:
                return False

        return True




s = Solution()
# A = [12, 67, 89, 34, 65, 29, 31]
# B = 3
# A = [ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ]
# B = 26
# A = [ 87, 3, 27, 29, 40, 12, 3, 69, 9, 57, 60, 33, 99 ]
# B = 3
# A = [ 12, 34, 67, 90 ]
# B = 2
# A = [ 53, 77, 8, 28, 33, 98, 81, 35, 13, 65, 14, 63, 36, 25, 69 ]
# B = 12
print s.books(A, B)



