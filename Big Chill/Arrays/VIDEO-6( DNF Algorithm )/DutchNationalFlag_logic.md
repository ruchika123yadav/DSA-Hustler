# Sort 0's, 1's and 2's
-------------------------------------------------------------------------------------------------------------------------
## Brute Force
1) create variables to store the count of ones, twoes and zeroes
2) Iterate through the array and store the count.
3) Again iterate thorugh the array and replace the values in the based on the count of variables, starting from 0, 1 and 2.

* Time Complexity : O(n) + O(n)
* Space Complexity : O(1)

-------------------------------------------------------------------------------------------------------------------------
## Optimal 

### Dutch National Flag Algorithm

~ Assumption : There are three pointers low, mid and high.
0 --> low - 1 : 0's
low --> mid - 1 : 1's
mid --> high : UNSORTED VALUES
high - 1 --> n : 2's

1) create three pointers low, mid and high. Iterate the array using mid
2) if mid pointer has 0, swap it with low pointer and move low and mid pointer.
3) if mid pointer has 1,  just move mid pointer alone
4) if mid pointer has 2, swap it with high and move high by -1 (reduce by 1).
        Why dont we move mid in last case ? Since the array is not sorted, high might contain other values like 1, 0, which should be place in appropriate position, which can be done once we assign this to mid.
