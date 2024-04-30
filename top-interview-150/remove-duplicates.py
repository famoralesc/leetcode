class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, limit = 0, 0, len(nums)
        while i<len(nums):
            j = i
            while j < limit:
                if j!=i and nums[j] == nums[i]:
                    del (nums[j])
                    limit -= 1
                else:
                    j += 1
            i += 1
        return len(nums)
    
if __name__ == '__main__':
    sol = Solution()
    inp = [1,1,2]
    assert sol.removeDuplicates(inp) == 2
    inp = [0,0,1,1,1,2,2,3,3,4]
    assert sol.removeDuplicates(inp) == 5
