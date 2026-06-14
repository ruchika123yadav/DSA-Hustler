
# Brute Force (O(n³))
Iterate with three loops: pick indices i, j, k such that i < j < k.
Check if nums[i] + nums[j] + nums[k] == 0.
If yes, create a triplet.
Sort the triplet and store it in a Set to avoid duplicates.
Convert the set to a list and return.


# Better Approach – Hashing (O(n²))
Fix one element at index i.
Create a HashSet to track visited elements.
For each j > i, compute third = -(nums[i] + nums[j]).
If third exists in the set → valid triplet found.
Sort and store in a Set to remove duplicates.

# Optimal Approach – Two Pointer (O(n²))
Sort the array.
Fix one element at index i (skip duplicates).
Use two pointers: left = i+1, right = n-1.
Compute sum:
If sum == 0 → store triplet and skip duplicates
If sum < 0 → move left++
If sum > 0 → move right--
Repeat until left < right.
