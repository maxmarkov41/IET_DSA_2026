#include<iostream>
#include<stdio.h>
#include<unordered_map>
#include<string>
#include<vector>
using namespace std;

int findMaxConsecutiveOnes(vector<int>& nums) {
    int curr = 0;
    int max_cnt = 0;
    for (int r = 0; r < nums.size(); r++) {
        if (nums[r] == 1) {
            curr++;
        } else {
            curr = 0;
        }
        max_cnt = max(max_cnt, curr);
    }
    return max_cnt;
}
