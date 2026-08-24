class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))  
        high = nums[0]
        count = 1
        totl = 1

        for i in nums[1:]:
            if i == high + 1:
                count += 1
            else:
                count = 1
            totl = max(totl, count)
            high = i

        return totl