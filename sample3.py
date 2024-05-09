class solution:
    def maxDepth(self,s:str) ->int:
        s=[]
        m=0
        for i in s:
            if i=='()':
                st.append(i)
            elif i=='):
                st.pop()
            if len(st)>m:
                m=len(st)
        return m            
        
        
        
            
            '
        
