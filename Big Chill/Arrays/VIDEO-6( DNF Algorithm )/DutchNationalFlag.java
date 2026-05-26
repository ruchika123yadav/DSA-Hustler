// Sort an array of 0's 1's & 2's 

// Brute Force
import java.util.*;

class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 1, 1, 2};
        int ones = 0;
        int twoes = 0;
        int zeroes = 0;
        int size = arr.length;
        
        for(int i = 0; i < size; i++){
            if(arr[i] == 0){
                zeroes += 1;
            }else if(arr[i] == 1){
                ones += 1;
            }else{
                twoes += 1;
            }
        }
        
        for(int i = 0; i < size; i++){
            if(zeroes > 0){
                arr[i] = 0;
                zeroes -= 1;
            }else if(zeroes == 0 && ones > 0){
                arr[i] = 1;
                ones -= 1;
            }else if(zeroes == 0 && ones == 0 && twoes > 0){
                arr[i] = 2;
                twoes -= 1;
            }
        }
        
        System.out.println(Arrays.toString(arr));
    }
}


// Optimal 
// Online Java Compiler
// Use this editor to write, compile and run your Java code online

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] arr = { 1, 2, 0, 1, 1, 1, 2, 0, 0, 0 };
        int low = 0;
        int mid = 0;
        int high = arr.length - 1;

        while (mid <= high) {

            if (arr[mid] == 0) {

                // swap arr[low] and arr[mid]
                int temp = arr[low];
                arr[low] = arr[mid];
                arr[mid] = temp;

                low++;
                mid++;

            } else if (arr[mid] == 1) {
                mid++;
            } else {
                // swap arr[mid] and arr[high]
                int temp = arr[mid];
                arr[mid] = arr[high];
                arr[high] = temp;

                high--;
            }
        }
        
        System.out.println(Arrays.toString(arr));
    }
}