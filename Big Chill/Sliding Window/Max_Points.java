class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int maxPoints = Integer.MIN_VALUE;
        int n = cardPoints.length;
        int leftSum = 0, rightSum = 0;

        for(int i = 0; i < k; i++){
            leftSum += cardPoints[i];
        }

        maxPoints = leftSum;

        for(int i = 0; i < k; i++){
            rightSum += cardPoints[n - 1 - i];
            leftSum -= cardPoints[k - i - 1];
            maxPoints = Math.max(maxPoints,rightSum + leftSum);
        }

        return maxPoints;
    }
}