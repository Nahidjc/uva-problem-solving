n=int(input())
i=0
while i<n:
    m=int(input())
    inputText=[]
    j=0
    while j<m:
        instruct= str(input())
        removeSpace=instruct.lstrip()
        inputText.append(removeSpace)
        j+=1

    p=0
    outputArray=[]
    count=0
    while p<m:
        if inputText[p][0]=="L":
            count-=1
            outputArray.append(0)
        elif inputText[p][0]=="R":
            count+=1
            outputArray.append(1)
        else:
            textLen=len(inputText[p])
            lastValue=int(inputText[p][8:textLen])
            if outputArray[lastValue-1]==0:
                count-=1
                outputArray.append(0)
            elif outputArray[lastValue-1]==1:
                count += 1
                outputArray.append(1)
        p+=1
    print(count)


    i+=1