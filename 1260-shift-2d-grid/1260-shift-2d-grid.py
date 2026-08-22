
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        a = len(grid)
        b = len(grid[0])

        flat = []
        for i in grid:
            for j in i:
                flat.append(j)

        k = k % len(flat)
        end = flat[-k:] if k != 0 else flat[:]
        start = flat[:-k] if k != 0 else []
        end.extend(start)

        result = []
        idx = 0
        for i in range(a):
            temp = []
            for j in range(b):
                temp.append(end[idx])
                idx += 1
            result.append(temp)
        return result

        
        