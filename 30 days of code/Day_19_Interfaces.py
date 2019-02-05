

import math

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        if n == 1:
            return 1
        else:
            ans = 1 + n
            for i in range(2, int(math.sqrt(n))+1):
                if n%i == 0:
                    if i != n/i:
                        ans += (i + n/i)
                    else:
                        ans += i
            return int(ans)
        

