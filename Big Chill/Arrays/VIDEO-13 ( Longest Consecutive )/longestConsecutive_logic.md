# Longest Consecutive Sequence

## 1. Brute Force Approach

### Steps

1. Traverse every element in the array.
2. Consider the current element as the starting point of a sequence.
3. Use linear search to check whether the next consecutive element `(current + 1)` exists.
4. Continue extending the sequence until the next number is not found.
5. Store the length of the current sequence.
6. Update the maximum sequence length.

### Time Complexity

- Outer loop runs `N` times.
- For each element, linear search takes `O(N)`.
- In the worst case, this search is performed for many consecutive elements.

**Time Complexity: O(N²)**

### Space Complexity

No extra data structure is used.

**Space Complexity: O(1)**

---

## 2. Better Approach (Sorting)

### Steps

1. Sort the array.
2. Initialize:
   - `count = 1`
   - `longest = 1`
3. Traverse the sorted array from index `1`.
4. If the current element is equal to the previous element:
   - Skip it (duplicate).
5. If the current element is exactly `1` greater than the previous element:
   - Increment `count`.
6. Otherwise:
   - Start a new sequence by setting `count = 1`.
7. Update `longest` after every iteration.
8. Return `longest`.

### Time Complexity

- Sorting: `O(N log N)`
- Array traversal: `O(N)`

**Time Complexity: O(N log N)**

### Space Complexity

No additional data structure is required (ignoring sorting space).

**Space Complexity: O(1)**

---

## 3. Optimal Approach (HashSet)

### Steps

1. Insert all array elements into a HashSet.
2. Traverse each element in the HashSet.
3. Check whether `(num - 1)` exists:
   - If it exists, skip the element because it is not the start of a sequence.
   - If it does not exist, it is the beginning of a new sequence.
4. Start counting the sequence length.
5. Continuously check whether `(current + 1)` exists in the HashSet.
6. Extend the sequence while consecutive numbers are present.
7. Update the maximum sequence length.
8. Return the longest sequence length.

### Time Complexity

- Building HashSet: `O(N)`
- Traversing HashSet: `O(N)`
- Each element is processed at most once.

**Time Complexity: O(N)**

### Space Complexity

HashSet stores all elements.

**Space Complexity: O(N)**

---

