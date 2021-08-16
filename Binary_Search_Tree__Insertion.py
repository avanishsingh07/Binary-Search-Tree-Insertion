
def insert(self, val):
        #Enter you code here.
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return
        
        currnode = self.root
        while currnode:
            if val< currnode.info:
                if currnode.left == None:
                    currnode.left = newNode
                    return
                
                currnode = currnode.left
                
            else:
                if currnode.right == None:
                    currnode.right = newNode
                    return
                
                currnode = currnode.right
