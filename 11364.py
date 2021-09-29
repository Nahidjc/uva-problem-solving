n = int(input())
final_dist = []
k=1
while k<=n:
    m = int(input())
    list_of_inputs=list(map(int,input().split()))
    list_of_inputs.sort()
    mn= list_of_inputs[0]
    mx=list_of_inputs[m-1]
    print((mx-mn)*2)
    k=k+1

# m = int(input())
# list_of_inputs=list(map(int,input().split()))
# list_of_inputs.sort()
# mn= list_of_inputs[0]
# mx=list_of_inputs[m-1]