d={0:[1,4],2:[1,3],3:[1,2,4],4:[2,3],5:[0]}
q=[0]
vis={0}
while q:
    a=q.pop()
    for i in d[a]:
        if i not in vis:
            q.append(i)
            vis.add(i)
