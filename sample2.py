'''class cse:
    def __init__(self,a):
        self.a=a
    def method(self):
        print("mathod")
o=cse(4)
print(o.a)'''  
class a:
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")
class b(a):
    def __init__(self):
        print("1")
    def __init__(self):
        print("2")
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4") 
class c:
    def fun(self):
        pass        
o=a()
p=b()
q=c()
p.fun1()
o.fun2()               
class ab:
    branch="cse"
    def __init__(self,a):
        ab.x=10
        self.a=a
    def fun(self):
        print("fun1",self.branch,self.x)
        print("fun1",ab.branch,ab.x)
o=ab(3)
o.fun()
#print(o.a,o.p)        