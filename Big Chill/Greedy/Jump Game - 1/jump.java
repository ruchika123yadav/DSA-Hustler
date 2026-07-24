class Solution {
    public boolean canJump(int[] nums) {
        int size = nums.length;

        if(size == 1) return true;

        int maxVal = 0;
        for(int i = 0; i < size; i++){
            if(i > maxVal) return false;
            maxVal = Math.max(maxVal, nums[i] + i);
        }

        return true;
    }
}