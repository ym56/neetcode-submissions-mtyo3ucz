class Solution {
public:
    vector<int> cntOfString (string& str) {
        vector<int> cnt(26, 0);
        for (char c : str) {
            cnt[c - 'a']++;
        }
        return cnt;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> groups;
        for (string& str : strs) {
            vector<int> cnt = cntOfString(str);
            groups[cnt].push_back(str);
        }
        vector<vector<string>> res;
        for (auto& [k, v] : groups) {
            res.push_back(v);
        }
        return res;
    }
};
