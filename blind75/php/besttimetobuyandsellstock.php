class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        if (empty($prices)) {
            return 0;
        }
        
        $maxProfit = 0;
        $minPrice = $prices[0];

        foreach ($prices as $price) {
            $maxProfit = max($maxProfit, $price - $minPrice);
            $minPrice = min($minPrice, $price);
        }

        return $maxProfit;
    }
}
