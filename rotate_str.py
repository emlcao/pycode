"""
Q: Rotate an array of n elements to the right by k steps.
Example:
n = 7, k = 3
a = [1, 2, 3, 4, 5, 6, 7]
output: [5, 6, 7, 1, 2, 3, 4]
Input: nums: list[int], k: int
Output: nums
Edge cases:
k > len(a)
a = []

Idea: slice the end of list

"""

def rotate_arr(nums, k):
    if nums == []:
        return []
    else:
        k = k % len(nums) # in case k > len(nums)
        nums = nums[-k:] + nums[:-k]
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
output = [5, 6, 7, 1, 2, 3, 4]
res = rotate_arr(nums, k)
assert(res == output)
