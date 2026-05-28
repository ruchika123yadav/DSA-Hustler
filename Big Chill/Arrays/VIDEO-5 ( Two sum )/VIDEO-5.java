// Two  Sum Problem

***********************************************************************************************************************************************
// Brute Force
import java.util.*;

class Main {
    public static void main(String[] args){
        int[] arr = {2, 5, 6, 8, 11};
        int target = 14;
        
        int size = arr.length;
        
        for(int i = 0; i < size; i++){
            for(int j = i + 1; j < size; j++){
                if(arr[i] + arr[j] == target){
                    System.out.println(arr[i] + " " + arr[j]);
                    break;
                }
            }
        }
        
    }
}


***********************************************************************************************************************************************
// Better 
import java.util.*;

class Main {
    public static void main(String[] args){
        int[] arr = {2, 5, 6, 8, 11, 3};
        int target = 14;
        
        HashMap<Integer, Integer> map = new HashMap<>();
        int size = arr.length;
        int sum = 0;
        
        for(int i = 0; i < size; i++){
            sum = arr[i];
            int remaining = target - sum;
            
            if(map.containsKey(remaining)){
                System.out.println(sum + " " + remaining);
            }
            
            map.put(sum, i);
        }
        
    }
}

***********************************************************************************************************************************************
// Optimal
import java.util.*;

class Main {
    public static void main(String[] args){
        int[] arr = {2, 5, 6, 8, 11, 3};
        int target = 14;
        
        Arrays.sort(arr);
        int left = 0, right = arr.length - 1;
        
        while(left < right){
            int current = arr[left] + arr[right];
            if( current == target){
                System.out.println(arr[left] +" "+ arr[right]);
                break;
            }else if(current < target){
                left += 1;
            }else{
                right -= 1;
            }
        }
        
    }
}