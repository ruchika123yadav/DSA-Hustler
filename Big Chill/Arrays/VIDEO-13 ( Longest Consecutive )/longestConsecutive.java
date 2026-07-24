
class Solution {
    public int longestConsecutive(int[] nums) {
        int longest = 1;
        int size = nums.length;

        for(int i = 0; i < size; i++){
            int count = 1;
            int target = nums[i];
            while(linearSearch(nums, target + 1)){
                target += 1;
                count += 1;
            }
            longest = Math.max(longest, count);
        }
        return longest;
    }

    public boolean linearSearch(int[] nums, int x){
        for(int num : nums){
            if(num == x) return true;
        }
        return false;
    }
}

// Better
import java.util.Arrays;

class Solution {
    public int longestConsecutive(int[] nums) {

        if (nums.length == 0)
            return 0;

        Arrays.sort(nums);

        int longest = 1;
        int count = 1;

        for (int i = 1; i < nums.length; i++) {

            if (nums[i] == nums[i - 1]) {
                continue; // skip duplicates
            }

            if (nums[i] == nums[i - 1] + 1) {
                count++;
            } else {
                count = 1;
            }

            longest = Math.max(longest, count);
        }

        return longest;
    }
}

// Optimal
import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        
        // Step 1: Add all elements to set
        for (int num : nums) {
            set.add(num);
        }

        int longest = 0;

        // Step 2: Traverse set
        for (int num : set) {
            // Only start if it's the beginning of sequence
            if (!set.contains(num - 1)) {
                int current = num;
                int count = 1;

                // Expand forward
                while (set.contains(current + 1)) {
                    current++;
                    count++;
                }

                longest = Math.max(longest, count);
            }
        }

        return longest;
    }
}