year=int(input())
"""if year%4==0 :
    if year%100==0:
        if year%400==0:
            print("it is a leap year")
       else :
           # print("it is not a leap year") 
    else :
        print("leap year")           

else:
   print("not a leap year")"""

"""if (year%100==0 and year%400==0):
    print("leap year")
elif (year%100!=0 and year%4==0):
      print("leap yaer")
else :
     print("not a leap year")  """  
if year%400==0 or year%100!=0 and year%4==0:
    print("leap year")
else:
    print("not leap year")
