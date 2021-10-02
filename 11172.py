t =int(input())
i=0
oparator=[]
if(t<15):
    while i<t:
        x=  input().split(maxsplit=1)
        if int(x[0])>int(x[1]):
            print(">")
        elif int(x[0])<int(x[1]):
            print("<")
        else:
            print("=")
        i+=1

