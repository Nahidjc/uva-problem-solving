n=int(input())
i=0

storeValue=[]
while i<n:
    inputValue = list(map(int, input().split()))
    inputValue.sort()
    storeValue.append(inputValue[1])
    i+=1


z=0
while z<len(storeValue):
    print("Case {0}: {1}".format(z+1,storeValue[z]))
    z+=1
