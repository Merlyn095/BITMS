'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
a.next=node(2)
a.next.next=node(3)
print(a,a.data,a.next)
print(a.next,a.next.data,a.next.next) 
print(a.next.next,a.next.next.data,a.next.next.next)'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self) -> None:
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(1)
        else:
            new=node(data)
            new.next=self.head
            self.head=new    

=[1,2,3,4,5]
head=None
for i in l:
    insertatbeg(i)
    '''def rev(self):
        curr=self.head
        while curr:
            if curr.next==None:
                self.head=curr
                curr.next,curr.prev=curr.prev,curr.next
                curr=curr.prev'''




          