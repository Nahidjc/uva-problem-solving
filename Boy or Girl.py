text=str(input())
newText=[]
newText.append(text[0])

i=1
count=1
while i<len(text):
    j=0
    check=0
    while j<len(newText):
        if text[i]==newText[j]:
            check=1
            break
        j+=1
    newText.append(text[i])
    if check==0:
        count+=1
    i+=1
if count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
