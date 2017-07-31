s= [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0 ],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]



def func(start,end):
    result=[start]
    d={}
    q=[]

    q=[(i,j) for i in range(start[0]-1,start[0]+2) for j in range(start[1]-1,start[1]+2) if (not (i==start[0] and j==start[1])) and (i>=0 and j>=0) and (i<len(s[0]) and j<len(s[0])) if s[i][j]==1]
    if len(q)==0:print('no path')
    result+=q

    while len(q)>0:
        current=q.pop(0)
        if current==end:
            break

        lst=[(i,j) for i in range(current[0]-1,current[0]+2) for j in range(current[1]-1,current[1]+2) if (not (i==current[0] and j==current[1])) and (i>=0 and j>=0) and (i<len(s[0]) and j<len(s[0])) if s[i][j]==1]
        n_lst=[]
        
        for a in lst:
            if a not in result:
                result.append(a)
                q.append(a)
                n_lst.append(a)

        d[(current[0],current[1])]=n_lst
        if len(q)==0:
            d={} 

    arr=[]
    while len(d):
        f_len=len(arr)
        for key,val in d.items():
            if current in val:
                arr.append(key)
                current=key

        l_len=len(arr)
        if f_len-l_len==0:
            break
    if len(d)>0:
        return [[end]+arr+[start] ,len(arr)+2]



check=[[(0,i),(9,j),func((0,i),(9,j))] for i in range(len(s)) for j in range(len(s)) if i!=0 and j!=0]
check=[i for i in check if i[2]!=None]
mini=min([i[2][1] for i in check])
print([i[2][1] for i in check])
path=[]
vertex=[]
for i,j in enumerate(check):
    if j[2][1]==mini:
        path.append(j[2][0])
        vertex.append(tuple((j[0],j[1])))
print('min distance',mini)
for i in vertex:
    print(i)    
