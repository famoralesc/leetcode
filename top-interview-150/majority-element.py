from typing import List

def majorityElement(nums: List[int]) -> int:
    """Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.

    Example 1:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    
    Examples
    -------
    >>> majorityElement([3,2,3])
    3
    >>> majorityElement([2,2,1,1,1,2,2])
    2
    """
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
    inp = [3,2,3]
    assert majorityElement(inp) == 3
    inp = [2,2,1,1,1,2,2]
    assert majorityElement(inp) == 2