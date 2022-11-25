# 986. Interval List Intersections
# You are given two lists of closed intervals,
# firstList and secondList, where firstList[i] = [starti, endi]
# and secondList[j] = [startj, endj].
# Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers
# that are either empty or represented as a closed interval.
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = j = 0
        A = []
        while i < len(firstList) or j < len(secondList):
            if i == len(firstList):
                break
            if j == len(secondList):
                break
            if not(firstList[i][1] < secondList[j][0] or secondList[j][1] < firstList[i][0]):

                A.append([max(firstList[i][0], secondList[j][0]),
                          min(firstList[i][1], secondList[j][1])])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1
            else:
                if firstList[i][1] < secondList[j][0]:
                    i += 1
                else:
                    j += 1
        return A


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]])
    )
