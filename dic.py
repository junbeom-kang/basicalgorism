import sys
from collections import deque
input=sys.stdin.readline
Q=[]
ans=[]
while True:
    try:
        Q.append(int(input()))
    except:
        break
def BS(L,R,root):
    if Q[R]>root:
        for i in range(L,R+1):
            if Q[i]>root:
                return i
    else:
        return L


def divide(left,right):
    print(left,right)
    if left==right:
        print(left,right,Q[left])
        ans.append(Q[left])
        return
    root=Q[left]
    print(root)
    ans.append(root)
    temp=BS(left+1,right,root)
    if temp==left+1:
        divide(temp,right)
        return
    else:
        divide(temp, right)
        divide(left+1,temp-1)
divide(0,len(Q)-1)
print(ans)