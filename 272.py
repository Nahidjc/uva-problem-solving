
count=0
while True:
    try:
        inputString = str(input())
        updateString = []
        for i in inputString:
            if i=='"':
                if count%2==0:
                    updateString.append("``")

                else:
                    updateString.append("''")
                count= count+1
            else:
                updateString.append(i)
        print("".join(updateString))

    except EOFError:
        break





