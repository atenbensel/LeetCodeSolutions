class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $numMap = array();
        for ($i = 0; $i < count($nums); $i++) {
            $complement = $target - $nums[$i];
            if (array_key_exists($complement, $numMap)) {
                return array($numMap[$complement], $i);
            }
            $numMap[$nums[$i]] = $i;
            
        }
        
    }
}
