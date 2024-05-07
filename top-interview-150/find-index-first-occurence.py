
def strStr(haystack: str, needle: str) -> int:
    """Given two strings needle and haystack, 
    return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:

    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.
    Example 2:

    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.
    
    Examples
    -------
    >>> strStr("sadbutsad", "sad")
    0
    >>> strStr("leetcode", "leeto")
    -1
    """
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:len(needle) + i] == needle:
                return i
    return -1

if __name__ == '__main__':
    inp1 = "sadbutsad"
    inp2 = "sad"
    assert strStr(inp1, inp2) == 0

    inp1 = "leetcode"
    inp2 = "leeto"
    assert strStr(inp1, inp2) == -1
