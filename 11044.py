n= int(input())
storeValue=[]
i=0
while i<n:
    x,y= map(int,input().split())
    storeValue.append(int(x/3)*int(y/3))
    i+=1
j=0
while j<len(storeValue):
    print(storeValue[j])
    j+=1