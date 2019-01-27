# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_even_odd(string):
    even = []
    odd = []
    for i in range(len(string)):
        if i % 2 == 0:
            even.append(string[i])
        else:
            odd.append(string[i])

    print("".join(even) + " " + "".join(odd))

size = int(input())
for i in range(size):
    string = input()
    print_even_odd(string)
