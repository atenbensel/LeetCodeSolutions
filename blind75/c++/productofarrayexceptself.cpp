class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        vector<int> answer(length);
        answer[0] = 1;
        for (int i = 1; i < length; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }
        int R = 1;
        for (int i = length - 1; i >= 0; i--) {
            answer[i] = answer[i] * R;
            R *= nums[i];
        }
        return answer;
    }
};
