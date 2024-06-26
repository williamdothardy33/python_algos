from linked_list import linked_list
class tree_node(object):
        data = None
        left = None
        right = None
        def __init__(self, data):
            self.data = data

def binary_search_tree(root = None):
    class tree(object):
        root = None
        def __init__(self, root):
            self.root = root
        def make(self, *args):
            for arg in args:
                self.insert(arg)

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
        # this creates a level at each insert so not correct
        def insert_incorrect(self, data):
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

        def insert(self, data):
            def insert_recur(node, data):
                if node.data > data:
                    if node.left is None:
                        node.left = tree_node(data)
                    else:
                        insert_recur(node.left, data)
                else:
                    if node.right is None:
                        node.right = tree_node(data)
                    else:
                        insert_recur(node.right, data)

            if self.root is None:
                self.root = tree_node(data)
            else:
                insert_recur(self.root, data)
        
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

        def in_order_show(self, node = None):
            return self.to_list().show()
        
        def pre_order_to_list(self):
            def pre_order_to_list_recur(node, list):
                if node is not None:
                    data = node.data
                    list.insert_last(data)
                    pre_order_to_list_recur(node.left, list)
                    pre_order_to_list_recur(node.right, list)
            result_list = linked_list()
            pre_order_to_list_recur(self.root, result_list)
            return result_list
        
        def pre_order_show(self):
            return self.pre_order_to_list().show()
        
        def is_equal(self, bst_root):
            def is_equal_recur(node0, node1):
                return (node0 == node1) or ((node0 is not None) and (node1 is not None)) and (node0.data == node1.data) and is_equal_recur(node0.left, node1.left) and is_equal_recur(node0.right, node1.right)
            return is_equal_recur(self.root, bst_root)


    result = tree(root)
    return result

def bst_max(node):
    if node is not None:
        if node.right is None:
            return node.data
        else:
            return bst_max(node.right)

def test_binary_search_tree():
    root = tree_node(30)
    left1 = tree_node(15)
    leftl1 = tree_node(7)
    leftr1 = tree_node(23)
    right1 = tree_node(45)
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
    # print(f'show before delete: {bst.in_order_show()}')
    #bst.delete(15)
    #print(f'show after delete 15: {bst.to_list().in_order_show()}')
    #print(f'right of the root 15: {bst.root.right}')
    # bst.delete(7)
    # print(f'show after delete 7: {bst.in_order_show()}')
    # bst.delete(15)
    # print(f'show after delete 15: {bst.in_order_show()}')
    # bst.delete(23)
    # print(f'show after delete 23: {bst.in_order_show()}')
    # bst.delete(50)
    # print(f'show after delete 50: {bst.in_order_show()}')
    # bst.delete(45)
    # print(f'show after delete 45: {bst.in_order_show()}')
    # bst.delete(30)
    # print(f'show after delete 30: {bst.in_order_show()}')
    # bst.delete(40)
    # print(f'show after delete 40: {bst.in_order_show()}')
    # bst.delete(47)
    # print(f'show after delete 47: {bst.in_order_show()}')
    bst1 = binary_search_tree()
    bst1.make(1,5,9,2,4,10,6,3,8)
    print(f'show after insert bst1: {bst1.in_order_show()}')

    is_equal_bst1 = tree_node(1)
    is_equal_bst1.right = tree_node(5)
    is_equal_bst1.right.right = tree_node(9)
    is_equal_bst1.right.right.left = tree_node(6)
    is_equal_bst1.right.right.left.right = tree_node(8)
    is_equal_bst1.right.right.right = tree_node(10)
    is_equal_bst1.right.left = tree_node(2)
    is_equal_bst1.right.left.right = tree_node(4)
    is_equal_bst1.right.left.right.left = tree_node(3)

    #print(bst1.is_equal(is_equal_bst1))
    #print(f'show after insert is_equalbst1: {binary_search_tree(is_equal_bst1).in_order_show()}')
    #print(f'max of bst1 is: {bst_max(bst1.root)}')
    print(f'pre order bst: {bst.pre_order_show()}')





    





test_binary_search_tree()




        
            