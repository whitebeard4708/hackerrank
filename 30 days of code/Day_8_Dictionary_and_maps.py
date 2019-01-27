# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
dict1 = {}
for i in range(size):
    key, value = input().split()
    dict1[key] = value

query = "a"
while query != None:
    query = input()
    if query in dict1:
        print("{}={}".format(query, dict1[query]))
    else:
        print("Not found")
