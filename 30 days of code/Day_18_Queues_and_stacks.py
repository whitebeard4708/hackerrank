

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = ""
        self.stack_ele = ""
        self.queue = ""
        self.queue_ele = ""
    
    def pushCharacter(self,s):
        self.stack += s

    def popCharacter(self):
        self.stack_ele = self.stack[-1]
        self.stack = self.stack[:-1]
        return self.stack_ele

    def enqueueCharacter(self, s):
        self.queue += s

    def dequeueCharacter(self):
        self.queue_ele = self.queue[0]
        self.queue = self.queue[1:]
        return self.queue_ele

