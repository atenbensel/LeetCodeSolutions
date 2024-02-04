func maxProfit(prices []int) int {
    if len(prices) == 0 {
        return 0
    }

    maxProfit := 0
    minPrice := prices[0]

    for _, price := range prices[1:] {
        maxProfit = max(maxProfit, price-minPrice)
        minPrice = min(minPrice, price)
    }

    return maxProfit
}
