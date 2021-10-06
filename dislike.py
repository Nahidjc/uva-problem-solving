numbers=[]
n=int(input())
i=0;
while i<n:
    numbers.append(int(input()))
    i+=1
j=0
x=1
storeValue=[]
while j<1000:
    while True:
        if x%3==0 or x%10==3:
            x+=1
        else:
            storeValue.append(x)
            x+=1
            break
    j+=1

k=0
while k<n:
   print(storeValue[numbers[k]-1])
   k+=1