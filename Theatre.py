m,n,a=map(int, input().split())
i=0
j=0
if m%a==0:
    i=m/a
else:
    i=int(m/a)+1
if n%a==0:
    j=n/a
else:
    j=int(n/a)+1

print(int(i*j))

