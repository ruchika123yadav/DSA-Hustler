# PROCESS STRING WITH SPECIAL OPERATIONS->https://leetcode.com/problems/process-string-with-special-operations-i/description/?envType=daily-question&envId=2026-06-16

# COMPLEXITY=O(n)  FOR WORST CASE=O(n^2)
# DATE-16/6
class Solution:
    def processStr(self, s: str) -> str:
        

        container=list(s)
        res=""
        

        for i in range(len(container)):
            n=len(res)
            if container[i]=='#':
                res+=res

            elif container[i]=='%':
                res=res[::-1]

            elif container[i]=='*':
                if(len(res)!=0):
                    res = res[:n-1]
                 
            else:
                res+=container[i]

        return res


# HARD PROCESS STRING WITH SPECIAL OPERATIONS || ->https://leetcode.com/problems/process-string-with-special-operations-ii/description/?envType=daily-question&envId=2026-06-17
# COMPLEXITY=O(2n) AND SPACE COMPLEXITY=O(1)
# tagda question hai bhaiiii

# DATE-17/6
class Solution:
    def processStr(self, s: str, k: int) -> str:

        length=0

# finding only length
        for i in range(len(s)):
            c=s[i]

            if c=='*':
                if length>0:
                    length-=1

            elif c=='#':
                length*=2
                 
            elif c=='%':
                continue
                 

            else:
                length+=1

        
        if k>=length:
            return "."

        # REVERSE SIMULATION
        for c in s[::-1]:            
            if c=='*':
                length+=1 #Yha reverse move krenge to ek character badha hua hoga na kyuki phele remove krr chuke the ush character ko
            elif c=='#':
                length=length//2
                if k>=length:
                    k=k-length

            elif c=='%':
                k=length-k-1 #length same but k ki value reverse ke acc change

            else:
                length-=1
            
            if k==length:
                return c


        return "."


# ANGLE BETWEEN HANDS OF A CLOCK->https://leetcode.com/problems/angle-between-hands-of-a-clock/?envType=daily-question&envId=2026-06-18
# COMPLEXITY=O(1)

# DATE-18/6
# bhai logical question tha pura mathematical
class Solution:
    def angleClock(self, h: int, m: int) -> float:

        minute=m*6
        hour=30*(h%12) +0.5*m

        diff=abs(minute-hour)

        return min(360-diff,diff)


# FIND THE HIGHEST ALTITUDE->https://leetcode.com/problems/find-the-highest-altitude/description/?envType=daily-question&envId=2026-06-19
# COMPLEXITY=O(n) and space COMPLEXITY=O(1)
# DAY-19/6

# shi tha question simple
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        if len(gain)==1:
            return max(gain[0],0)

        maxGain=max(gain[0],0)
        summ=gain[0]

        for i in range(1,len(gain)):
            summ+=gain[i]
            maxGain=max(maxGain,summ)


        return maxGain


# MAXIMUM BIULDING HEIGHT->https://leetcode.com/problems/maximum-building-height/description/?envType=daily-question&envId=2026-06-20
# COMPLEXITY=O(n)   

class Solution:
    def maxBuilding(self, n: int, res: List[List[int]]) -> int:
        res.append([1,0])
        res.append([n,n-1])
        res.sort()
        ans=0

        # LEFT TO RIGHT PASS
        for i in range(1,len(res)):
            res[i][1]=min(res[i][1],res[i-1][1]+res[i][0] - res[i-1][0])

#        RIGHT TO LEFT PASS
        for i in range(len(res)-2,-1,-1):
            res[i][1]=min(res[i][1],res[i+1][1]+res[i+1][0] - res[i][0])

#       THE PEAK BETWEEN 2 RESTRCITED BUILDING
        for i in range(1,len(res)):
            idx1=res[i-1][0]
            h1=res[i-1][1]

            idx2=res[i][0]
            h2=res[i][1]

            gap=idx2-idx1

            ans=max(ans,(gap+h2+h1)//2)


        return ans



# MAXIMUM ICE CREAM BARS->https://leetcode.com/problems/maximum-ice-cream-bars/?envType=daily-question&envId=2026-06-21
# COMPLEXITY=O(n+K) whre k is the maximum number


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        if len(costs)==1 and costs[0]>coins:
            return 0
        elif len(costs)==1 and costs[0]<=coins:
            return 1

        
        max_value=max(costs)
        count=[0]*(max_value+1)
        val=0

        for i in range(len(costs)):
            count[costs[i]]+=1

        for i in range(len(count)):
            if count[i]>0:
                if i>coins:
                    return val
                else:
                    while(count[i]>0):
                        if coins>=i:
                            val+=1
                            coins-=i
                            count[i]-=1
                        else:
                            break                
        return val



# MAXIMUM NUMBER OF BALLOONS->https://leetcode.com/problems/maximum-number-of-balloons/description/?envType=daily-question&envId=2026-06-22
# COMPLEXITY=O(n) AND SPACE COMPLEXITY=O(1)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if text=="balloon":
            return 1
        if len(text)<7:
            return 0

        count={'b':0,'a':0,'l':0,'o':0,'n':0}

        for i in range(len(text)):
            if text[i]=='b':
                count['b']+=1
            elif text[i]=='a':
                count['a']+=1
            elif text[i]=='l':
                count['l']+=1
            elif text[i]=='o':
                count['o']+=1
            elif text[i]=='n':
                count['n']+=1

        count['l']=count['l']//2
        count['o']=count['o']//2
        # minn=float('inf')
        # for value in count.values():
        #     if value==0:
        #         return 0

        #     minn=min(minn,value)

        return min(count.values())


# 
# BRUTE FORCE
from functools import cache

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        res = 0
        
        @cache
        def zigzag(i: int, prev: int, went_up: bool):
            if i == n:
                return 1

            total = 0

            if went_up:
                # GO DOWN
                for val in range(l, prev):
                    total = (total + zigzag(i + 1, val, False)) % mod
            else:
                # GO UP
                for val in range(prev + 1, r + 1):
                    total = (total + zigzag(i + 1, val, True)) % mod

            return total%mod

        # Main logic loop for first two numbers
        for first in range(l, r + 1):
            for second in range(l, r + 1):
                if second > first:
                    res = (res + zigzag(2, second, True)) % mod
                elif first > second:
                    res = (res + zigzag(2, second, False)) % mod

        return res % mod
        

        

        


        