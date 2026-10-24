class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev

            stack.append(i)

        return (res)
                