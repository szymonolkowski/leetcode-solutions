from math import factorial
def nPr(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

class Solution:
    def climbStairs(self, n: int) -> int:
        perms = 1
        dwojaki = 1
        m = n
        n-=1
        while  dwojaki * 2 <= m:
            perms += nPr(n,dwojaki)
            dwojaki += 1
            n-=1

        return perms