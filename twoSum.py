
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, w in enumerate(nums):
            dic[w] = i
        print(dic)
        for i, w in enumerate(nums):
            if target-w in dic.keys():
                if i != dic[target-w]:
                    return([i,dic[target-w]])
