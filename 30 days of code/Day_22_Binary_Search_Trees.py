

    def getHeight(self,root):
        #Write your code here
        left, right = 0, 0
        if root.left != None:
            left = self.getHeight(root.left) + 1
        if root.right != None:
            right = self.getHeight(root.right) + 1
        return max(left, right)

