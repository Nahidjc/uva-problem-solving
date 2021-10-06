numbers=[]
n=int(input())
i=0;
while i<n:
    numbers.append(int(input()))
    i+=1
j=0
storeValue=[]
a=1
while j<max(numbers):
    if a%3!=0 and a%10!=3:
        storeValue.append(a)
        a+=1
    else:
        a+=1
        if a%3!=0 and  a%10!=3:
          storeValue.append(a)
          a+=1
        else:
            a+=1
            storeValue.append(a)
            a+=1
    j+=1
k=0

while k<n:
   print(storeValue[numbers[k]-1])
   k+=1