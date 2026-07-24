class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int right = 0, left = 0;
        int size = s.length();
        int maxLen = 0;

        while(right < size){
            char current = s.charAt(right);
            if(map.containsKey(current) && map.get(current) >= left){
                left = map.get(current) + 1;
            }
            maxLen = Math.max(maxLen, right - left + 1);
            map.put(current, right);
            right += 1;
        }

        return maxLen;
    }
}