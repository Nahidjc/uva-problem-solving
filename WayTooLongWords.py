n= int(input())
i=0
while i<n:

    x=str(input())
    x_len=len(x)
    if x_len<=10:
        print(x)
    # elif x_len==10:
    #     print("{0}{1}{2}".format(x[0], x_len - 2, x[x_len - 1]))
    elif x_len>10:
        print("{0}{1}{2}".format(x[0],x_len-2,x[x_len-1]))
    i+=1
