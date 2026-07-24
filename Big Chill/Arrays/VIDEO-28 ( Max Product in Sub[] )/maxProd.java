// Brute Force

class Solution {
    public int maxProduct(int[] nums) {
        int size = nums.length;
        int maxValue = Integer.MIN_VALUE;

        for(int i = 0; i < size; i++){
            int prod = 1;
            for(int j = 0; j < size; j++){
                prod *= nums[j];
                maxValue = Math.max(maxValue, prod);
            }
        }

        return maxValue;
    }
}


// Optimal Solution
class Solution {
    public int maxProduct(int[] nums) {
        int size = nums.length;
        int maxValue = Integer.MIN_VALUE;
        int sufix = 1, prefix = 1;

        for(int i = 0; i < size; i++){
            
            sufix *= nums[size - 1 - i];
            prefix *= nums[i];
            
            maxValue = Math.max(maxValue, Math.max(prefix, sufix));

            if(sufix == 0) sufix = 1;
            if(prefix == 0) prefix = 1;
        }

        return maxValue;
    }
}