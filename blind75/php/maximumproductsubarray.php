class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProduct($nums) {
        if (empty($nums)) return 0;

        $max_product = $nums[0];
        $min_product = $nums[0];
        $result = $nums[0];

        $length = count($nums);
        for ($i = 1; $i < $length; $i++) {
            $temp_max = $max_product;
            $max_product = max($nums[$i], $nums[$i] * $max_product, $nums[$i] * $min_product);
            $min_product = min($nums[$i], $nums[$i] * $temp_max, $nums[$i] * $min_product);
            $result = max($result, $max_product);
        }
        return $result;
    }
}
