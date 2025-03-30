# Leetcode 1614. Maximum Nesting Depth of the Parentheses

def maxDepth(s: str) -> int:
    """
    Given a valid parentheses string s, return the nesting depth of s. 
    The nesting depth is the maximum number of nested parentheses.
    """
    depth = 0
    max_depth = 0

    for val in s:
        if val == "(":
            depth += 1
            if max_depth < depth:
                max_depth = depth
        elif val == ")":
            depth -= 1

    return max_depth


def main() -> None:
    print(maxDepth(s = "(1+(2*3)+((8)/4))+1"))  # 3
    print(maxDepth(s = "(1)+((2))+(((3)))"))    # 3
    print(maxDepth(s = "()(())((()()))"))       # 3


if __name__ == '__main__':
    main()
