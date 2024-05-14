def isAnagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Runtime 49 ms
    Beats 58.10% of users with Python3

    Memory 17.04 MB
    Beats 33.77% of users with Python3

    Examples
    -------
    >>> isAnagram(s = "anagram", t = "nagaram")
    True
    >>> isAnagram(s = "rat", t = "car")
    False
    """
    
    if len(s) != len(t):
        return False
    dT = {}
    dS = {}
    for idx in range(len(s)):
        inS = dS.get(s[idx], 0)
        dS[s[idx]] = inS + 1
        
        inT = dT.get(t[idx], 0)
        dT[t[idx]] = inT + 1

    for kS in dS.keys():
        if kS in dT and dS[kS] == dT[kS]:
            continue
        else:
            return False
    return True