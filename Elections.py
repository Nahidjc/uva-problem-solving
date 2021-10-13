n= int(input())
i=0
while i<n:
    inputValue = list(map(int, input().split()))
    max_value = max(inputValue)
    dup_max = inputValue.count(max_value)
    if inputValue[0] == inputValue[1] and inputValue[1] == inputValue[2]:
        j=0
        while j<3:
            inputValue[j]+=1
            j+=1
    elif dup_max>1:
        j = 0
        while j < 3:
            if inputValue[j]== max_value:
                inputValue[j]=1
            else:
                inputValue[j]=max_value-inputValue[j]+1
            j += 1

    else:
        j=0
        while j<3:
            if inputValue[j]== max_value:
                inputValue[j]=0
            else:
                inputValue[j]=max_value-inputValue[j]+1
            j+=1
    i+=1
    print(' '.join(str(x) for x in inputValue))



