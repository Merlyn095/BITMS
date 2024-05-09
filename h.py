height=float(input())
if(height>6) :
    print("tall")
elif(height>=4 and height<=6) : 
    print("average")
elif(height<4) :
    print("short")


    a=input()
b=input()
for i in range(a):
    for j in range(b):
        if i==j:
        a = a.replace(char, '', 1)
        b = b.replace(char, '', 1)
        break
r = "FLAMES"
count = len(a) + len(b)
while len(r) > 1:
        index = (count % len(r)) - 1
        if index >= 0:
            r = r[:index] + r[index + 1:]
        else:
            r = r[:len(r) - 1]
print(f"The relationship between {a} and {b} is: {result}")  



