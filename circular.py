class Node: 
    def __init__(self,data): 
       self.data=data 
       self.next=None 
class CircularLinkedList: 
    def __int__(self): 
        self.head=None 
    def printlist(self): 
        temp=self.head 
        if self.head is not None: 
          while(True): 
              print(temp.data,"-->",end="") 
              temp=temp.next 
              if (temp==self.head): 
                  break 
clist=CircularLinkedList() 
node1=Node('mon') 
node2=Node('tues') 
node3=Node('wed') 
node4=Node('thur') 
clist.head=node1 
clist.head.next=node2 
node2.next=node3 
node3.next=node4 
node4.next=clist.head 
print("the circilar linked list is \n************") 
clist.printlist() 
