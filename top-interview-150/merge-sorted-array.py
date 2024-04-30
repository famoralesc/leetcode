from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n + m - 1
        j = 0
        while i >= 0:
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1
            if j == n:
                break
            i -= 1
        nums1.sort()


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3 
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1]