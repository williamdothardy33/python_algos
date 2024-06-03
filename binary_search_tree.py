from linked_list import linked_list
class tree_node(object):
        data = None
        left = None
        right = None
        def __init__(self, data):
            self.data = data

def binary_search_tree(root):
    class tree(object):
        root = None
        def __init__(self, root):
            self.root = root

        def search(self, data):
            def search_recur(node, data):
                if node.data == data:
                    return node
                elif node.data > data:
                    return search_recur(node.left, data)
                else:
                    return search_recur(node.right, data)
            if self.root is not None:
                return search_recur(self.root, data)
            
        def insert(self, data):
            def insert_recur(parent_node, node, data):
                if node is None:
                    if parent_node.data > data:
                        parent_node.left = tree_node(data)
                    else:
                        parent_node.right = tree_node(data)
                else:
                    if node.data > data:
                        insert_recur(node, node.left, data)
                    else:
                        insert_recur(node, node.right, data)
            if self.root is None:
                self.root = tree_node(data)
            else:
                if self.root.data > data:
                    insert_recur(self.root, self.root.left, data)
                else:
                    insert_recur(self.root, self.root.right, data)

        
        def to_list(self):
            def to_list_recur(node, list):
                if node is not None:
                    to_list_recur(node.left, list)
                    data = node.data
                    list.insert_last(data)
                    to_list_recur(node.right, list)
            result_list = linked_list()
            to_list_recur(self.root, result_list)
            return result_list
        
#this algo says traverse the tree until you find the node of data you want to delete, then find successor(s) for the 'holes'
#you will be creating by deleting and moving data. if you cannot find successors then find predecessors to fill the 'holes'
        
        def delete(self, data):
            def delete_recur(node, data):
                if node is None:
                    return node
                elif node.data == data:
                    if node.right is not None:
                        if node.right.left is not None:
                            successor(node.right, node)
                            return node
                        else:
                            left = node.left
                            node.right.left = left
                            return node.right
                    else:
                        return node.left
                else:
                    if node.data > data:
                        node.left = delete_recur(node.left, data)
                        return node
                    else:
                        node.right = delete_recur(node.right, data)
                        return node
        
            def successor(node, node_to_delete):
                if node.left is not None:
                    node.left = successor(node.left, node_to_delete)
                    return node
                else:
                    node_to_delete.data = node.data
                    return node.right
                
            self.root = delete_recur(self.root, data)

    result = tree(root)
    return result

def test_binary_search_tree():
    root = tree_node(30)
    left1 = tree_node(15)
    right1 = tree_node(45)
    leftl1 = tree_node(7)
    leftr1 = tree_node(23)
    rightl1 = tree_node(40)
    rightr1 = tree_node(50)
    rightr1l2 = tree_node(47)
    rightr1r2 = tree_node(53)
    rightr1r2r1 = tree_node(55)
    root.left = left1
    root.right = right1
    right1.left = rightl1
    right1.right = rightr1
    left1.left = leftl1
    left1.right = leftr1
    right1.right.left = rightr1l2
    right1.right.right = rightr1r2
    right1.right.right.right = rightr1r2r1
    bst = binary_search_tree(root)
    print(f'show before delete: {bst.to_list().show()}')
    #bst.delete(15)
    #print(f'show after delete 15: {bst.to_list().show()}')
    #print(f'right of the root 15: {bst.root.right}')
    bst.delete(7)
    print(f'show after delete 7: {bst.to_list().show()}')
    bst.delete(15)
    print(f'show after delete 15: {bst.to_list().show()}')
    bst.delete(23)
    print(f'show after delete 23: {bst.to_list().show()}')
    bst.delete(50)
    print(f'show after delete 50: {bst.to_list().show()}')
    bst.delete(45)
    print(f'show after delete 45: {bst.to_list().show()}')
    bst.delete(30)
    print(f'show after delete 30: {bst.to_list().show()}')
    bst.delete(40)
    print(f'show after delete 40: {bst.to_list().show()}')
    bst.delete(47)
    print(f'show after delete 47: {bst.to_list().show()}')



    





test_binary_search_tree()




        
            