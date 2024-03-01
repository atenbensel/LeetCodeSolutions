class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSubArray($nums) {
        $max_sum = $nums[0];
        $current_sum = $nums[0];

        $length = count($nums);
        for ($i = 1; $i < $length; $i++) {
            $current_sum = max($nums[$i], $current_sum + $nums[$i]);
            $max_sum = max($max_sum, $current_sum);
        }
        return $max_sum;
    }
}
