class Solution:
    def trap(self, height: List[int]) -> int:

        left = []
        high = 0
        for i in height :
            if i > high:
                high = i
            left.append(high)

        right = []
        high = 0
        for i in height[-1::-1] :
            if i > high:
                high = i
            right.insert(0,high)

        res = 0

        for l , r, h in zip(left,right,height):
            if l <= r:
                res += (l-h)
            elif r < l:
                res += (r-h)

        return res