
// brute force 

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