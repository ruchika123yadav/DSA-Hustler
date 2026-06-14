# LARGEST ODD NUMBER IN STRING->https://leetcode.com/problems/largest-odd-number-in-string/description/
# COMPLEXITY->O(n)

class Solution {
    public String largestOddNumber(String num) {
        for (int i = num.length() - 1; i >= 0; i--) {
            if (Character.getNumericValue(num.charAt(i)) % 2 == 1) {
                return num.substring(0, i + 1);
            }
        }
        return "";        
    }
}


# REMOVE OUTERMOST PARENTHESIS->https://leetcode.com/problems/remove-outermost-parentheses/description/
# TIME COMPLEXITY=O(n) AND SPACE COMPLEXITY=

class Solution {
    public String removeOuterParentheses(String s) {
        
      int n = s.length();
      if(n<=2){
        return "";
      }

      StringBuilder result = new StringBuilder();
      int open = 0;

      for(char c :s.toCharArray()){
         if(c=='('){
            open++;
            if(open>1){
                result.append('(');
            }
         }

         else{
            if(open>1){
                result.append(')');
            }
            open--;
         }
      }

      return result.toString();
    }
}

# REVERSE THE STRING ->https://leetcode.com/problems/reverse-words-in-a-string/

# BETTER APPRAOCH
# COMPEXITY =O(n) , SPACE COMPEXITY=O(n)

class Solution {
    public String reverseWords(String s) {
        
         
        String [] sr = s.trim().split("\\s+");
        int n = sr.length;
        StringBuilder result = new StringBuilder();

        for(int i=n-1;i>=0;i--){
            
           result.append(sr[i]);
           if(i==0){
            continue;
           }
           result.append(" ");
           
        }

        return result.toString();
    }
}

# OPTIMAL APPRAOCH
# COMPEXITY =O(n)

class Solution:
    def reverseWords(self, s: str) -> str:

        sr=s.split()
        n=len(sr)

        result=[]

        for i in range(n-1,-1,-1):
            result.append(sr[i])
            if i==0:
                continue
            result.append(" ")


        return "".join(result)
        

# LONGEST COMMON PREFIX->https://leetcode.com/problems/longest-common-prefix/description/
# COMPLEXITY=O(n^2)


class Solution {
    public String longestCommonPrefix(String[] strs) {
        
     String s=strs[0];
     int n = s.length();

     for(int i=1;i<strs.length;i++){
        String sub=strs[i];

        while(n>0 && !sub.startsWith(s.substring(0,n))){
            n--;
        }

        if(n==0){
            return "";
        }
     }

     return s.substring(0,n);

    }
}


# ROTATE STRING ->https://leetcode.com/problems/rotate-string/description/
# COMPLEXITY=O(n)
class Solution {
    public boolean rotateString(String s, String goal) {
        if(s.length()!=goal.length()){
            return false;
        }

        return (s+s).contains(goal);
    }
}


# ISOMORPHIC STRING->https://leetcode.com/problems/isomorphic-strings/
# COMPEXITY=O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_index_s={}
        char_index_t={}

        for i in range(len(s)):
            if s[i] not in char_index_s:
                char_index_s[s[i]]=i
        
            if t[i] not in char_index_t:
                char_index_t[t[i]]=i

            if char_index_s[s[i]]!=char_index_t[t[i]]:
                return False

        return True
        


# VALID ANAGRAM ->https://leetcode.com/problems/valid-anagram/
# BRUTE FORCE
# COMPLEXITY=O(nlog(n))

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        return sorted(s)==sorted(t)


# OPTIMAL APPRAOCH
# COMPLEXITY=O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True


# SORT CHARACTER BY FREQUENCY->https://leetcode.com/problems/sort-characters-by-frequency/
# COMPLEXITY=
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)


        sorted_chars=sorted(s,key=lambda x:(-count[x],x))


        return "".join(sorted_chars)
        
