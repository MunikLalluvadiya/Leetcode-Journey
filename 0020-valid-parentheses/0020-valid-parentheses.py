class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its matching opening bracket
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in bracket_map:
                # It's a closing bracket
                top = stack.pop() if stack else '#'
                if bracket_map[ch] != top:
                    return False
            else:
                # It's an opening bracket
                stack.append(ch)

        # Valid only if no unmatched opening brackets remain
        return not stack