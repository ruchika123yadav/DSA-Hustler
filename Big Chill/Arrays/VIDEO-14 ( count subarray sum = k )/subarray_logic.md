For the Subarray Sum Equals K problem:
Given an integer array nums and an integer k, return the number of continuous subarrays whose sum equals k.
1. Brute Force Approach
Logic
Generate all possible subarrays.
For each subarray, calculate its sum.
If the sum equals k, increment the count.

2. Better Approach
Logic
Instead of recalculating the sum for every subarray, maintain a running sum while extending the subarray.
This removes the third loop.


3. Optimal Approach (Prefix Sum + HashMap)
Logic
If:

currentPrefixSum - previousPrefixSum = k
Then:

previousPrefixSum = currentPrefixSum - k
So, while traversing the array:
Maintain the current prefix sum.
Check whether (prefixSum - k) already exists.
If it exists, all occurrences of that prefix sum contribute to valid subarrays.
Store frequency of prefix sums in a HashMap.