# Ab Python in saare Tuples ko aapas me compare karke sort karega (Chote se Bada):
# Pehle Tuple ka pehla element dekhega: -2 sabse chota hai, to dono 'e' sabse pehle aa gaye.
# Ab bache (-1, 't') aur (-1, 'r'). Dono ka pehla element -1 hai (Tie!).
# Ab wo doosra element dekhega: 'r' ki ASCII value 't' se choti hoti hai (r pehle aata hai, t baad me). To 'r' pehle aayega aur 't' baad me.


# MAXIMUM NESTING DEPTH OF THE PARENTHESIS->https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
# COMPLEXITY=O(n)

class Solution:
    def maxDepth(self, s: str) -> int:

        count=0
        max_num=0

        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                max_num=max(max_num,count)

            elif s[i]==")":
                count-=1

        return max_num


# SUM OF BEAUTY OF ALL SUBSTRING
# COMPLEXITY=O(n^2) AND SPACE COMPLEXITY=O(n)


class Solution {
    public int beautySum(String s) {
        if(s.length()<=2){
            return 0;
        }
        
        HashMap<Character,Integer> hm = new HashMap<>();
         int sum=0;

       
       for(int i=0;i<s.length();i++){
        for(int j=i;j<s.length();j++){
            char c=s.charAt(j);
              hm.put(c,hm.getOrDefault(c,0)+1);


             int min=Integer.MAX_VALUE;
             int max=0;
             if(hm.size()>1){
            for(char ch:hm.keySet()){
                min=Math.min(min,hm.get(ch));
                max=Math.max(max,hm.get(ch));
            }
            sum+=max-min; 
        }
         
        }
        hm.clear();
         
             
       }

       return sum;

    }
}



# LONGEST PALINDROME SUBSTRING->https://leetcode.com/problems/longest-palindromic-substring/description/

# BRUTE FORCE COMPLEXITY=O(n^3)

class Solution:

    def palindrome(self,s:str)->bool:
         i=0
         j=len(s)-1
         while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
         
         return True


    def longestPalindrome(self, ss: str) -> str:
        # if(len(ss)==1):
        #     return ""


        result=""

        for i in range(len(ss)):
             
            for j in range(i,len(ss)):
                 
                if(self.palindrome(ss[i:j+1])):
                    if(len(result)<len(ss[i:j+1])):
                        result=ss[i:j+1]

        return result



# OPTIMAL APPRAOCH COMPLEXITY=O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(s:str,left:int,right:int):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1


        start=0
        end=0

        for i in range(len(s)):
            odd=expand_around_center(s,i,i)
            even=expand_around_center(s,i,i+1)
            max_len=max(odd,even)

            if max_len>end-start:
                start=i-(max_len-1)//2
                end=i+max_len//2

        return s[start:end+1]


# DETERMINE IF STRING HALVES ARE ALIKE->https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
# COMPLEXITY=O(N) AND SPACE COMPLEXITY=O(10)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        i=0
        j=len(s)//2
        vow_set={'a','e','i','o','u','A','E','I','O','U'}
        leftCount=0
        rightCount=0

        while(i<n//2 and j<n):

            if s[i] in vow_set:
                leftCount+=1
            if s[j] in vow_set:
                rightCount+=1
            
            i+=1
            j+=1

        if leftCount==rightCount:
            return True

        return False


# TWO POINTERS
# REVERSE VOWLES OF STRING->https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# COMPLEXITY=O(n) SPACE COMPLEXITY=O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:

        left=0
        right=len(s)-1
        words=list(s)
        vowels={'a','e','i','o','u','A','E','I','O','U'}

        while left<right:
            if words[left] in vowels and words[right] in vowels:
                words[left], words[right] = words[right],words[left]
                left+=1
                right-=1

            elif words[left] in vowels:
                right-=1

            elif words[right] in vowels:
                left+=1
            
            else:
                left+=1
                right-=1

            
        return "".join(words)




        
        
        

        