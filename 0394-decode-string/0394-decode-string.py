class Solution:
    def decodeString(self, s: str) -> str:

        def decode(i):
            result = ""

            while i < len(s):

                if s[i].isdigit():
                    num = 0

                    while s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1

                    i += 1  # Skip '['

                    text, i = decode(i)
                    result += text * num

                elif s[i] == ']':
                    return result, i + 1

                else:
                    result += s[i]
                    i += 1

            return result, i

        result, _ = decode(0)
        return result