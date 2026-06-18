//SELECTION SORT:

class Solution {

    public static void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    public static int min(int[] arr, int k) {
        int min = arr[k];
        int minIndex = k;
        for (int i = k; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
                minIndex = i;
            }
        }
        return minIndex;
    }

    public int[] selectionSort(int[] nums) {
        for (int i = 0; i <= nums.length - 2; i++) {
            int minIndex = min(nums, i);
            swap(nums, i, minIndex);
        }
        return nums;
    }
}




//************************************BUBBLE SORT*********************************************************
//TIME COMPLEXITY FOR WORST = O(N^2) AND THE BEST COMPLEXITY = O(N)
class Solution {
  
public static void swap(int []arr,int k,int l){
    int t=arr[k];
    arr[k]=arr[l];
    arr[l]=t;
}

   public static boolean it(int []arr,int k,boolean swapped){
        
    for(int i=1;i<arr.length-k;i++){
          if(arr[i-1]>arr[i]){
            swap(arr,i-1,i);
            swapped=true;
          }
    }

    return swapped;
   }

    public int[] bubbleSort(int[] nums) {
       
       for(int i=0;i<nums.length;i++){
        boolean swapped =false;
       boolean re= it(nums,i,swapped);

         if(!re){
            return nums;
        }
       }
        
       

       return nums;
    }
}

//*************************************************INSERTION SORT************************************** */
//TIME COMPLEXITY FOR WORST = O(N^2) AND THE BEST COMPLEXITY = O(N)

class Solution {

     public static void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    public int[] insertionSort(int[] nums) {


 for(int i=1;i<nums.length;i++){
    j=i;
    while(j>0 && nums[j-1]>nums[j]){
        swap(nums,j-1,j);
        j--;
    }

 }

 return nums;
    }
}

// MERGE SORT
 
class Solution:
 
    def mergeSort(self, arr, l, r):
        #code here
        
        if l>=r:
            return
        
        mid=(r+l)//2
        
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        
        
        self.merge(arr,l,mid,r)
        
        
        
    def merge(self,arr,l,mid,r):
        left=arr[l : mid + 1]
        right=arr[mid + 1 : r + 1]
        n1=mid-l+1
        n2=r-mid
        
        k=l
        
        for i in range(n1):
            left[i]=arr[k]
            k+=1
            
        # fill R
        for i in range(n2):
            right[i]=arr[k]
            k+=1
            
        i=0
        j=0
        k=l
        
        # MERGE THEM IN ARR
        while i<n1 and j<n2:
            if left[i]<right[j]:
                arr[k]=left[i]
                
                i+=1
            
            else:
                arr[k]=right[j]
                j+=1
                
            k+=1
            
            
        
        while i<n1:
            arr[k]=left[i]
            k+=1
            i+=1
            
        
        while j<n2:
            arr[k]=right[j]
            k+=1
            j+=1
                
            
        return
        

// QUICK SORT->https://www.geeksforgeeks.org/problems/quick-sort/1
// COMPLEXITY=O(nlog(n)) and in worst case=O(n^2) if its sorted and reverse

class Solution:
    def quickSort(self, arr, low, high):
        #code here 
        if low>=high:
            return 
        
        pIndex= self.partition(arr,low,high)
        
        self.quickSort(arr,low,pIndex-1)
        self.quickSort(arr,pIndex+1,high)
        

    def partition(self, arr, low, high):
        
        pivot=high
        pidex=low
        
        while low<high:
            if arr[low]<arr[pivot]:
                arr[pidex],arr[low]=arr[low],arr[pidex]
                pidex+=1
            
            low+=1     
                
        arr[pidex],arr[pivot]=arr[pivot],arr[pidex]
        
        return pidex
    
    