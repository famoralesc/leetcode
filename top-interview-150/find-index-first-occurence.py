class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:len(needle) + i] == needle:
                    return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    inp1 = "sadbutsad"
    inp2 = "sad"
    assert sol.strStr(inp1, inp2) == 0

    inp1 = "leetcode"
    inp2 = "leeto"
    assert sol.strStr(inp1, inp2) == -1
