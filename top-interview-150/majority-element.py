from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        majority = len(nums) / 2
        freqDict = {}
        for num in nums:
            freq = freqDict.get(num, 0)
            freq += 1
            freqDict[num] = freq
        
        for value, freq in freqDict.items():
            if freq > majority:
                return value
        return major


if __name__ == '__main__':
    sol = Solution()
    inp = [3,2,3]
    assert sol.majorityElement(inp) == 3
    inp = [2,2,1,1,1,2,2]
    assert sol.majorityElement(inp) == 2