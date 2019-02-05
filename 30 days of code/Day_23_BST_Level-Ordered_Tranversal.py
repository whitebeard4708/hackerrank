

def levelOrder(self,root):
    #Write your code here
    queue = [root]
    #print(len(queue))
    for current in queue:
        #print(current)
        if current:
            print(current.data, end = " ")
            queue.append(current.left)
            queue.append(current.right)
    # print(len(queue))

