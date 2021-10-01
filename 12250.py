
showValue=[]
i=0
while i<2000:
    m=input()
    if(len(m)>14):
        pass
    else:
        if m=="HELLO":
            showValue.append("ENGLISH")
        elif m=="HOLA":
            showValue.append("SPANISH")
        elif m=="HALLO":
            showValue.append("GERMAN")
        elif m=="BONJOUR":
            showValue.append("FRENCH")
        elif m=="CIAO":
            showValue.append("ITALIAN")
        elif m=="ZDRAVSTVUJTE":
            showValue.append("RUSSIAN")
        elif m=="#":
            break
        else:
            showValue.append("UNKNOWN")

    i+=1


j=0
while j<len(showValue):
    print("Case {0}: {1}".format(j+1,showValue[j]))
    j+=1