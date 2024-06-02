def linked_list(*args):
    class node(object):
        data = None
        next = None

        def __init__(self, data):
            self.data = data

    class linked_list(object):
        first_node = None

        def __init__(self, *args):
            for arg in args:
                self.insert_last(arg)

        def insert_last(self, data):
            n = node(data)
            if self.first_node is None:
                self.first_node = n
            else:
                current = self.first_node
                while current.next is not None:
                    current = current.next
                current.next = n

        def insert_first(self, data):
            n = node(data)
            if self.first_node is None:
                self.first_node = n
            else:
                n.next = self.first_node
                self.first_node = n

        def insert_at(self, data, index):
            pointer = index
            if pointer == 0:
                self.insert_first(data)
            else:
                current = self.first_node
                while current is not None:
                    if pointer == 1:
                        n = node(data)
                        rest = current.next
                        current.next = n
                        n.next = rest
                        break
                    else:
                        current = current.next
                        pointer -= 1

        def delete_first(self):
            result = self.first_node
            if result is not None:
                self.first_node = result.next
                return result.data
        
        def delete_last(self):
            current = self.first_node
            if current is not None and current.next is None:
                return current.data
            else:
                while current.next is not None:
                    if current.next.next is None:
                        result = current.next
                        current.next = None
                        return result.data

        def delete_at(self, data, index):
            pointer = index
            if pointer == 0:
                self.delete_first(data)
            else:
                current = self.first_node
                while current is not None:
                    if pointer == 1:
                        rest = current.next
                        if rest is not None:
                            result = rest.data
                            if rest.next is not None:
                                current.next = rest.next
                            else:
                                current.next = None
                            return result.data
                    else:
                        current = current.next
                        pointer -= 1

        def delete_node(self, n):
            if n.next is not None:
                n.data = n.next.data
                n.next = n.next.next
            else:
                n.data = None
                n.next = None

        def get_node(self, index):
            current = self.first_node
            pointer = index
            while current is not None:
                if pointer == 0:
                    return current
                else:
                    current = current.next
                    pointer -= 1


        def show(self):
            prefix = '['
            current = self.first_node
            if  current is not None:
                prefix += f'{current.data}'
                n = current.next
                while n is not None:
                    prefix += f', {n.data}'
                    n = n.next

            return prefix + ']'

        def read(self, index):
            current = self.first_node
            pointer = index
            while current is not None:
                if pointer == 0:
                    return current.data
                else:
                    current = current.next
                    pointer -= 1

        def index_of(self, value):
            current = self.first_node
            pointer = 0
            while current is not None:
                if current.data == value:
                    return pointer
                else:
                    current = current.next
                    pointer += 1

        def last_node(self):
            if self.first_node is not None and self.first_node.next is None:
                return self.first_node
            else:
                current = self.first_node
                while current.next is not None:
                    current = current.next
                return current

        def reverse(self):
            current = self.first_node
            if current is not None and current.next is not None:
                after = current.next
                current.next = None
                while after is not None:
                    next_after = after.next
                    after.next = current
                    self.first_node = after
                    current = after
                    after = next_after

            
    result = linked_list(*args)
    return result


def test_linked_list():
    t = linked_list(1,2,3,4,5)
    print(f't before reversing: {t.show()}')
    t.reverse()
    print(f't reversed: {t.show()}')
    print(f'middle node removed')
    node_to_delete = t.get_node(2)
    t.delete_node(node_to_delete)
    print(f'after deleting {t.show()}')
    last_node = t.last_node()
    t.delete_node(last_node)
    print(f'last node data: {last_node.data}')
    print(f'after deleting last {t.show()}')
    print(last_node)

#test_linked_list()