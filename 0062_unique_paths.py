# 62. Unique Paths
# There is a robot on an m x n grid. The robot is initially
# located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner
# (i.e., grid[m - 1][n - 1]). The robot can only move either
# down or right at any point in time.

# Given the two integers m and n, return the number
# of possible unique paths that the robot can take
# to reach the bottom-right corner.

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        A = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = A[i-1][j]+A[i][j-1]
        return A[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
