# from collections import defaultdict
# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # d1,d2 = defaultdict(int),defaultdict(int)
        # for i in s:
        #     d1[i] += 1
        # for j in t:
        #     d1[j] -= 1
        # for i in d1.values():
        #     if i:return False
        # return True
        # return Counter(s) == Counter(t)
        if len(s) != len(t) or set(s) != set(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True

# an anagram is a word or phrase formed by rearranging letters of a different word
# if len(s) != len(t), it's not an anagram, it set(s) is not equal to set(t), it's not an anagram, if the count of individual elements is not equal, it's not an anagram.
        