storeValue=[]
i=0
while i<75:
    n=int(input())
    if n==0:
        break
    numbers = list(map(int,input().split()))
    j=0
    positive =0
    negative=0
    while j<len(numbers):
        if numbers[j]>0:
            positive+=1
        else:
            negative+=1
        j+=1
    storeValue.append(positive - negative)
    numbers=[]
    i+=1

j=0
while j<len(storeValue):
    print('Case {0}: {1}'.format(j+1,storeValue[j]))
    j+=1