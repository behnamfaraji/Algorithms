# 130. Surrounded Regions

# Given an m x n matrix board containing 'X' and 'O',
# capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's
# in that surrounded region.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        visited = []
        rn = len(board)
        cn = len(board[0])
        for i in range(rn):
            if board[i][0] == 'O' and (i, 0) not in visited:
                visited.append((i, 0))
                board, visited = self.BFS(board, visited, i, 0)
            if board[i][cn-1] == 'O' and (i, cn-1) not in visited:
                visited.append((i, cn-1))
                board, visited = self.BFS(board, visited, i, cn-1)

        for j in range(cn):
            if board[0][j] == 'O' and (0, j) not in visited:
                visited.append((0, j))
                board, visited = self.BFS(board, visited, 0, j)
            if board[rn-1][j] == 'O' and (rn-1, j) not in visited:
                visited.append((rn-1, j))
                board, visited = self. BFS(board, visited, rn-1, j)

        for i in range(rn):
            for j in range(cn):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
        return board

    def BFS(self, board, visited, i, j):
        queue = []
        queue.append((i, j))
        while queue != []:
            w = queue.pop(0)
            neighbor = []
            if w[0] > 0 and board[w[0]-1][w[1]] == 'O':
                neighbor.append((w[0]-1, w[1]))

            if w[0] < len(board)-1 and board[w[0]+1][w[1]] == 'O':
                neighbor.append((w[0]+1, w[1]))

            if w[1] > 0 and board[w[0]][w[1]-1] == 'O':
                neighbor.append((w[0], w[1]-1))

            if w[1] < len(board[0])-1 and board[w[0]][w[1]+1] == 'O':
                neighbor.append((w[0], w[1]+1))
            for v in neighbor:
                if (v[0], v[1]) not in visited:
                    visited.append((v[0], v[1]))
                    queue.append((v[0], v[1]))
        return board, visited


if __name__ == '__main__':
    s = Solution()
    print(s.solve([["X", "X", "X", "X"],
                   ["X", "O", "O", "X"],
                   ["X", "X", "O", "X"],
                   ["X", "O", "X", "X"]]
                  )
          )
