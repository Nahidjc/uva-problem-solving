
while (1):
    x,a,b,c=map(int, input().split())
    if x==0 and a==0 and b==0 and c==0:
        break
    startClockDegree = 1080

    first_clock= ((x-a)+40)%40
    second_clock=((b-a)+40)%40

    third_clock = ((b-c)+40)%40
    print(startClockDegree+(+first_clock+second_clock+third_clock)*9)


