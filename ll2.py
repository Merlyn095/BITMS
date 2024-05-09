'''class node:
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
    def endinsert(self,data):
        if self.head==None:
            self.head==node(1)
        else:
             new=node(data)
             slow=self.head
             while slow.next==None:
                 slow=slow.next
                 slow.next=new'''
#doublyll
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def delatbeg(self):
        self.head=self.head.next
        self.head.prev=None
    def delatend(self):
        self.tail=self.tail.prev
        self.tail.next=None    
                


o=dll()
for i in range(1,6):
    o.insertatend(i)
o.printing()











            




    


              