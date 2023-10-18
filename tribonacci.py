def tribonacci(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        if n>=3:
            return (tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3))
