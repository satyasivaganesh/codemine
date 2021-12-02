s=input()
p="a"
for i in range(len(s)):
    for j in range(len(s)-1,i,-1):
        if s[i]==s[j]:
            a=s[i:j+1]
            b=a[::-1]
            if a==b:
                if len(a)>len(p):
                    p=a
print(p)
