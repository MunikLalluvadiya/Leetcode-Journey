class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its matching opening bracket
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in bracket_map:
               
                top = stack.pop() if stack else '#'
                if bracket_map[ch] != top:
                    return False
            else:
            
                stack.append(ch)

      
        return not stack