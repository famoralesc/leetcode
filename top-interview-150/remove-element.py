from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        limit = len(nums)
        while i < limit:
            if nums[i] == val:
                del nums[i]
                if len(nums) == 0:
                    break
                limit -= 1
            else:
                i += 1
        return i
    
if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    expectedNums = [2,2]
    s = Solution()
    k = s.removeElement(nums, val)

    assert k == len(expectedNums)
    nums.sort()
    for i in range(k):
        assert nums[i] == expectedNums[i]
    