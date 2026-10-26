class Solution:
    def decodeString(self, s: str) -> str:
        root = []
        current = root
        parse_stack = []
        number = 0

        # Parse the encoded string
        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)

            elif char == '[':
                parse_stack.append((current, number))
                current = []
                number = 0

            elif char == ']':
                parent, repeat = parse_stack.pop()
                parent.append((repeat, current))
                current = parent

            else:
                current.append(char)

        # Decode without recursion
        result = []
        work = [(root, 0, 1)]

        while work:
            nodes, index, remaining = work[-1]

            if index == len(nodes):
                if remaining == 1:
                    work.pop()
                else:
                    work[-1] = (nodes, 0, remaining - 1)
                continue

            node = nodes[index]
            work[-1] = (nodes, index + 1, remaining)

            if isinstance(node, str):
                result.append(node)
            else:
                repeat, children = node
                if repeat > 0 and children:
                    work.append((children, 0, repeat))

        return "".join(result)