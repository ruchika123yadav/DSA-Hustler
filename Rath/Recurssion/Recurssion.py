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


# MINIMUM BIT FLIPS TO CONVERT A NUMBER->https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
# COMPLEXITY=O(1)

 class Solution {
    public int minBitFlips(int start, int goal) {

        int ans=start^goal;
        int count=0;

        for(int i=0;i<31;i++){
            if((ans&(1<<i))!=0){
                count++;
            }
        }

        return count++;
        
    }
}


#    FIND THE KTH CHARACTER IN STRING GAME 1      
# COMLEXITY=O(n)

class Solution:
    def kthCharacter(self, k: int) -> str:

        def append(string):
            array = []
            for val in string:
                array.append( chr( ord(val) + 1)  )
            array = ''.join(array)
            return string + array
            
        inp = "a"
        while len(inp) < k:
            inp = append(inp)
            
        return inp[k-1]


#  Sort a stack->https://takeuforward.org/plus/dsa/problems/sort-a-stack?source=strivers-a2z-dsa-track
# COMPLEXITY=O(n^2)

class Solution:
    def sortStack(self, stack):
        # Your code goes here
        if not stack:
            return

        top_element=stack.pop()

        self.sortStack(stack)
        self.insertedElement(stack,top_element)

        return

    
    def insertedElement(self,stack,top_element):
        if not stack or top_element>=stack[-1]:
            stack.append(top_element)
            return
        
        remove=stack.pop()

        self.insertedElement(stack,top_element)

        stack.append(remove)


# REVERSE THE STACK->https://takeuforward.org/plus/dsa/problems/reverse-a-stack?source=strivers-a2z-dsa-track
# COMPLEXITY=O(n^2)


class Solution:
    def reverseStack(self, stack):
        # Your code goes here

        if not stack:
            return

        top_el=stack.pop()

        self.reverseStack(stack)
        self.reverse(stack,top_el)

        return

    def reverse(self,stack,top_el):
        if not stack:
            stack.append(top_el)
            return

        left=stack.pop()

        self.reverse(stack,top_el)
        stack.append(left)


# GENERATE PARENTHESIS->https://leetcode.com/problems/generate-parentheses/
# COMPLEXITY=hamare bss ki nhi🙂

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<String>();
        recurse(res, 0, 0, "", n);
        return res;
    }
    
    public void recurse(List<String> res, int left, int right, String s, int n) {
        if (s.length() == n * 2) {
            res.add(s);
            return;
        }
        
        if (left < n) {
            recurse(res, left + 1, right, s + "(", n);
        }
        
        if (right < left) {
            recurse(res, left, right + 1, s + ")", n);
        }
    }
}

# ishliye nhi pasand mujhe ye dimaag kharab bkwsss call stackkkkkkkkkkk😑


# CONTRCUT STRING FROM BINARY TREE->https://leetcode.com/problems/construct-string-from-binary-tree/description/
# COMPLEXITY=O(n)


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root==None:
            return ""

        res=str(root.val)

        left=self.tree2str(root.left)
        right=self.tree2str(root.right)

        if root.left==None and root.right==None:
            return res

        if root.right==None:
            return res+"("+left+")"

        return res+"("+left+")"+"("+right+")"
        