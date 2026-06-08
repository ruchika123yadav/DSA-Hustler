// Online Java Compiler
// Use this editor to write, compile and run your Java code online

// Brute Force
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();
        int size = nums.length;
        for(int i = 0; i < size; i++){
            int current = nums[i];
            int count = 0;
            for(int j = 0; j < size; j++){
                if(current == nums[j]){
                    count += 1;
                }
            }
            if(count > (size/3) && !res.contains(current)){
                res.add(current);
            }
        }

        return res;
    }
}

// Better Solution
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        int arrLength = nums.length;

        for(int i = 0; i < arrLength; i++){
            int current = nums[i];
            map.put(current, map.getOrDefault(current, 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            if(entry.getValue() > arrLength / 3){
                int res = entry.getKey();
                if(!list.contains(res)) list.add(res);
            }
        }
        return list;
    }
}

// Optimal Solution
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int cnt1 = 0, cnt2 = 0;
        int ele1 = -1, ele2 = -1;
        int n = nums.length;
        List<Integer> res = new ArrayList<>();
        for(int i = 0; i < n; i++){
            if(cnt1 == 0 && ele2 != nums[i]){
                ele1 = nums[i];
                cnt1 = 1;
            }else if(cnt2 == 0 && ele1 != nums[i]){
                ele2 = nums[i];
                cnt2 = 1;
            }else if(nums[i] == ele1){
                cnt1 += 1;
            }else if(nums[i] == ele2){
                cnt2 += 1;
            }else{
                cnt1 -= 1;
                cnt2 -= 1;
            }
        }
        cnt1 = 0;
        cnt2 = 0;

        for(int num : nums){
            if(num == ele1) cnt1++;
            else if(num == ele2) cnt2++;
        }

        if(cnt1 > n/3) res.add(ele1);
        if(cnt2 > n/3) res.add(ele2);

        return res;
    }
}