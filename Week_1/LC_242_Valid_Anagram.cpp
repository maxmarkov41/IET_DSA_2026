#include <map>
#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        map<char, int> x;
        
        for (int i = 0; i < s.size(); i++) {
            x[s[i]]++; 
            x[t[i]]--;
        }
        
        for (const auto& entry : x) {
            if (entry.second != 0) {
                return false;
            }
        }
        
        return true;
    }
};
