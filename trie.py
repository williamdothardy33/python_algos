def trie(data):
    class trie_node():
        children = None
        def __init__(self):
            self.children = {}

    class trie():
        root = None
        def __init__(self):
            self.root = trie_node()

        def search(self, search_term, node):
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
            
            #return search_recur(search_term, search_length, node, 0)
            return search_iter(search_term, node)
        
        def longest_prefix(self, search_term):
            search_pointer = 0
            search_length = len(search_term)
            current = self.root
            while search_pointer < search_length:
                search_part = search_term[search_pointer]
                next = self.search(search_part, current)
                if next is not None:
                    current = next
                    search_pointer += 1
            if search_pointer > 0:
                return current
            
    
        

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

        def contents_from(self, node):
            def data_from_recur(prefix, prefix_node, result, results):
                if prefix != '*':
                    for next_prefix, next_node in prefix_node.children.items():
                        data_from_recur(next_prefix, next_node, result + prefix, results)        
                else:
                    results.append(result)

            results = []

            for prefix, suffixes in node.children.items():
                result = ''
                data_from_recur(prefix, suffixes, result, results)

            return results
        
        def auto_suggest(self, search_term):
            results = []
            next_node = self.search(search_term, self.root)
            if next_node is not None:
                for result in self.contents_from(next_node):
                    results.append(search_term + result)
            return results
        
        def auto_suggest_fix(self, search_term):
            search_pointer = 0
            search_length = len(search_term)
            current = self.root
            prefix = ''
            while search_pointer < search_length:
                search_part = search_term[search_pointer]
                next = self.search(search_part, current)
                if next is not None:
                    prefix += search_part
                    current = next
                    search_pointer += 1
                else:
                    break
            
            if search_pointer == search_length:
                return [search_term]
            else:
                if search_pointer > 0:
                    results = []
                    for result in self.contents_from(current):
                        results.append(prefix + result)
                    return results
        
        def trie_keys(self, node):
            def trie_keys_recur(node, results):
                if node is not None:
                    for key, node in node.children.items():
                        results.append(key)
                        trie_keys_recur(node, results)

            results = []
            trie_keys_recur(node, results)
            return results









    result = trie()
    result.insert(data)
    return result

def test_tree():
    data1 = 'calorie'
    data2 = 'cantrip'
    data3 = 'canter'
    data4 = 'cancel'
    data5 = 'cat'
    data6 = 'catnip'
    data7 = 'catnap'
    

    a_trie = trie(data1)
    a_trie.insert(data2)
    a_trie.insert(data3)
    a_trie.insert(data4)
    a_trie.insert(data5)
    a_trie.insert(data6)
    a_trie.insert(data7)


    #search_result = a_trie.search('catn'. a_trie.root)
    #print(f'result of search is: {search_result.children.keys()}')
    #print(f'words in trie are: {a_trie.contents_from(a_trie.root)}')
    result = a_trie.auto_suggest('cat')
    print(f'result of auto_suggest for \'cat\' is: {result}')
    #keys = a_trie.trie_keys(a_trie.root)
    #print(f'keys in a_trie are: {keys}')
    result1 = a_trie.auto_suggest_fix('candida')
    print(f'result of auto_suggest_fix for \'ca\' is: {result1} ')

test_tree()
                    







