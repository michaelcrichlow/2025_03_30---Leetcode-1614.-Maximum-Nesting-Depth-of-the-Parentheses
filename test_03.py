def longestCommonPrefix(strs: list[str]) -> str:
    smallest_word = sorted(strs, key=len)[0]
    idx = len(smallest_word)
    while idx > 0:
        if all(val.startswith(smallest_word[:idx]) for val in strs):
            break
        else:
            idx -= 1
    
    return smallest_word[:idx]


def main() -> None:
    print(longestCommonPrefix(strs = ["flower","flow","flight"]))
    print(longestCommonPrefix(strs = ["dog","racecar","car"]))


if __name__ == '__main__':
    main()