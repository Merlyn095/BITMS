m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
per=(((m1+m2+m3+m4+m5)/500)*100)
print(per)
if per>=75:
    print("grade A")
elif per>=60 and per<75:
    print("grade B")
elif per>=35 and per<60:
    print("Grade C")
else :
    print("fail")    