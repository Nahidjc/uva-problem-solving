dataList=[]
i = 0
while True:
    n=input()
    if n=="*":
        break
    else:
        dataList.append(n)

    i = i + 1
j=0
while j<len(dataList):
    if dataList[j]=="Hajj":
        print("Case {0}: Hajj-e-Akbar".format(j+1))
    elif dataList[j]=="Umrah":
        print("Case {0}: Hajj-e-Asghar".format(j+1))
    j=j+1


