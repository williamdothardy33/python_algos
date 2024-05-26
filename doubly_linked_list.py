class node(object):
    data = None
    previous = None
    next = None

    def __init__(self, data, previous, next):
        self.data = data
        self.previous = previous
        self.next = next

def make_linked_list(first_node, last_node):
    class linked_list(object):
        first_node = None
        last_node = None

        def __init__(self, first_node, last_node):
            self.insert_last(first_node)
            self.insert_last(last_node)

        def insert_last(self, node):
            if self.first_node is None:
                self.first_node = node
            elif self.last_node is None:
                self.first_node.next = node
                node.previous = self.first_node
                self.last_node = node
            else:
                self.last_node.next = node
                node.previous = self.last_node
                self.last_node = node

        def insert_first(self, node):
            if self.first_node is None:
                self.first_node = node
            elif self.last_node is None:
                node.next = self.first_node
                self.first_node.previous = node
                self.first_node = node
                self.last_node = self.first_node
            else:
                node.next = self.first_node
                self.first_node.previous = node
                self.first_node = node

        #def insert(self, index, value)

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
    



    result = linked_list(first_node, last_node)
    return result

        




def test_node():

    n1 = node(3, None, None)
    n2 = node(4, None, None)
    ll = make_linked_list(n1, n2)
    print(ll)
    print(f'first node: {ll.first_node}')
    print(f'first node value: {ll.first_node.data}')
    print(f'first node previous: {ll.first_node.previous}')
    print(f'first node next {ll.first_node.next}')
    print(f'first node next\'s data: {ll.first_node.next.data}')
    print(f'first node next previous data {ll.first_node.next.previous.data}')
    print(f'first node next next: {ll.first_node.next.next}')
    print(f'read index 0: {ll.read(0)}')
    print(f'read index 1: {ll.read(1)}')
    print(f'read index 2: {ll.read(2)}')
    print(f'lookup 3: {ll.index_of(3)}')
    print(f'lookup 4: {ll.index_of(4)}')
    print(f'lookup 5: {ll.index_of(5)}')






test_node()