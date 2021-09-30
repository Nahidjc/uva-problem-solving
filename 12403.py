n= int(input())
totalAmount=0
i=0;
while i<n:
    x=  input().split(maxsplit=1)
    if(len(x)==1):
        print(totalAmount)
    else:
        val = int(x[1])
        totalAmount = totalAmount + val
    i=i+1