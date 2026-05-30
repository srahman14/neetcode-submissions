# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

from collections import Counter

class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        Counter_s = Counter(s)
        Counter_t = Counter(t) 

        return Counter_t == Counter_s

# Sort the strings - then compare each character
# since the order does not matter
class Solution2: 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        # Sort the strings then iterate through both 
        # while comparing characters

        sorted_s = sorted(s)
        sorted_t = sorted(t)
            
        return sorted_s == sorted_t

# Use of Hashmap
# O(n + m) time complexity, O(1) space
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        countS, countT = {}, {} 

        # Store every character and its frequency 
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = 1 + countS.get(t[i], 0)

        # If the frequencies are the same return true
        # else false
        return countS == countT

# Use of Hash Table 
# O(n + m) time complexity, O(1) space
class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 
            count[ord(t[i]) - ord('a')] += 1 
        
        for val in count:
            if val != 0:
                return False
        
        return True
