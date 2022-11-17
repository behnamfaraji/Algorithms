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
