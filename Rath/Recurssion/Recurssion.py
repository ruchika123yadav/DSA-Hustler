# RECURSION LEAP OF FAITH (SOME SORT OF EASY QUESTION WHICH BUILD BASIC)

# RECRUSION LEAP OF FATIH
# 1- FACTORIAL

class Solution:

    def fact(n:int)->int:
        if n<=1:
            return 1

        return n*fact(n-1)


    def factorail(self, n: int) -> int:

        self.solve(n)


        
# reverse a string 
class Solution:

    def solve(self,s:str,idx:int)->str:

            if idx>=len(s):
                return ""
            
            res=solve(s,idx+1,res)
            
         
         return res+s[idx]
         


    def stringReverse(self, strr: str) -> str:
        

         i=0
         self.solve(strr,i)

         return s


        



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


# CONSTRUCT STRING FROM BINARY TREE->https://leetcode.com/problems/construct-string-from-binary-tree/description/
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


# JOSEPH PROBLEM OR FIND THE WINNER OF THE CIRCULAR GAME->https://leetcode.com/problems/find-the-winner-of-the-circular-game/

# COMPLEXITY=O(n^2)
# BRUTE FORCE
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

 
        if n==1:
            return 1

        store=list(range(1,n+1))

         
        i=0

        while len(store)>1:
            i=(i+k-1)%len(store)

            store.pop(i)

            # i=idx+1

        return store[0]



        

# JOSEPH PROBLEM OR FIND THE WINNER OF THE CIRCULAR GAME->https://leetcode.com/problems/find-the-winner-of-the-circular-game/

# COMPLEXITY=O(n^2)
# BRUTE FORCE
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

 
        if n==1:
            return 1

        store=list(range(1,n+1))

         
        i=0

        while len(store)>1:
            i=(i+k-1)%len(store)

            store.pop(i)

            # i=idx+1

        return store[0]



        
# BETTER APPRAOCH COMPLEXITY=O(nXk)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        queue=deque()

        for i in range(1,n+1):
            queue.append(i)

        
        while len(queue)>1:

            for i in range(k-1):
                queue.append(queue.popleft())

            queue.popleft()
        
        return queue.popleft()


# OPTIMAL APPRAOCH  jo ki mujhe theek se samj nhi ayii bkwss recursion
# COMPLEXITY=O(n) something uske baad
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        queue=deque()

        for i in range(1,n+1):
            queue.append(i)

        
        while len(queue)>1:

            for i in range(k-1):
                queue.append(queue.popleft())

            queue.popleft()
        
        return queue.popleft()





# INTEGER TO ENGLISH WORDS->https://leetcode.com/problems/integer-to-english-words/description/
# COMPLEXITY=O(log(n))

class Solution:


    def solve(self,num:int)->str:
        belowTen={0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}

        belowTwenty={11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 
        15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

        tens = {
        2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 
        6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}

        if num<=10:
            return belowTen[num]

        if num<20:
            return belowTwenty[num]
        
        if num<100:
            return tens[num//10]+(" "+self.solve(num%10) if num%10!=0 else "")

        if num<1000:
            return self.solve(num//100)+" Hundred"+(" "+self.solve(num%100) if num%100!=0 else "")

        if num<1000000:
            return self.solve(num//1000)+" Thousand"+(" "+self.solve(num%1000) if num%1000!=0 else "")

        if num<1000000000:
            return self.solve(num//1000000)+" Million"+(" "+self.solve(num%1000000) if num%1000000!=0 else "")

        return self.solve(num//1000000000)+" Billion"+(" "+self.solve(num%1000000000) if num%1000000000!=0 else "")




    def numberToWords(self, num: int) -> str:

        if num==0:
            return "Zero"

         
        return self.solve(num)





         

         

        
# DIFFERENT WAYS TO ADD PARENTHESIS->https://leetcode.com/problems/different-ways-to-add-parentheses/
# COMPLEXITY=O(NX2^n)

class Solution:
    def solve(self,s:str)-> List[int]:
        res=[]

        for i in range(len(s)):
            if s[i]=="+" or s[i]=="-" or s[i]=="*":
                left=self.solve(s[0:i])
                right=self.solve(s[i+1:])

                for l in left:
                    for r in right:
                        if s[i]=="+":
                            res.append(l+r)
                        if s[i]=="*":
                            res.append(l*r)
                        if s[i]=="-":
                            res.append(l-r)

        if not res:
            res.append(int(s))
        return res



    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.solve(expression)
        
        # LEXOGRAPHICAL NUMBERS->https://leetcode.com/problems/lexicographical-numbers/description/
        # COMPLEXITY=O(n)  AND SPACE COMPLEXITY=O(Log(n))

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        result=[]

        for currNum in range(1,10):
            self.solve(currNum,n,result)

        return result

    
    def solve(self,currNum:int,n:int,res:List[int]):
        if currNum>n:
            return

        res.append(currNum)
        

        for append in range(10):
            newNum=currNum*10 +append
            if newNum>n: return
            self.solve(newNum,n,res)




# RAT IN A MAZE->https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
# COMPLEXITY=O(3^n) SPACE COMPLEXITY=O(n^2)


class Solution:
    def ratInMaze(self, maze):
        # code here
        
        res=[]
        lis=[]
        
        if maze[0][0] == 0 or maze[len(maze)-1][len(maze)-1] == 0:
            return res
        
        
        self.solve(0,0,maze,res,lis)
        
        return res
        
        
        
    def solve(self,i,j,maze,res,lis):
        n=len(maze)
        if i<0 or i>=n or j<0 or j>=n or maze[i][j]==0:
            return 
        
        if i==n-1 and j==n-1:
            res.append("".join(lis))
            return
            
        maze[i][j]=0
        
        # Bottom
        lis.append('D')
        self.solve(i+1,j,maze,res, lis)
        lis.pop()
        
        # left
        lis.append('L')
        self.solve(i,j-1,maze,res,lis)
        lis.pop()
        
        # Right
        lis.append('R')
        self.solve(i,j+1,maze,res,lis)
        lis.pop()
        
        # Top
        lis.append('U')
        self.solve(i-1,j,maze,res,lis)
        lis.pop()
        
        
        
        maze[i][j]=1
        
        
      

 

