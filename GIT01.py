# cook your dish here
t = int(input()) 

def pen(c):
    if c == 'R':
        return 5 
    return 3 

for q in range(t):
    n,m = map(int,input().split()) 
    s = [] 
    for i in range(n):
        s.append('') 
        s[i] = input() 
    a,b = [],[] 
    for i in range(n):
        a.append([]) 
        b.append([]) 
        for j in range(m):
            if (i+j)%2 == 0:
                a[i].append('R') 
                b[i].append('G') 
            else:
                a[i].append('G') 
                b[i].append('R') 
    pena,penb=0,0 
    for i in range(n):
        for j in range(m):
            if s[i][j] == a[i][j]:
                penb += pen(s[i][j]) 
            else:
                pena += pen(s[i][j]) 
    print(min(pena,penb))