n = int(input())
tenList = []
i=1
while i <= n:
    digit = int(input())
    result = ((((digit*567)/9)+7492 )*235)/47 -498
    tensInt = int(result)
    tensStr = str(tensInt)
    tensDigit = str(tensStr[-2])
    tens = int(tensDigit)
    tenList.append(tens)
    i=i+1

for i in range(len(tenList)):
    print (tenList[i])
