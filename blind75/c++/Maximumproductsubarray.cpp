#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0;

        int max_product = nums[0];
        int min_product = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            int temp_max = max_product;
            max_product = max(nums[i], max(nums[i] * max_product, nums[i] * min_product));
            min_product = min(nums[i], min(nums[i] * temp_max, nums[i] * min_product));
            result = max(result, max_product);
        }
        return result;
    }
};
