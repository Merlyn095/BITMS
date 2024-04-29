d={1:23,'a':24,'abc':90}
"""d[1]='abc'
print(d[1])
d['python']=1
print(d,type(d))
print(d[1])"""
'''print(d.get('a'))
print(d.keys())
print(d.values())
print(d.items())'''
for i in d:
    print(i,d[i],end=" ")
print()
for i,j in d.items():
        print(i,j,end=" ")
