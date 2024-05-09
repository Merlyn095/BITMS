''''operations=["--X","X++","X++"]
x=0
for i in operations:
    if i=='++X' or i=='X++':
        x+=1
    else:
        x-=1
return x ''''
nums=[1,2,3,4]
for i in range(1,len(nums)):
    nums[i]=nums[i]+nums[i-1]
