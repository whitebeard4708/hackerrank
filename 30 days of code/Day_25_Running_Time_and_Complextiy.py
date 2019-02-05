# Enter your code here. Read input from STDIN. Print output to STDOUT
def isprime(x):
    if x == 1: return False
    elif x == 2: return True
    else:
        if x % 2 == 0:
            return False
        else:
            bound = int(x**0.5)
            for counter in range(3, bound+1, 2):
                if x % counter == 0:
                    return False
            return True



size = int(input())
for _ in range(size):
    num = int(input())
    condition = isprime(num)
    if condition:
        print("Prime")
    else:
        print("Not prime")
