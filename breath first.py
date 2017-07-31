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

##s=[[1,0,1,0,1],
##   [0,0,1,1,0],
##   [0,1,1,1,0],
##   [1,0,0,1,0],
##   [1,0,1,0,1]]

start=input('enter starting point').split(',')
start=tuple((int(start[0]),int(start[1])))
if s[start[0]][start[1]]==0:
    print('start must be 1')
end=input('enter ending point').split(',')
end=tuple((int(end[0]),int(end[1])))
if s[end[0]][end[1]]==0:
    print('end must be 1')
result=[start]
d={}
q=[]


q=[(i,j) for i in range(start[0]-1,start[0]+2) for j in range(start[1]-1,start[1]+2) if (not (i==start[0] and j==start[1])) and (i>=0 and j>=0) and (i<len(s[0]) and j<len(s[0])) if s[i][j]==1]
if len(q)==0:print('no path')
result+=q

while len(q)>0:
    current=q.pop(0)
    if current==end:
        print('this is it')
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
        print('nopath')
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
    print([end]+arr+[start][::-1])
    print(len(arr)+2)
