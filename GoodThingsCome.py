n=int(input())
i=0

storeValue=[]
while i<n:
    k=int(input())
    inputValue = []
    inputValue = list(map(int, input().split()))
    mx=max(inputValue)
    mn=min(inputValue)
    storeValue.append(mx*mn)
    i+=1

z=0
while z<len(storeValue):
    print("Case {0}: {1}".format(z+1,storeValue[z]))
    z+=1
# print(storeValue)

# s=[4]
# mn=min(s)
# mx=max(s)
# print(mn,mx)