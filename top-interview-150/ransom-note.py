class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        for letter in ransomNote:
            ransomDict[letter] = ransomDict.get(letter, 0) + 1
        magazineDict = {}
        for letter in magazine:
            magazineDict[letter] = magazineDict.get(letter, 0) + 1
        can = False
        for k in ransomDict.keys():
            if k in magazineDict:
                if ransomDict[k] <= magazineDict[k]:
                    can = True
                    continue
                else:
                    can = False
                    break
            else:
                can = False
                break
        return can

if __name__ == '__main__':
    sol = Solution()
    inp = "a"
    inp2 = "b"
    assert sol.canConstruct(inp, inp2) == False
    inp = "aa"
    inp2 = "ab"
    assert sol.canConstruct(inp, inp2) == False
    inp = "aa"
    inp2 = "aab"
    assert sol.canConstruct(inp, inp2) == True
    inp = "bcb"
    inp2 = "cjjajdfaaeegig"
    assert sol.canConstruct(inp, inp2) == False