class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function productExceptSelf($nums) {
        $length = count($nums);
        $answer = array_fill(0, $length, 1);
        for ($i = 1; $i < $length; $i++) {
            $answer[$i] = $nums[$i - 1] * $answer[$i - 1];
        }
        $R = 1;
        for ($i = $length - 1; $i >= 0; $i--) {
            $answer[$i] = $answer[$i] * $R;
            $R *= $nums[$i];
        }
        return $answer;
    }
}
