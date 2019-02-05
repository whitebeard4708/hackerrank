# Enter your code here. Read input from STDIN. Print output to STDOUT

d1, m1, y1 = list(map(int, input().split()))
d2, m2, y2 = list(map(int, input().split()))

if y1 > y2:
    print("10000")
elif y1 == y2:
    if m1 > m2:
        print("{}".format((m1-m2)*500))
    elif m1 == m2:
        if d1 > d2:
            print("{}".format((d1-d2)*15))
        else:
            print("0")
    else:
        print("0")
else:
    print("0")      
