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


         