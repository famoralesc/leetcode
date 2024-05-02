from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        i = 0
        while i < len(nums):
            j = len(nums) - 1
            while j > i:
                result = nums[i] + nums[j]
                if result == target:
                    solution.append(i)
                    solution.append(j)
                    return solution
                j -= 1
            i += 1
        return solution

if __name__ == '__main__':
    sol = Solution()
    inp = [2,7,11,15]
    inp2=9
    assert sol.twoSum(inp, inp2) == [0,1]
    inp = [3,2,4]
    inp2=6
    assert sol.twoSum(inp, inp2) == [1,2]
    inp = [3,3]
    inp2=6
    assert sol.twoSum(inp, inp2) == [0,1]