# https://leetcode.com/problems/contains-duplicate/solutions/3672475/4-methods-c-java-python-beginner-friendl-zozw
from typing import List

# store elements that aren't in the set in the set, if element is alr in the sem, then it's being repeated, hence return True, if no element is alr in the set, it passes, hence return false

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        di = {}
        for i in nums:
            if i in di:
                return True
            di[i] = 1
        return False
            
"""