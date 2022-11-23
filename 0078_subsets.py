# Given an integer array nums of unique elements, return all possible
# subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return([[]])

        a = nums[:1]
        nums.pop(0)

        set_list = []
        for w in self.subsets(nums):
            set_list.append(w)
            set_list.append(w+a)
        return(set_list)


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
