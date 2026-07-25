class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        for (int num : nums) {
            cnt[num]++;
        }
        vector<vector<int>> buckets(nums.size() + 1, vector<int>());
        for (auto&[k, v]: cnt) {
            buckets[v].push_back(k);
        }

        vector<int> res;
        for (int i = buckets.size() - 1; i >= 0; i--) {
            for (int j = 0; j < buckets[i].size(); j++) {
            if (res.size() == k) {
                return res;
            }
            res.push_back(buckets[i][j]);
            }
        }

        return res;
    }
};
