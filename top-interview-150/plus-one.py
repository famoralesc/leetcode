from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join([str(d) for d in digits])
        value = int(s)
        value += 1
        value = str(value)
        return [int(v) for v in value]
    
if __name__ == '__main__':
    sol = Solution()
    inp = [1,2,3]
    assert sol.plusOne(inp) == [1,2,4]
    inp = [4,3,2,1]
    assert sol.plusOne(inp) == [4,3,2,2]
    inp = [9]
    assert sol.plusOne(inp) == [1,0]