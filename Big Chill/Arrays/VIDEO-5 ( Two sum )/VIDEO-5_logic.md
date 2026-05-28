# Two Sum
-------------------------------------------------------------------------------------------------------------------------
## Brute Force
1) Take each variable from the array and check this with other variables in the array.
2) This can be acheived using two for loops, for each operation check whether the two variables add up to the sum.
3) If yes, then return those variables, else go with other variables.
4) If no pair is obtained, then return -1.

* Time Complexity : O(n^2)
* Space Complexity : O(1)

-------------------------------------------------------------------------------------------------------------------------
## Better Solution
1) create a map data structure to store the value along with the index of the integer.
2) for each variable check whether the complement is present in the map or not. Complement can be obtained by subtracting  the varaible from the target.
3) If found return both the variables else add the current variable along with its index in the map.

* Time Complexity : O(n)
* Space Complexity : O(n)


-------------------------------------------------------------------------------------------------------------------------
## Optimal 
1) Sort the array, then create two pointers, left and right.
2) Place left at the left corner of the array and right at the right most corner of the array.
3) If the sum of left and right pointer is less than the target value, move the left pointer by one.
4) If the sum of left and right pointer is greater than the target value, reduce the right pointer by one.
        Why we need to move left and right pointer because, the first half of the array contains lower values 
        but the second half of the array contains higher value, so if we. require low value to achieve the target 
        we increase left pointer and vice versa the right pointer.