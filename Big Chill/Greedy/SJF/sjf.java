class Solution {
    static int solve(int bt[]) {
        // code here
        Arrays.sort(bt);
        int waitingTime = 0, currentTime = 0;
        
        for(int i = 0; i < bt.length; i++){
            waitingTime += currentTime;
            currentTime += bt[i];
        }
        
        return waitingTime/(bt.length);
    }
}
