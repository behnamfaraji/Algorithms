# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['()']

        A = []
        for v in self.generateParenthesis(n-1):
            if '()'+v not in A:
                A.append('()'+v)
            if v + '()' not in A:
                A.append(v + '()')
            for i, s in enumerate(v):
                if s == '(':
                    if v[:i+1] + '()' + v[i+1:] not in A:

                        A.append(v[:i+1] + '()' + v[i+1:])
        return A


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(5))
