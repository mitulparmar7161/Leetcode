# 2593. Find Score of an Array After Marking All Elements

# Medium

# You are given an array nums consisting of positive integers.
#
# Starting with score = 0, apply the following algorithm:
#
# Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
# Add the value of the chosen integer to score.
# Mark the chosen element and its two adjacent elements if they exist.
# Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.
#
#
#
# Example 1:
#
# Input: nums = [2,1,3,4,5,2]
# Output: 7
# Explanation: We mark the elements as follows:
# - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
# - 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
# - 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
# Our score is 1 + 2 + 4 = 7.
# Example 2:
#
# Input: nums = [2,3,5,1,3,2]
# Output: 5
# Explanation: We mark the elements as follows:
# - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
# - 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
# - 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
# Our score is 1 + 2 + 2 = 5.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
#
#


class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sum, r=0, 0
        while r<n:
            l=r
            while r+1<n and nums[r]>nums[r+1]:
                r+=1
            for i in range(r, l-1, -2):
                sum+=nums[i]
            r+=2
        return sum


obj = Solution()
print(obj.findScore([2,1,3,4,5,2]))