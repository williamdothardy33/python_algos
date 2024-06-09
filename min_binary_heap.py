#this is a custom heap, I don't have access to internet and I don't know if and how there is a comparator interface/ordering typeclass similar to java/scala
#for giving an ordering to custom data types in python

class wrap():
    data = None
    def __init__(self, data):
        self.data = data

    def show(self):
        return str(self.data)

class item():
        ordinal = None
        value = None

        def __init__(self, ordinal=None, value=None):
            self.ordinal = ordinal
            self.value = value
        
        def show(self):
            return f'ordinal: {self.ordinal}, value: {self.value.show()}'
        
def number_items(*args):
            result = []
            for arg in args:
                result.append(item(arg, wrap(arg)))
            return result



def min_binary_heap():
    class min_binary_heap():
        underlying = []
        def __init__(self) -> None:
            pass

        def is_empty(self):
            return len(self.underlying) == 0

        def make(self, *args):
            for arg in args:
                self.insert(arg)

        def make_from_items(self, *args):
            for arg in args:
                self.insert_item(arg)

        def peek(self):
            if len(self.underlying) != 0:
                return self.underlying[0]
            
        def parent(self, child_node):
            if child_node - 1 < 0:
                return None
            else:
                result = int((child_node - 1) / 2)
                return result
            
        def left_child(self, parent_node):
            result = 2 * parent_node + 1
            if result < len(self.underlying):
                return result
            
        def right_child(self, parent_node):
            result = 2 * parent_node + 2
            if result < len(self.underlying):
                return result
            
        def swap(self, node1, node2):
            node1_data = self.underlying[node1]
            self.underlying[node1] = self.underlying[node2]
            self.underlying[node2] = node1_data

            
        # def bubble_recur(self, node):
        #     if node is not None:
        #         parent_node = self.parent(node)
        #         if parent_node is not None:
        #             parent_data = self.underlying[parent_node]
        #             node_data = self.underlying[node]

        #             if parent_data < node_data:
        #                 self.swap(node, parent_node)
        #                 self.bubble_recur(parent_node)

        def bubble_recur(self, node_data, current):
            if current is not None:
                current_data = self.underlying[current]
                current_data_ordinal = current_data.ordinal
                node_data_ordinal = node_data.ordinal
                if node_data_ordinal <= current_data_ordinal:
                    next_parent = self.parent(current)
                    self.underlying[current] = self.bubble_recur(node_data, next_parent)
                else:
                    return node_data
                return current_data
            else:
                return node_data
            
        def bubble_iter(self, index):
            data = self.underlying[index]
            data_ordinal = data.ordinal
            data_pointer = index
            parent_pointer = int((data_pointer - 1) / 2)
            while data_pointer > 0:
                parent_data = self.underlying[parent_pointer]
                parent_data_ordinal = parent_data.ordinal
                if data_ordinal > parent_data_ordinal:
                    break
                else:
                    self.underlying[parent_pointer] = data
                    self.underlying[data_pointer] = parent_data
                    data_pointer = parent_pointer
                    parent_pointer = int((data_pointer - 1) / 2)
                    


#the only reason you should go right is if both left and right children exist and left child is smaller than right
        def sink_recur(self, node_data, current):
            if current is not None:
                current_data = self.underlying[current]
                node_data_ordinal = node_data.ordinal
                current_data_ordinal = current.ordinal
                if node_data_ordinal >= current_data_ordinal:
                    current_left = self.left_child(current)
                    current_right = self.right_child(current)
                    if current_left is not None:
                        left_data = self.underlying[current_left]
                        left_data_ordinal = left_data.ordinal
                        if current_right is not None:
                            right_data = self.underlying[current_right]
                            right_data_ordinal = right_data.ordinal
                            if left_data_ordinal < right_data_ordinal:
                                self.underlying[current] = self.sink_recur(node_data, current_left)
                            else:
                                self.underlying[current] = self.sink_recur(node_data, current_right)
                        else:
                            self.underlying[current] = self.sink_recur(node_data, current_left)
                    else:
                        self.underlying[current] = self.sink_recur(node_data, current_left)
                else:
                    return node_data
                
                return current_data
            
            else:
                return node_data
            
        def sink_iter(self, index):
            last_idx = len(self.underlying) - 1
            data = self.underlying[index]
            data_ordinal = data.ordinal
            data_pointer = index
            
            while data_pointer < len(self.underlying):
                left_pointer = 2 * data_pointer + 1
                right_pointer = 2 * data_pointer + 2
                if left_pointer <= last_idx:
                    data_left = self.underlying[left_pointer]
                    data_left_ordinal = data_left.ordinal
                    if right_pointer <= last_idx:
                        data_right = self.underlying[right_pointer]
                        data_right_ordinal = data_right.ordinal
                        if data_left_ordinal < data_right_ordinal:
                            if data_ordinal > data_left_ordinal:
                                self.underlying[data_pointer] = data_left
                                self.underlying[left_pointer] = data
                                data_pointer = left_pointer
                            else:
                                break
                        else:
                            if data_ordinal > data_right_ordinal:
                                self.underlying[data_pointer] = data_right
                                self.underlying[right_pointer] = data
                                data_pointer = right_pointer
                            else:
                                break
                    else:
                        if data_ordinal > data_left_ordinal:
                            self.underlying[data_pointer] = data_left
                            self.underlying[left_pointer] = data
                            data_pointer = left_pointer
                        else:
                            break
                else:
                    break

        
            
        def insert(self, data):
            self.underlying.append(data)
            current = len(self.underlying) - 1
            self.bubble_iter(current)

        def insert_item(self, ordinal, data):
            data_item = item(ordinal, data)
            self.insert(data_item)

        def delete(self):
        
            if len(self.underlying) > 0:
                root = 0
                result = self.underlying[root]
                last_node = len(self.underlying) - 1
                self.underlying[root] = self.underlying[last_node]
                root_data = self.underlying[root]
                self.sink_iter(root)
                self.underlying.pop()
                return result.value
            else:
                return []

        def show(self):
            result = '['
            for item in self.underlying:
                result += f'{item.show()}| '
            result = result.removesuffix('| ')
            result += ']'
            return result
        
    result = min_binary_heap()
    return result

# def test_max_binary_heap():
#     mbh = min_binary_heap()
#     data = number_items(1,2,3,4,17,5,8,6,4,9,3)
#     mbh.make(*data)
#     print(mbh.show())

#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())


#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())


#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())

#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())

#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())

#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())

#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())

#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())

#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())

#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())

#     print('deleting root...')
#     print(f'root is: {mbh.delete().show()}')
#     print(f'after deleting...')
#     print(mbh.show())

# test_max_binary_heap()
            




            

