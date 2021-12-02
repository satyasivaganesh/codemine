n=int(input())
r=int(input())
m=int(input())
x=n-r
for i in range(n-1,0,-1):
    n*=i
for j in range(r-1,0,-1):
    r*=j
for k in range(x-1,0,-1):
    x*=k
#print(n,r,x)
print((n//(r*x))%m)
