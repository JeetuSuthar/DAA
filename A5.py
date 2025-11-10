
def is_safe(queens,row,col):
    for c in range(len(queens)):
        if queens[c] == -1 or c == col:
            continue
        if queens[c]==row or abs(queens[c]-row)==abs(c-col):
            return False
    return True
    
def solve(queens,col,n):
    if col==n:
        return True
    if queens[col] != -1: 
        return solve(queens,col+1,n)
    for row in range(n):
        if is_safe(queens,row,col):
            queens[col]=row
            if solve(queens,col+1,n):
                return True
            queens[col]=-1
    return False
        
def print_sol(queens,n):
    for r in range(n):
        for c in range(n):
            if queens[c]==r:
                print("Q",end=" ")
            else :
                print("*", end=" ")
        print()
    print()
    
n=int(input("enter"))
queens=[-1]*n
fr=int(input("row"))
fc=int(input("col"))
queens[fc]=fr

found=solve(queens,0,n)
if found:
    print_sol(queens,n)
