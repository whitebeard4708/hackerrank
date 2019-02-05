#Write your code here


class Calculator:
    def __init__(self):
        self.num = 0

    def power(self, n1, p1):
            if (n1 < 0 or p1 < 0):
                raise Exception("n and p should be non-negative")
            else:
                return int(n1**p1)
            
        




