#include<bits/stdc++.h>
#include<unordered_set>

using namspace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

	for (int num : nums) {
		if (seen.find(num) != seen.end()) {
			return true
		}
		seen.insert(num);
	}
	return false;
    }
};

