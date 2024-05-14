def wordPattern(pattern: str, s: str) -> bool:
    """
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

    Runtime 39 ms
    Beats 23.26% of users with Python3
    Memory 16.56 MB
    Beats 61.62% of users with Python3
    Examples
    -------
    >>> wordPattern(pattern = "abba", s = "dog cat cat dog")
    True
    >>> wordPattern(pattern = "abba", s = "dog cat cat fish")
    False
    >>> wordPattern(pattern = "aaaa", s = "dog cat cat dog")
    False
    """
    pos = 0
    sList = s.split(" ")
    if len(sList) != len(pattern):
        return False
    d = {pattern[0] : str(pos)}
    newPattern = ""
    newS = ""
    for idx in range(len(pattern)):
        k = d.get(pattern[idx], None)
        if not k and k != 0:
            pos += 1
            d[pattern[idx]] = str(pos)
        newPattern = newPattern + d[pattern[idx]]
    
    pos = 0
    d = {sList[0] : str(pos)}
    for idx in range(len(sList)):
        k = d.get(sList[idx], None)
        if not k and k != 0:
            pos += 1
            d[sList[idx]] = str(pos)
        newS = newS + d[sList[idx]]
    return newS == newPattern
