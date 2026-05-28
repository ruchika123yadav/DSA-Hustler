// Best Time to Buy and Sell Stock 

class Solution {
    public int maxProfit(int[] prices) {
        int buying = prices[0], max_profit = 0;
        for (int i = 1; i <= prices.length - 1; i++) {
            int profit = prices[i] - buying;
            max_profit = max_profit > profit ? max_profit : profit;
            buying = buying > prices[i] ? prices[i] : buying;
        }
        return max_profit;
    }
}