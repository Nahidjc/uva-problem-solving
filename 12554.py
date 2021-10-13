n= int(input())
inputText=[]
strText=['Happy', 'birthday', 'to', 'you', 'Happy', 'birthday', 'to', 'you', 'Happy', 'birthday', 'to', 'Rujia', 'Happy', 'birthday', 'to', 'you']
i=0
while i<n:
    x=str(input())
    inputText.append(x)
    i+=1

if n<16:
    j = 0
    for name in strText:
        print("{0}: {1}".format(inputText[j], name))
        j += 1
        if j>=n-1:
            j=0
elif n>=16:
    if n%16==0:
        rootLoop = n
    else:
        rootLoop = (int(n/16)+1)*16

    p=0
    m=0
    name=0
    while p<rootLoop:
        print("{0}: {1}".format(inputText[name], strText[m]))

        m+=1
        name+=1
        if name==n:
            name=0
        if m==16:
            m=0
        p+=1





