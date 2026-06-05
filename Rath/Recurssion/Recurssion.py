# //POWER X(N)->https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn=n

        ans=1.0

        if nn<0: nn=-1*nn

        while nn>0:
            if nn%2==1:
                ans=ans*x
                nn-=1

            else:
                x=x*x
                nn=nn//2

        if n<0:
            ans=1/ans

        return ans



# FINDING PRIME NUMBER

if n <= 1:
        return False

for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
        

# STRING TO INTEGER(ATOI)->https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution:
    def myAtoi(self, s: str) -> int:

        s=s.strip()

        if not s:
            return 0
        sign,i=1,0
        res=0

        if s[0]=='-':
            sign=-1
            i+=1
        elif s[0]=='+':
            sign=1
            i+=1

        
        while i<len(s) and s[i].isdigit():
            res=res*10 + int(s[i])

            if res*sign>2**31-1: return 2**31-1
            if res*sign<-2**31: return -2**31

            i+=1

        return sign*res

#    COUNT GOOD NUMBER->https://leetcode.com/problems/count-good-numbers/description/ 
# BRUTE FORCE COMPLEXITY= O(\log n)
        
class Solution:
    def power(self, x: int, k: int) -> int:
        res = 1
        n = k

        while n > 0:
            if n % 2 == 1:
                res = res * x
                n -= 1
            else:
                x = x * x
                n = n // 2

        return res

    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        if n == 1:
            return 5

        five = 0
        four = 0
        k = n // 2
        res = 0

        if n % 2 == 0:
            five = self.power(5, k)
            four = self.power(4, k)
            res = (five * four) % mod

        else:
            five = self.power(5, k + 1)
            four = self.power(4, k)
            res = (five * four) % mod

        return res

# OPTIMAL APPRAOCH COMPLEXITY SAME AS BRUTE O(log(n))
class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod =10**9+7

        even_position=(n+1)//2
        odd_position=n//2

        five=pow(5,even_position,mod)
        four=pow(4,odd_position,mod)

        return (five*four)%mod


        