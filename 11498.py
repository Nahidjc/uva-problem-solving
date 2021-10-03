valueStore=[]
while (1):
    k=int(input())
    if k==0:
        break
    m,n=map(int, input().split())

    i=0
    while i<k:
        a,b= map(int, input().split())
        if a==m or b==n:
            valueStore.append('divisa')
        elif m<a:
            if n<b:
                valueStore.append('NE')
            else:
                valueStore.append('SE')
        elif m>a:
            if n<b:
                valueStore.append('NO')
            else:
                valueStore.append('SO')

        i+=1
j=0
while j<len(valueStore):
    print(valueStore[j])
    j+=1