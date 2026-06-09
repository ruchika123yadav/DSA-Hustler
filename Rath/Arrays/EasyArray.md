# Array Data Structures & Algorithms: Logic Cheat Sheet

This document outlines the step-by-step logic and intuition for 9 classic array interview problems, optimizing for clarity, edge cases, and time complexity.

---

## 1. Find the Largest Element in an Array
**Approach:** Single Pass / Linear Scan ($O(N)$ Time, $O(1)$ Space)

* **Step 1:** Initialize a variable `max` and assign it the value of the first element of the array (`nums[0]`).
* **Step 2:** Iterate through the array using a loop starting from the second element (index `1`) to the end of the array.
* **Step 3:** Inside the loop, check if the current element (`nums[i]`) is greater than `max`.
* **Step 4:** If `nums[i] > max`, update the value of `max` to `nums[i]`. Otherwise, do nothing and proceed to the next iteration.
* **Step 5:** Once the loop terminates, return the final value of `max`.

---

## 2. Find the Second Largest Element in an Array
**Approach:** Two-Pass Linear Scan with Boundary Check ($O(N)$ Time, $O(1)$ Space)

* **Step 1:** Run a standard linear scan to find the maximum element in the array and store it in a variable named `maxEl`.
* **Step 2:** Initialize a variable `secLargest` to the minimum possible integer value (`Integer.MIN_VALUE`) and a boolean variable `flag` to `true`.
* **Step 3:** Start iterating through the array again from index `0`.
* **Step 4:** For each element, check the condition: `if (nums[i] > secLargest && nums[i] < maxEl)`.
  * This ensures that the element is strictly smaller than the absolute maximum but larger than our currently tracked second largest value.
* **Step 5:** If the condition is met, update `secLargest = nums[i]` and toggle `flag = false` (indicating that a distinct second largest element exists).
* **Step 6:** After the loop finishes, check the value of `flag`. If it remains `true`, it means no distinct second largest element exists (all elements are identical). Otherwise, return `secLargest`.

---

## 3. Check if an Array is Sorted and Rotated
**Approach:** Counting the Breaks in Ascending Order ($O(N)$ Time, $O(1)$ Space)

* **Step 1:** Initialize a counter variable `cnt = 0` to track how many times the ascending order rule is violated.
* **Step 2:** Iterate through the array from index `0` to `N-2` and check if the current element is greater than the next element (`nums[i] > nums[i+1]`). If it is, increment `cnt`.
* **Step 3:** Check the boundary condition for a rotated array: compare the last element with the first element. If `nums[N-1] > nums[0]`, increment `cnt` by 1.
  * *Exception:* If the array is already perfectly sorted without any rotation, this boundary check will not increment the count.
* **Step 4:** At the end, verify if `cnt <= 1`. If true, return `true` (the array is validly sorted and rotated); otherwise, return `false`.

---

## 4. Remove Duplicates from a Sorted Array
**Approach:** Two-Pointer Technique / In-place Modification ($O(N)$ Time, $O(1)$ Space)

* **Step 1:** Initialize two pointers. Place the first pointer `i` (slow pointer) at index `0` and the second pointer `j` (fast pointer) at index `1`.
* **Step 2:** Iterate through the array by continuously incrementing the fast pointer `j`.
* **Step 3:** In each iteration, compare the values at both pointers: `if (nums[i] != nums[j])`.
* **Step 4:** When a non-equal (new unique) element is detected:
  * Increment the slow pointer `i` by 1 (`i++`).
  * Copy the value of `nums[j]` to this new position: `nums[i] = nums[j]`.
* **Step 5:** Repeat this process until `j` reaches the end of the array. The first `i + 1` elements of the array will now contain all the unique values in their original sorted order.

---

## 5. Rotate Array by K Places
**Approach:** Three-Step Reversal Rule ($O(N)$ Time, $O(1)$ Space)

