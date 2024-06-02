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

    result = tree(root)
    return result

def test_binary_search_tree():
    root = tree_node(30)
    left1 = tree_node(15)
    right1 = tree_node(45)
    rightl1 = tree_node(40)
    rightr1 = tree_node(50)
    root.left = left1
    root.right = right1
    right1.left = rightl1
    right1.right = rightr1
    bst = binary_search_tree(root)
    bst_list = bst.to_list()
    print(f'bst list: {bst_list.show()}')
    bst.insert(15)
    bst_list1 = bst.to_list()
    print(f'bst list1: {bst_list1.show()}')



test_binary_search_tree()




        
            