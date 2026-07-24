// Brute Force
class Solution {
    public long subarrayXor(int nums[], int target) {
        // code here
        long cnt = 0;
        int size = nums.length;

        for(int i = 0; i < size; i++){
            for(int j = i; j < size; j++){
                int xor = 0;
                for(int k = i; k <= j; k++){
                    xor ^= nums[k];
                }
                if(xor == target) cnt += 1;
            }
        }

        return cnt; 
    }
}


// Better Solution
class Solution {
    public long subarrayXor(int nums[], int target) {
        // code here
        long cnt = 0;
        int size = nums.length;

        for(int i = 0; i < size; i++){
            int xor = 0;
            for(int j = i; j < size; j++){
                xor ^= nums[j];
                if(xor == target) cnt += 1;
            }
        }

        return cnt; 
    }
}


// Optimal Solution
class Solution {
    public long subarrayXor(int nums[], int target) {
        // code here
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int size = nums.length;
        int sum = 0;
        long cnt = 0;
        
        for(int i = 0; i < size; i++){
            sum ^= nums[i];
            int required = target ^ sum;
            if(map.containsKey(required)){
                cnt += map.get(required);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        
        return cnt;
    }
}

