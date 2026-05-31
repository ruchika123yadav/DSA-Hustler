// Brute Force 
import java.util.*;

class Solution {
    public void nextPermutation(int[] nums) {
        Set<List<Integer>> set = new HashSet<>();
        generate(nums, new ArrayList<>(), new boolean[nums.length], set);

        List<List<Integer>> res = new ArrayList<>(set);

        // Sort lexicographically
        Collections.sort(res, (a, b) -> {
            for (int i = 0; i < a.size(); i++) {
                if (!a.get(i).equals(b.get(i))) {
                    return a.get(i) - b.get(i);
                }
            }
            return 0;
        });

        // Convert nums → List
        List<Integer> curr = new ArrayList<>();
        for (int num : nums) curr.add(num);

        int idx = res.indexOf(curr);
        List<Integer> next = (idx == res.size() - 1) ? res.get(0) : res.get(idx + 1);

        // Copy back
        for (int i = 0; i < nums.length; i++) {
            nums[i] = next.get(i);
        }
    }

    private void generate(int[] nums, List<Integer> temp, boolean[] used, Set<List<Integer>> set) {
        if (temp.size() == nums.length) {
            set.add(new ArrayList<>(temp)); // removes duplicates
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;

            used[i] = true;
            temp.add(nums[i]);

            generate(nums, temp, used, set);

            temp.remove(temp.size() - 1);
            used[i] = false;
        }
    }
}

// Optimal Solution
class Solution {
    public void nextPermutation(int[] nums) {
        int size = nums.length;
        int breakPoint = -1;
        for (int i = size - 1; i >= 1; i--) {
            if (nums[i - 1] < nums[i]) {
                breakPoint = i - 1;
                break;
            }
        }

        if (breakPoint == -1){
            reverseArray(nums, 0, size-1);
            return ;
        }

        for (int i = size - 1; i >= breakPoint; i--) {
            if (nums[i] > nums[breakPoint]) {
                int temp = nums[i];
                nums[i] = nums[breakPoint];
                nums[breakPoint] = temp;
                break;
            }
        }

        reverseArray(nums, breakPoint + 1, size - 1);
        return ;

    }

    public void reverseArray(int[] nums, int left, int right) {
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left += 1;
            right -= 1;
        }
    }
}