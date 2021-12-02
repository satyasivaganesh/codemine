n=int(input())
for i in range(n//2,1,-1):
    if n%i==0:
        x=0
        for j in range(2,i//2):
            if i%j==0:
                x=1
        if x==0:
            print(i)
            break
else:
    print(-1)
