class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> ttoi;

        for (int i = 0; i < nums.size(); i++) {
            if (ttoi.count(nums[i])) {
                return {ttoi[nums[i]], i};
            }
            ttoi[target - nums[i]] = i;
        }
    }
};
