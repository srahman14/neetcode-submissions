# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

from collections import Counter

class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        Counter_s = Counter(s)
        Counter_t = Counter(t) 

        return Counter_t == Counter_s

