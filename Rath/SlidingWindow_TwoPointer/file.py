# Longest Substring without repeating Character->https://leetcode.com/problems/longest-substring-without-repeating-characters/
# COMPLEXITY=O(2n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique=set()

        left=0
        right=0
        maxLength=0

        while right<len(s):

            if s[right] in unique:

                while s[left]!=s[right]:
                    unique.remove(s[left])
                    left+=1
                left+=1
                    
            unique.add(s[right])             
            maxLength=max(maxLength,right-left+1)
            right+=1


        return maxLength



# MAX CONSECUTIVE ONES||| ->https://leetcode.com/problems/max-consecutive-ones-iii/description/

# complexity=O(2n)
# BETTER SOLUTION
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        if len(nums)==1 and nums[0]==1:
            return 1

        right=0
        left=0
        maxLength=0
        zero=0

        while right<len(nums):
            if nums[right]==0:
                zero+=1

            if zero>k:
                while nums[left]!=0:
                    left+=1
                left+=1
                zero-=1

            maxLength=max(maxLength,right-left+1)

            right+=1


        return maxLength
            

# OPTIMAL SOLUTION-O(n)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        if len(nums)==1 and nums[0]==1:
            return 1

        right=0
        left=0
        maxLength=0
        zero=0

        while right<len(nums):
            if nums[right]==0:
                zero+=1

            if zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
                         
            if zero<=k:
                maxLength=max(maxLength,right-left+1)

            right+=1


        return maxLength
            

# LONGEST REAPEATING CHARACTER REPLACEMENT->https://leetcode.com/problems/longest-repeating-character-replacement/description/
# COMPLEXITY=O(2n)
    

    class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hm={}

        right=0
        left=0
        maxLen=0
        maxFreq=0

        while right<len(s):
            hm[s[right]]=hm.get(s[right],0)+1
            maxFreq=max(maxFreq,hm[s[right]])
            
            while (right-left+1)-maxFreq>k:
                hm[s[left]]-=1
                maxFreq=max(hm.values())
                left+=1

             
            maxLen=max(maxLen,right-left+1)
            right+=1

        return maxLen


        
# BINARY SUBARRAY WITH SUM->https://leetcode.com/problems/binary-subarrays-with-sum/description/
# COMPLEXITY=O(2n)
        

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        if len(nums)==1 and (nums[0]>goal or nums[0]<goal):
            return 0

        
        return self.subarr(nums,goal)-self.subarr(nums,goal-1)

    
    def subarr(self,nums: List[int], goal: int) -> int:

        if goal<0:
            return 0

        left=0
        right=0
        preSum=0
        count=0

        while right<len(nums):

            preSum+=nums[right]

            while preSum>goal:
                preSum-=nums[left]
                left+=1

            count+=right-left+1
            right+=1

        return count

            
        
# "3 POINTER APPRAOCH" ->https://leetcode.com/problems/count-number-of-nice-subarrays/
# COMPLEXITY=O(2n)
 
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d1 = 0
        d2 = 0
        odd_count = 0
        res = 0
        temp_left_choices = 0   
        while d2 < len(nums):
             if nums[d2] % 2 != 0:
                odd_count += 1
                temp_left_choices = 0 
            
            
            while odd_count == k:
                temp_left_choices += 1
                if nums[d1] % 2 != 0:
                    odd_count -= 1
                d1 += 1
            
            res += temp_left_choices
            d2 += 1
            
        return res

# SAME QUESTION BUT APPRAOCH LIKE THE BIARY SUN WALA BHAII jitne bhi odd hai unko 1 maan lo or even ko 0:
 
 class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.subarr(nums,goal)-self.subarr(nums,goal-1)

    
    def subarr(self,nums: List[int], goal: int) -> int:

        if goal<0:
            return 0

        left=0
        right=0
        preSum=0
        count=0

        while right<len(nums):

            preSum+=nums[right]%2

            while preSum>goal:
                preSum-=nums[left]%2
                left+=1

            count+=right-left+1
            right+=1

        return count

# NUMBER OF SUBSTRING CONTAINING ALL THREE CHARACTER->https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# COMPLEXITY=O(2n)


        class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        map={'a':0,'b':0,'c':0}
        left=0
        right=0
        res=0
        count=0

        while right<len(s):
            map[s[right]]+=1

            while map['a']>0 and map['b']>0 and map['c']>0:
                count+=1
                map[s[left]]-=1
                left+=1

            res+=count
            right+=1

        return res


# maximum points u can attain from cards->https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# COMPLEXITY=0(2k)

class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:

        if len(nums)==k:
            return sum(nums)

        
        left=0
        summ=0
        res=0
        right=len(nums)-1

        while left<k:
            summ+=nums[left]
            left+=1
        print(left)
        
        res=summ
        rightval=0
        left -= 1

        while left>=0:
            rightval+=nums[right]
            summ-=nums[left]
 
            res=max(res,rightval+summ)
            right-=1
            left-=1

        return res


#SUM OF GCD OF FORMED PARIES
# COMEPLXITY=O(n)

class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        maxVal=0
        l=[]
     
     #creating the list
        for i in range(len(nums)):
            maxVal=max(maxVal,nums[i])
            l.append(math.gcd(maxVal,nums[i]))

        
        #sorting the list
        l.sort()

        left=0
        right=len(l)-1
        res=0
     
     # find the sum
        while left<len(l)//2:
            res+=math.gcd(l[left],l[right])
            left+=1
            right-=1


        return res


        
          
            
        