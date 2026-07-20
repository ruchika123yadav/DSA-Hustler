# LINKED LIST INSERTION AT BEGINNING->https://www.geeksforgeeks.org/problems/linked-list-insertion-at-beginning/1
# COMPLEXITY=O(n)
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def insertAtFront(self, head, x):
        #code here
        newNode=Node(x)
        newNode.next=head
        head=newNode
        
        return head


# DELETE NODE IN A LINKED LIST->https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# COMPLEXITY=O(1)

 

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val=node.next.val
        node.next=node.next.next


# FIND THE LENGTH OF THE LINKED LIST->https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/1
# COMPLEXITY=O(n)

''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        length=0
        if head.next is None:
            return 1
            
        cur=head
        
        while cur is not None:
            length+=1
            cur=cur.next
            
        return length

# SEARCH IN LINKED LIST->https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1
# COMPLEXITY=O(n)

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        #Code here
        cur=head
        present=False
        
        while cur is not None:
            if cur.data==key:
                present=True
                return present
            cur=cur.next
                
        return present

# MIDDLE OF THE LINKED LIST->https://leetcode.com/problems/middle-of-the-linked-list/description/
# COMPLEXITY=O(n)

 
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow=head
        fast=head

        while fast and fast.next  is not None :
            slow=slow.next
            fast=fast.next.next


        return slow

        
# REVERSE THE LINKED LIST->https://leetcode.com/problems/reverse-linked-list/submissions/2049944611/
# COMPLEXITY=O(n)

 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        prev=None
        curr=head
        Next=head

        while Next is not None:
            Next=curr.next
            curr.next=prev
            prev=curr
            curr=Next


        return prev


# NUMBER OF SUBSTRING CONTAINING ALL TRHEE CHARACTER->https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?envType=daily-question&envId=2026-06-30
# COMPLEXITY=O(2n)

# BRUTE FORCE
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res=0
        n=len(s)
         

        for i in range(n):
            l=['a','b','c']
            for j in range(i,n):
                if s[j] in l:
                    l.remove(s[j])
                    if len(l)==0:
                        res+=n-j
                        break

        return res

        
# OPTIMAL APPRAOCH
# COMPLEXITY=O(n) SPACE COMPLEXITY=O(3)=O(1)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res=0
        n=len(s)

        mapp={}
        j=0

        for i in range(len(s)):
            mapp[s[i]]=mapp.get(s[i],0)+1
            if len(mapp)==3:
                while(len(mapp)>=3):
                    res+=n-i
                    mapp[s[j]]-=1
                    if mapp[s[j]]==0:
                        del mapp[s[j]]
                    j+=1
        
        return res


    #LINKED LIST CYCLE || Floyd's Cycle-Finding Algorithm->https://leetcode.com/problems/linked-list-cycle-ii/description/


    class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list or single node with no cycle
        if not head or not head.next:
            return None

        slow = head
        fast = head
        has_cycle = False

        # Phase 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None

        fast = head # Reset fast to the beginning
        while slow != fast:
            slow = slow.next
            fast = fast.next  

        return slow     

                


# PALINDROME IN LINKED LIST 

# BRUTE FORCE
 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head.next==None:
            return True
        
        curr = head
        l=[]
        length=0
        
        while curr is not None:
            l.append(curr.val)
            curr=curr.next

        res="".join(str(x) for x in l)

        return res==res[::-1]



        
# OPTIMAL APPRAOCH:
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head.next==None:
            return True

               slow=head
        fast=head
        curr=head

        while fast.next and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next

        secondHalf=self.reverse(slow.next)

        while secondHalf is not None:
            if curr.val!=secondHalf.val:
                return False
            curr=curr.next
            secondHalf=secondHalf.next
        
        return True

    def reverse(self,head: Optional[ListNode])-> Optional[ListNode]:

        if head.next is None:
            return head

        prev=None
        curr=head
        Next=head

        while Next is not None:
            Next=curr.next
            curr.next=prev
            prev=curr
            curr=Next        
         
        return prev


# ODD EVEN LINKED LIST->https://leetcode.com/problems/odd-even-linked-list/description/
# COMPLEXITY=O(n) AND SPACE COMPLEXITY=O(n)

