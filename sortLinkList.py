'''
First line take the sorted array of absolute value
Sample 1) Input:-
-1 4 7 -8 9

Output:-
-8 -1 4 7 9

Sample 2) Input:-
-1 -2 -3 -4 -5

Output:-
-5 -4 -3 -2 -1
'''
class linkedlist:
    def __init__(self):
        self.head=None
    
    class Node(object): 
        def __init__(self, d): 
            self.data = d 
            self.next = None
            
    def insert(self, new_data):
        new_node = self.Node(new_data) 

        if self.head is None: 
            self.head = new_node 
            return
    
        last = self.head 
        while (last.next): 
            last = last.next
    
        last.next =  new_node 
    
    def sort(self):
        prev=self.head
        curr=prev.next
        while curr != None:
            if curr.data < prev.data:
                prev.next=curr.next
                curr.next=self.head
                self.head=curr
                curr=prev
            else:
                prev=curr
            curr=curr.next 
        
    def printList(self): 
        temp = self.head 
        while temp != None: 
            print (temp.data, end=" ")
            temp = temp.next
        
llist = linkedlist() 
l=[]
l=list(map(int,input().split(" ")))
for i in l:
    llist.insert(i)
llist.sort()
llist.printList()