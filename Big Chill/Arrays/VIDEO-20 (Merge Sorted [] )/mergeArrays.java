// Brute Force

class Solution {
    public void mergeArrays(int a[], int b[]) {
        // code here
        int aSize = a.length;
        int bSize = b.length;
        int totalSize = aSize + bSize;
        int[] res = new int[totalSize];
        int left = 0, right = 0;
        int pointer = 0;
        
        while(left < aSize && right < bSize){
            if(a[left] <= b[right]){
                res[pointer++] = a[left];
                left += 1;
            }else{
                res[pointer++] = b[right];
                right += 1;
            }
        }
        
        while(left < aSize){
            res[pointer++] = a[left];
            left += 1;
        }
        
        while(right < bSize){
            res[pointer++] = b[right];
            right += 1;
        }
        
        for(int i = 0; i < totalSize; i++){
            if(i < aSize){
                a[i] = res[i];
            }else{
                b[i - aSize] = res[i];
            }
        }
        
        return ;
    }
}


// Optimal Solution
class Solution {
    public void mergeArrays(int a[], int b[]) {
        // code here
        int aSize = a.length;
        int bSize = b.length;
        int left = aSize - 1, right = 0;

        
        while(left >= 0 && right < bSize){
            if(a[left] >= b[right]){
                int temp = a[left];
                a[left] = b[right];
                b[right] = temp;
                left -= 1;
            }else{
                break;
            }
            right += 1;
        }
        
        Arrays.sort(a);
        Arrays.sort(b);
        
        return ;
    }
}
