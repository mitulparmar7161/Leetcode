# 3097. Shortest Subarray With OR at Least K II
#
# Medium
#
# You are given an array nums of non-negative integers and an integer k.
#
# An array is called special if the bitwise OR of all of its elements is at least k.
#
# Return the length of the shortest special non-empty
# subarray
# of nums, or return -1 if no special subarray exists.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3], k = 2
#
# Output: 1
#
# Explanation:
#
# The subarray [3] has OR value of 3. Hence, we return 1.
#
# Example 2:
#
# Input: nums = [2,1,8], k = 10
#
# Output: 3
#
# Explanation:
#
# The subarray [2,1,8] has OR value of 11. Hence, we return 3.
#
# Example 3:
#
# Input: nums = [1,2], k = 0
#
# Output: 1
#
# Explanation:
#
# The subarray [1] has OR value of 1. Hence, we return 1.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 109
# 0 <= k <= 109
#
#
# Runtime 2097 ms Beats 100.00% Analyze Complexity

class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        min_length = float('inf')
        current_or = 0
        left = 0

        for right in range(n):
            current_or |= nums[right]

            while current_or >= k:
                min_length = min(min_length, right - left + 1)
                current_or ^= nums[left]
                left += 1

        return min_length if min_length != float('inf') else -1


obj = Solution()
print(obj.minimumSubarrayLength([2,1,8],10))