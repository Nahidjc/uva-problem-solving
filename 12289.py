words=['one','two','three']
n= int(input())
i=0
if n<=10:
    while i<n:
        m=input()
        j=0
        while j<3:
             if len(words[j])==len(m):
                 counter = 0
                 k = 0
                 while k < len(m):
                     if m[k] != words[j][k]:
                         counter += 1
                     k = k + 1
                 if counter < 2:
                    print(j+1)
                    break

             j=j+1
        i=i+1

