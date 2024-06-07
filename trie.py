def trie(data):
    class trie_node():
        children = None
        def __init__(self):
            self.children = {}

    class trie():
        root = None
        def __init__(self):
            self.root = trie_node()

        def search(self, search_term):
            def search_recur(search_term, search_length, current_node, search_pointer):
                if search_pointer >= search_length:
                    return current_node
                else:
                    next_node = current_node.children.get(search_term[search_pointer])
                    if next_node is not None:
                        return search_recur(search_term, search_length, next_node, search_pointer + 1)
                    
            def search_iter(search_term, node):
                search_pointer = 0
                current_node = node
                length = len(search_term)

                while search_pointer < length:
                    next_node = current_node.children.get(search_term[search_pointer])
                    if next_node is None:
                        current_node = None
                        break
                    else:
                        current_node = next_node
                        search_pointer += 1

                return current_node
            search_length = len(search_term)
            
            #return search_recur(search_term, search_length, self.root, 0)
            return search_iter(search_term, self.root)

        def insert(self, data):
            def insert_recur(data, data_length, data_pointer, current_node):
                if data_pointer == data_length:
                    current_node.children['*'] = None
                else:
                    data_part = data[data_pointer]
                    next = current_node.children.get(data_part)
                    if next is None:
                        child_node = trie_node()
                        current_node.children[data_part] = child_node
                        next = child_node
                    insert_recur(data, data_length, data_pointer + 1, next)

            def insert_iter(data, node):
                data_pointer = 0
                current_node = node
                data_length = len(data)
                
                while data_pointer <= data_length:
                    if data_pointer == data_length:
                        current_node.children['*'] = None
                        break
                    else:
                        data_part = data[data_pointer]
                        next = current_node.children.get(data_part)
                        if next is None:
                            child_node = trie_node()
                            current_node.children[data_part] = child_node
                            next = child_node
                        current_node = next
                    data_pointer += 1
            
            data_length = len(data)
            #insert_recur(data, data_length, 0, self.root)
            insert_iter(data, self.root)

        #def words_from(self, node):





    result = trie()
    result.insert(data)
    return result

def test_tree():
    data = 'catnip'
    a_trie = trie(data)
    search_result = a_trie.search('cat')
    print(f'result of search is: {search_result.children.keys()}')
    print(f'words in trie are: {a_trie.words_from(a_trie.root)}')

test_tree()
                    







