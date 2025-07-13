# 862. Shortest Subarray with Sum at Least K
#
# Hard
#
# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [1], k = 1
# Output: 1
# Example 2:
#
# Input: nums = [1,2], k = 4
# Output: -1
# Example 3:
#
# Input: nums = [2,-1,2], k = 3
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= k <= 109


class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = float("inf")

        cur_sum = 0
        q = deque()

        for r in range(len(nums)):
            cur_sum += nums[r]
            if cur_sum >= k:
                res = min(res, r + 1)

            while q and cur_sum - q[0][0] >= k:
                prefix, end_idx = q.popleft()
                res = min(res, r - end_idx)

            while q and q[-1][0] > cur_sum:
                q.pop()
            q.append((cur_sum, r))

        return -1 if res == float("inf") else res

obj = Solution()
print(obj.shortestSubarray([2,-1,2],3))