# https://www.lintcode.com/problem/predict-the-winner/description


# class NumsState:

#     def __init__(self, left, right, is_first_move, first_score, second_score, parent):
#         self.left = left
#         self.right = right
#         self.is_first_move = is_first_move
#         self.first_score = first_score
#         self.second_score = second_score
#         self.parent = parent
#         self.children = []

#     @property
#     def is_final(self):
#         return self.left > self.right

#     def __repr__(self):
#         return '{}. FS: {}, SS: {}. {}'.format((self.left + self.right) // 2, self.first_score, self.second_score, self.is_first_move)

#     @property
#     def winner(self):
#         return 'first' if self.first_score > self.second_score else 'second'

#     def is_first_winner(self):
#         if not self.children:
#             return self.winner == 'first'
#         if self.is_first_move:
#             return any(child.is_first_winner() for child in self.children)
#         else:
#             return all(child.is_first_winner() for child in self.children)


# class Solution:
#     """
#     @param nums: nums an array of scores
#     @return: check if player 1 will win
#     """
#     def PredictTheWinner(self, nums):
#         self.nums = nums
#         root_state = NumsState(0, len(nums) - 1, is_first_move=True, first_score=0, second_score=0, parent=None)
#         states = [root_state]
#         for state in states:
#             if state.is_final:
#                 continue
#             states += self.get_next_states(state)
#         return root_state.is_first_winner()

#     def get_next_states(self, current_state):
#         is_first_move = not current_state.is_first_move
#         if current_state.left == current_state.right:
#             children = [
#                 NumsState(
#                     current_state.left + 1, current_state.right,
#                     is_first_move=is_first_move,
#                     first_score=current_state.first_score + self.nums[current_state.left] if not is_first_move else current_state.first_score,
#                     second_score=current_state.second_score + self.nums[current_state.left] if is_first_move else current_state.second_score,
#                     parent=current_state,
#                 )
#             ]
#         else:
#             children = [
#                 NumsState(
#                     current_state.left + 1, current_state.right,
#                     is_first_move=is_first_move,
#                     first_score=current_state.first_score + self.nums[current_state.left] if not is_first_move else current_state.first_score,
#                     second_score=current_state.second_score + self.nums[current_state.left] if is_first_move else current_state.second_score,
#                     parent=current_state,
#                 ),
#                 NumsState(
#                     current_state.left, current_state.right - 1,
#                     is_first_move=is_first_move,
#                     first_score=current_state.first_score + self.nums[current_state.right] if not is_first_move else current_state.first_score,
#                     second_score=current_state.second_score + self.nums[current_state.right] if is_first_move else current_state.second_score,
#                     parent=current_state,
#                 ),
#             ]
#         current_state.children = children
#         return children

# s = Solution()
# s.PredictTheWinner([1, 5, 233, 7])


class Solution:
    """
    @param nums: nums an array of scores
    @return: check if player 1 will win
    """
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[None] * n] * n
        for i, num in enumerate(nums):
            dp[i][i] = num

        for i in range(n - 1):
            dp[i][i + 1] = Math.max(nums[i], nums[i + 1])

        _sum = sum(nums)

        for l in range(3, n + 1):
            i = 0
            while i + l - 1 < n:


        for(int l = 3; l <= nums.length; l++){
            for(int i = 0; i + l - 1 < nums.length; i++){
                int j = i + l - 1;

                dp[i][j] =
                Math.max(Math.min(dp[i+1][j-1], dp[i+2][j]) + nums[i],
                Math.min(dp[i][j-2], dp[i+1][j - 1]) + nums[j]);
            }
        }

        return 2 * dp[0][nums.length-1] >= sum;

