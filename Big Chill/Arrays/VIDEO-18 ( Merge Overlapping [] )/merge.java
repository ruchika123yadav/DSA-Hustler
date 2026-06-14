// Brute Force
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        int size = intervals.length;
        List<int[]> res = new ArrayList<>();

        for(int i = 0; i < size; i++){
            int start = intervals[i][0];
            int end = intervals[i][1];
            if(!res.isEmpty() && res.get(res.size() - 1)[1] >= end ) continue;
            for(int j = i + 1; j < size; j++){
                if(end >= intervals[j][0]){
                    end = intervals[j][1];
                }else{
                    break;
                }
            }
            res.add(new int[] {start, end});
        }
        

        int[][] arr = new int[res.size()][];

        for (int i = 0; i < res.size(); i++) {
            arr[i] = res.get(i);
        }

        return arr;
    }
}


// Optimal Solution
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        int size = intervals.length;
        List<int[]> res = new ArrayList<>();

        for(int i = 0; i < size; i++){
            if(res.isEmpty() || res.get(res.size() - 1)[1] < intervals[i][0]){
                res.add(intervals[i]);
            }else{
                res.get(res.size() - 1)[1] = Math.max(res.get(res.size() - 1)[1], intervals[i][1]);
            }
        }
        

        int[][] arr = new int[res.size()][];

        for (int i = 0; i < res.size(); i++) {
            arr[i] = res.get(i);
        }

        return arr;
    }
}
