# 2563. Count the Number of Fair Pairs
#
# Medium
#
# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
#
# A pair (i, j) is fair if:
#
# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper
#
#
# Example 1:
#
# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
# Example 2:
#
# Input: nums = [1,7,9,2,5], lower = 11, upper = 11
# Output: 1
# Explanation: There is a single fair pair: (2,3).
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums.length == n
# -109 <= nums[i] <= 109
# -109 <= lower <= upper <= 109



class Solution(object):
    def lowerBound(self, nums, bound):
        res = 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] <= bound:
                res += j - i
                i += 1
            else:
                j -= 1
        return res
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        return self.lowerBound(nums, upper) - self.lowerBound(nums, lower - 1)

obj = Solution()
print(obj.countFairPairs([0,1,7,4,4,5],3,6))