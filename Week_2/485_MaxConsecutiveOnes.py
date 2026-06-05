from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ctr = []
        ctr_i = 0
        for i in nums:
            if i == 1:
                ctr_i += 1
            else:
                ctr.append(ctr_i)
                ctr_i = 0
        ctr.append(ctr_i)
        return max(ctr)

## counts 1s, add 1 to a counter list when 0 is encountered, find max in the counter list

import re
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        strin = ''.join([str(i) for i in nums])
        rege = r"1{0,}"
        matches = re.findall(rege, strin)
        matches = [len(i) for i in matches]
        return max(matches)
# using regex

