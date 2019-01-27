class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        l = len(self.__elements)
        arr = self.__elements
        ans = abs(arr[1] - arr[0])
        for i in range(l-1):
            for j in range(i+1, l):
                ans = max(ans, abs(arr[i] - arr[j]))
        self.maximumDifference = ans




# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
