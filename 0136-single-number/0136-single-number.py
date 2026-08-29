class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1

            elif num in nums:
                d[num] += 1

        for key, vel in d.items():
            if vel % 2 != 0:
                return (key)