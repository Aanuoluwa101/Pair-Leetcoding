"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

I used the two-pointer pattern.
The solution has a time complexity of O(n2)
"""

def two_sum(nums, target):
    for pointer_1 in range(len(nums)):
        pointer_2 = pointer_1 + 1 
        while pointer_2 < len(nums):
            if nums[pointer_1] + nums[pointer_2] == target:
                return [pointer_1, pointer_2]
            pointer_2 += 1


if __name__ == "__main__":
    nums, target = [2, 7, 11, 15], 9
    nums, target = [3,2,4], 6
    nums, target = [3,3], 6 
    print(two_sum(nums, target)) 
        