n= int(input())

i=0
dataStore = []
while i<n:
    x=  input().split(maxsplit=2)
    length = int(x[0])
    width = int(x[1])
    height = int(x[2])
    if(length>20 or width>20 or height>20) :
        dataStore.append('bad')
    else:
        dataStore.append('good')
    i=i+1
j=0
while j<len(dataStore):
    print("Case {0}: {1}".format(j+1,dataStore[j]))
    j=j+1