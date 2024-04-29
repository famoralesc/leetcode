class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {
            "I":             1,
            "V":            5,
            "X":             10,
            "L":            50,
            "C":             100,
            "D":             500,
            "M":             1000
        }
        ops = []
        for i in range(len(s)):
            currentValue = romanMap[s[i]]
            if i + 1 == len(s):
                nextValue = romanMap[s[i]]
            else: 
                nextValue = romanMap[s[i + 1]]
            if currentValue < nextValue:
                ops.append(-currentValue)
            else:
                ops.append(currentValue)
        
        return sum(ops)

if __name__ == '__main__':
    sol = Solution()
    inp = "MCMXCIV"
    assert sol.romanToInt(inp) == 1994
    inp = "LVIII"
    assert sol.romanToInt(inp) == 58
    inp = "III"
    assert sol.romanToInt(inp) == 3
