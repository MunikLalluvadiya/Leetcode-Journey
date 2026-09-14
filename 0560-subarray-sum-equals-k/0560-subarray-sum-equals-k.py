class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        sum_freq = {0: 1}  # important: empty prefix sum occurs once

        for num in nums:
            curr_sum += num
            
            # if (curr_sum - k) exists in map, those subarrays sum to k
            if (curr_sum - k) in sum_freq:
                count += sum_freq[curr_sum - k]
            
            # record current running sum
            sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1

        return count