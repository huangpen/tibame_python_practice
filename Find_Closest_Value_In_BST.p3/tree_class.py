class treeNode:
    def __init__(self, identity, value):
        self.identity = identity
        self.value = value
        self.left = None
        self.right = None

    def insertLeft(self, identity, value):
        if self.left == None:
            self.left = treeNode(identity, value)
        else:
            self.left.insertLeft(identity, value)

    def insertRight(self, identity, value):
        if self.right == None:
            self.right = treeNode(identity, value)
        else:
            self.right.insertRight(identity. value)


    def build_tree(self, nodes):

        for each in nodes:
            if each['id'] == self.identity:
                 left_ind = self.findID_helper(nodes,each['left'])
                 right_ind = self.findID_helper(nodes,each['right'])
                 if left_ind is not None:
                     self.insertLeft(each['left'], nodes[left_ind]['value'])
                 if right_ind is not None:
                     self.insertRight(each['right'], nodes[right_ind]['value'])

        if self.left is not None:
            self.left.build_tree(nodes)
        if self.right is not None:
            self.right.build_tree(nodes)

        return self

    @staticmethod    
    def findID_helper(nodes, identity):
        if identity == None:
            return None
        for ind in range(len(nodes)):
            if nodes[ind]['id'] == identity:
                return ind
        

