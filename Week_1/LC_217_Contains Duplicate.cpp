#include <vector>
// #include <unordered_set>
#include <unordered_map>


// store elements that aren't in the set in the set, if element is alr in the sem, then it's being repeated, hence return True, if no element is alr in the set, it passes, hence return false


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // unordered_set<int> s;
        unordered_map<int,int> d;
        for (int i=0;i<nums.size();i++){
            if (d.count(nums[i])){
                return true;
            }
            d[nums[i]] = 1;
        }
        return false;
    }
};