'''
First line take the size of matrix that is n
Second it take matrix of size n*n
Sample 1) Input:-
3
2 7 4
9 6 5
1 3 8

Output:-
Continous longest chain
4, 5, 6, 7

Sample 2) Input:-
4
1 5 7 15
8 9 10 16
3 14 11 4
6 13 12 2

Output:-
Continous longest chain
8, 9, 10, 11, 12, 13, 14
'''
n=int(input("Enter the matrix size "))

mat=[]

for i in range(0,n):
    mat.append(list(map(int,input().split(" "))))

#list of list
lol = [] 
def check(i, j, l):
    up, down, left, right = 0, 0, 0, 0
    if i == 0:
        up = -1
    if j == 0:
        left = -1
    if i == n-1:
        down = -1
    if j == n-1:
        right = -1
    if up != -1:
        up = mat[i-1][j]
        if up == mat[i][j]+1:
            l.append(up)
            check(i-1, j, l)
            return 0
    if left != -1:
        left = mat[i][j-1]
        if left == mat[i][j]+1:
            l.append(left)
            check(i, j-1, l)
            return 0
    if down != -1:
        down = mat[i+1][j]
        if down == mat[i][j]+1:
            l.append(down)
            check(i+1, j, l)
            return 0
    if right != -1:
        right = mat[i][j+1]
        if right == mat[i][j]+1:
            l.append(right)
            check(i, j+1, l)
            return 0

for i in range(n):
    for j in range(n):
        if(any(mat[i][j] in l for l in lol)):
            continue
        else:
            l = []
            l.append(mat[i][j])
            check(i, j, l)
            lol.append(l)
result=1
result=len(max(lol,key=len))
for l in lol:
    if result==len(l):
        print( ", ".join( repr(e) for e in l ) )