* **Step 1:** Handle cases where the rotation factor `K` is greater than the length of the array `N` by taking the modulus: `K = K % N`. This eliminates redundant full-circle rotations.
* **Step 2:** Reverse the entire array from index `0` to `N - 1`.
* **Step 3:** Reverse the first part of the inverted array containing `K` elements, from index `0` to `K - 1`.
* **Step 4:** Reverse the remaining part of the array from index `K` to `N - 1`.
* **Step 5:** After these three selective reversal operations, the array will be perfectly shifted by `K` places.

---

## 6. Move Zeroes to the End of the Array
**Approach:** Two-Pointer Partitioning without Extra Space ($O(N)$ Time, $O(1)$ Space)

* **Step 1:** Initialize a pointer `j = 0` which will track and maintain the position where the next non-zero element should be placed.
* **Step 2:** Use a loop pointer `i` to scan the array from index `0` to `N - 1`.
* **Step 3:** For every iteration, check if the current element is a non-zero value: `if (nums[i] != 0)`.
* **Step 4:** If `nums[i]` is non-zero, swap the elements at index `i` and index `j`: `swap(nums[i], nums[j])`.
* **Step 5:** Right after swapping, increment the pointer `j` (`j++`) so that the next non-zero value is accumulated at the correct subsequent index. This effectively pushes all zeroes towards the end while keeping the relative order of non-zero elements intact.

---

## 7. Union of Two Sorted Arrays
**Approach:** Utilizing Set Properties for Uniqueness ($O((M+N) \log(M+N))$ Time, $O(M+N)$ Space)

* **Step 1:** Instantiate a standard unique collection data structure like a `Set` (e.g., `HashSet` or `TreeSet` depending on sorting requirements).
* **Step 2:** Loop through the first array and insert every single element into the set.
* **Step 3:** Loop through the second array and insert all of its elements into the exact same set. The set data structure automatically filters out duplicate entries.
* **Step 4:** Create an empty dynamic list/array.
* **Step 5:** Iterate over the unique elements stored inside the set, add them sequentially into the list, and return that list as the final result.

---

## 8. Find the Missing Number
**Approach:** Gauss' Mathematical Sum Formula ($O(N)$ Time, $O(1)$ Space)

* **Step 1:** Traverse the given array to calculate the actual mathematical sum of all the elements present in it. Store this value in a variable (e.g., `actualSum`).
* **Step 2:** Determine the expected sum of the first `N` natural numbers using the standard algebraic formula:
  $$\text{Expected Sum} = \frac{N \times (N + 1)}{2}$$
* **Step 3:** Subtract the `actualSum` from the calculated `Expected Sum`.
* **Step 4:** The resultant scalar value obtained from the subtraction is your explicit missing number.

---

## 9. Max Consecutive Ones
**Approach:** Linear Scan with Dynamic Reset Counter ($O(N)$ Time, $O(1)$ Space)

* **Step 1:** Initialize two variables: a temporary tracker `count = 0` (to maintain the current consecutive streak of 1s) and a global tracker `maxCount = 0` (to store the longest sequence found so far).
* **Step 2:** Loop through the array from start to end.
* **Step 3:** Evaluate the value of the current element in each iteration:
  * `if (nums[i] == 1)`: Simply increment the temporary `count++`.
  * `else`: If a `0` is encountered, it means the current chain of 1s is broken. Update the global max with `maxCount = max(maxCount, count)` and reset the temporary tracker `count = 0`.
* **Step 4:** After exiting the loop, perform one final conditional calculation to handle edge cases where the array ends on a continuous stream of 1s: `return max(maxCount, count)`.


<!-- SINGLE NUMBER -->

This question is pritty much goof becuase i solved this question by using ht xor logic means that if we xor a number with itself it will give the value it will return 1 and if we xor a number with 1 we will get that number so bascially it will return only the unique elemenet while traversing in the entire whole array

<!-- longest subarrayw ith sum k -->

hmm in this question bascially i used the sliding window appraoch means I used 2 pointers in which the right pointer expands the window by addind element, we contnously check if the total sum has excedded the target value. When the sum becomes too large, the left pointer shrinks the window from the frint by subtracting elements until the sum falls back within bounds, once the window stablized I will check if the current sum is equal to our target or not and then calculte the max length

NOTE-> but this is only for the positive intergers only