def houseRobber(nums):
    if not nums:
        return 0
    first = 0
    second = nums[0]

    for num in nums[1:]:
        third = max(first + num, second)
        first = second
        second = third

    return second


print houseRobber([1, 1, 1])
