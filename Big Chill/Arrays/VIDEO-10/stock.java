// Best Time to Buy and Sell Stock 

class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0, maxProfit = 0;
        int size = prices.length;
        int stockPrice = prices[0];
        for(int i = 0; i < size; i++){
            profit = prices[i] - stockPrice;
            stockPrice = Math.min(stockPrice, prices[i]);
            maxProfit = Math.max(maxProfit, profit);
        }

        return maxProfit;
    }
}