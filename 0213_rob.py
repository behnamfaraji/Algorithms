# 213. House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        A = [0]*(len(nums)-1)
        A[0] = nums[0]
        A[1] = max(nums[0:2])
        for i in range(2, len(nums)-1):
            A[i] = max([A[i-1], A[i-2]+nums[i]])

        B = [0]*(len(nums)-1)
        B[0] = nums[1]
        B[1] = max(nums[1:3])
        for i in range(3, len(nums)):
            B[i-1] = max([B[i-2], B[i-3]+nums[i]])

        return(max([A[-1], B[-1]]))


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 2]))
