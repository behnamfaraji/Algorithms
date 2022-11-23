# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = 0
        for i in range(len(nums)-1):
            if nums[i] == 0 and max_index <= i:
                return False
            else:
                max_index = max([max_index, i+nums[i]])
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([5, 2, 0, 1, 2, 0, 3, 10]))
