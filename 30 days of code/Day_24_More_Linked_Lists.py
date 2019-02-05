

def removeDuplicates(self,head):
    #Write your code here
    if head:
        data = {"a"}
        node = head
        nextnode = head.next
        while nextnode:
            if node.data not in data:
                data.add(node.data)
            if nextnode.data in data:
                node.next = nextnode.next
                nextnode = nextnode.next
                continue
            node = nextnode
            nextnode = nextnode.next


        return head