# BRUTE FORCE
 
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None or head.next.next is None:
            return head

        odd=[]
        even=[]
        
        oddIndex=head
        evenIndex=head.next

        while oddIndex is not None:
            if oddIndex.next is None:
                odd.append(oddIndex.val)
                break
                    
            odd.append(oddIndex.val)
            oddIndex=oddIndex.next.next


        
        while evenIndex.next:
            if evenIndex.next.next is None:
                even.append(evenIndex.val)
                break

            even.append(evenIndex.val)
            evenIndex=evenIndex.next.next
         
        curr=head

        for i in range(len(odd)):
            curr.val=odd[i]
            curr=curr.next

        for i in range(len(even)):
            curr.val=even[i]
            curr=curr.next

        return head

        
# OPTIMAL SOLUTION: COMPLEXITY=O(n) and SPACE COMPLEXITY=O(1)

 
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None or head.next.next is None:
            return head

        odd=head
        even=head.next
        evenHead=head.next

        while even and even.next is not None:
            odd.next=odd.next.next
            even.next=even.next.next

            odd=odd.next
            even=even.next

        odd.next=evenHead

        return head


# SORT LIST:> https://leetcode.com/problems/sort-list/description/
# BRUTE FORCE lagega ye shurhu me lekin ye hi optimize hai mere bhaii 

 
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l=[]

        curr=head

        while curr is not None:
            l.append(curr.val)
            curr=curr.next

        l.sort()
        curr=head

        for i in range(len(l)):
            curr.val=l[i]
            curr=curr.next

        return head


# OPTIMIZE:wo merge wala bkwss hatao ushe ha lekin sala wo interviwer puch skta to krr le bhai 
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return dummy.next


# REMOVE NTH NODE FORM THE LIST->https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# COMPLEXITY=O(n)

 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            return None

        length=0
        curr=head

        while curr is not None:
            length+=1
            curr=curr.next

        curr=head

        k=length-n-1

        if length-n==0:
            head=head.next
            return head
        

        while k!=0:
            curr=curr.next
            k-=1
        

        curr.next=curr.next.next

        return head
    
        
       
# DELETE THE MIDDLE NODE OF THE LL->https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# COMPLEXITY=O(n)

 
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next is None:
            return None

        curr=head
        fast=head
        slow=head

        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next

        
        while curr.next!=slow:
            curr=curr.next

        curr.next=curr.next.next

        return head
        
        

         

 

# ADD TWO NUMBERS ->https://leetcode.com/problems/add-two-numbers/description/
# COMPLEXITY=O(n)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         firstHead = l1
        secondHead = l2
        
        carry = 0
        newL = ListNode(-1)
        curr = newL

         while firstHead is not None and secondHead is not None:
            v = firstHead.val + secondHead.val + carry
            if v >= 10:
                curr.next = ListNode(v % 10)
                carry = 1
            else:
                curr.next = ListNode(v)
                carry = 0
            curr = curr.next
            firstHead = firstHead.next
            secondHead = secondHead.next

         while firstHead is not None:
            v = carry + firstHead.val
            if v >= 10:
                curr.next = ListNode(0)  
                                  
            else:
                curr.next = ListNode(v)
                carry = 0
            curr = curr.next
            firstHead = firstHead.next

         while secondHead is not None:
            v = carry + secondHead.val
            if v >= 10:
                curr.next = ListNode(0) 
                                   
            else:
                curr.next = ListNode(v)
                carry=0
            curr = curr.next
            secondHead = secondHead.next

         if carry == 1:
            curr.next = ListNode(1)
            curr = curr.next

        curr.next = None
        return newL.next


# ish ticchu question ne jo mere dimmag ka dhi kiya hai faaltu kaa mtlb bss whi meme yaad aa rha hia-> beta tumshe na ho payega
        
# ROTATE LIST:->https://leetcode.com/problems/rotate-list/
# COMPLEXITY=(k)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        length=0
        curr=head

        while curr is not None:
            length+=1
            curr=curr.next

        k=k%length

        if k==0:
            return head

        n=length-k
        prev=head
        mainHead=head

        while n>0:
            prev=mainHead
            mainHead=mainHead.next
            n-=1

        prev.next=None
        curr=mainHead

        while curr.next is not None:
            curr=curr.next

        curr.next=head
        head=mainHead

        return head



# INTERSECTION OF TWO LINKED LIST->https://leetcode.com/submissions/detail/2058963970/
# COMPLEXITY=O(headA+headB)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        a,b=headA,headB

        while a!=b:
            a=a.next if a else headB
            b=b.next if b else headA

        return a

       
        


        

        
    



        
        