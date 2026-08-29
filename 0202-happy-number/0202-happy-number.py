class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def calculate(n):
            l = []
            while n > 0:
                last = n % 10
                l.append(last)
                n //= 10
            return l

        while True:
            if n in seen:
                return False
                break
            seen.add(n)
            lis = calculate(n)
        

            t = 0
            for i in lis:
                t += i ** 2

            if t == 1:
                return True
                break
            else:
                n = t