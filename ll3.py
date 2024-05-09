class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self) -> None:
        self.head=None
      
        
    def frontinsert(self,data):
        if self.head==None:
            self.head=node(1)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def rev(self):
        prev=None
        curr=self.head
        nxt=self.head.next
        while curr:
            
            curr.next=prev
            prev=curr
            if nxt:
                nxt=nxt.next
        self.head=prev        
    def printing(self):
         i=self.head
        while i:
            print(i.data)
            i=i.next
    def delatbeg(self):
        self.head=self.head.next
        self.head.prev=None
    def delatendsll(self):
       i=self.head
       while i.next.next:
       i=i.next
       i.next=None
o=sll()
for i in range(1,6):
    o.frontinsert()
    
o.printing() 




