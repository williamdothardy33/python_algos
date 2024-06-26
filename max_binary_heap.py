def max_binary_heap():
    class max_binary_heap():
        underlying = []
        def __init__(self) -> None:
            pass

        def make(self, *args):
            for arg in args:
                self.insert(arg)

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
                if current_data <= node_data:
                    next_parent = self.parent(current)
                    self.underlying[current] = self.bubble_recur(node_data, next_parent)
                else:
                    return node_data
                return current_data
            else:
                return node_data
            
        def bubble_iter(self, index):
            data = self.underlying[index]
            data_pointer = index
            parent_pointer = int((data_pointer - 1) / 2)
            while data_pointer > 0:
                parent_data = self.underlying[parent_pointer]
                if parent_data > data:
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
                if current_data >= node_data:
                    current_left = self.left_child(current)
                    current_right = self.right_child(current)
                    if current_left is not None:
                        left_data = self.underlying[current_left]
                        if current_right is not None:
                            right_data = self.underlying[current_right]
                            if left_data > right_data:
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
            data_pointer = index
            
            while data_pointer < len(self.underlying):
                left_pointer = 2 * data_pointer + 1
                right_pointer = 2 * data_pointer + 2
                if left_pointer <= last_idx:
                    data_left = self.underlying[left_pointer]
                    if right_pointer <= last_idx:
                        data_right = self.underlying[right_pointer]
                        if data_left > data_right:
                            if data < data_left:
                                self.underlying[data_pointer] = data_left
                                self.underlying[left_pointer] = data
                                data_pointer = left_pointer
                            else:
                                break
                        else:
                            if data < data_right:
                                self.underlying[data_pointer] = data_right
                                self.underlying[right_pointer] = data
                                data_pointer = right_pointer
                            else:
                                break
                    else:
                        if data < data_left:
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

        def delete(self):
        
            if len(self.underlying) > 0:
                root = 0
                result = self.underlying[root]
                last_node = len(self.underlying) - 1
                self.underlying[root] = self.underlying[last_node]
                root_data = self.underlying[root]
                self.sink_iter(root)
                self.underlying.pop()
                return result
            else:
                return []

        def show(self):
            print(self.underlying)
    result = max_binary_heap()
    return result

def test_max_binary_heap():
    mbh = max_binary_heap()
    mbh.make(1,2,3,4,17,5,8,6,4,9,3)
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

    print('deleting root...')
    print(f'root is: {mbh.delete()}')
    print(f'after deleting...')
    mbh.show()

test_max_binary_heap()
            




            

