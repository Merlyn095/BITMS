'''d={0:[1,4],2:[1,3],3:[1,2,4],4:[0,3],5:[0]}
def dfs(start,vis):
    vis.add(start)
    for i in d[start]:
        if i not in vis:
           dfs(i,vis)
dfs(0,set()) '''


