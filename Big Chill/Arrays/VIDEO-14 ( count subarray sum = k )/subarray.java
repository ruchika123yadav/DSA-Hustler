// Brute Force
class Solution {
    public int subarraySum(int[] nums, int target) {
        int size = nums. length;
        int count = 0;
            for(int i = 0; i < size; i++){
                for(int j= i; j < size; j++){
                int sum = 0;
                    for(int k = i; k <= j; k++){
                        sum += nums[k];
                    }
                    if(sum == target) count += 1;
                }
            
            }
        
        return count;
    }
}

// Better Solution
class Solution
    public int subarraySum(int[] nums, int target) {
        int size = nums. length;
        int count = 0;
        for(int i = 0; i < size; i++){
            int sum = 0;
            for(int j= i; j < size; j++){
                sum += nums[j];
                if(sum == target) count += 1;
            }
        }
        return count;
    }
}

// Optimal Solution
import java.util.HashMap;

class Solution {
    public int subarraySum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int prefixSum = 0;
        int count = 0;
        for (int num : nums) {
            prefixSum += num;
            if (map.containsKey(prefixSum - target)) {
                count += map.get(prefixSum - target);
            }
            map.put(prefixSum, map.getOrDefault(prefixSum, 0) + 1);
        }
        return count;
    }
}


