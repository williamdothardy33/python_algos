def doubly_linked_list(*args):
    class node(object):
        data = None
        previous = None
        next = None

        def __init__(self, data):
            self.data = data

    class doubly_linked_list(object):
        first_node = None
        last_node = None

        def __init__(self, *args):
            for arg in args:
                self.insert_last(arg)

        def insert_last(self, data):
            n = node(data)
            if self.first_node is None:
                self.first_node = n
                self.last_node = n
            else:
                self.last_node.next = n
                n.previous = self.last_node
                self.last_node = n

        def insert_first(self, data):
            n = node(data)
            if self.first_node is None:
                self.first_node = n
                self.last_node = n
            else:
                n.next = self.first_node
                self.first_node.previous = n
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
                        n.previous = current
                        n.next = rest
                        if rest is not None:
                            rest.previous = n
                        break
                    else:
                        current = current.next
                        pointer -= 1




        def delete_first(self):
            result = self.first_node
            if self.first_node == self.last_node:
                self.first_node = None
                self.last_node = None
            else:
                self.first_node = self.first_node.next
                self.first_node.previous = None
            if result is not None:
                return result.data
        
        def delete_last(self):
            result = self.last_node
            if self.first_node == self.last_node:
                self.first_node = None
                self.last_node = None
            else:
                self.last_node = self.last_node.previous
                self.last_node.next = None
            if result is not None:
                return result.data

        def delete_at(self, index):
            pointer = index
            if pointer == 0:
                return self.delete_first()
            else:
                current = self.first_node
                while current is not None:
                    if pointer == 0:
                        if self.last_node == current:
                            self.delete_last()
                        else:
                            before = current.previous
                            after = current.next
                            before.next = after
                            after.previous = before
                        return current.data
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
    

        def reverse(self):
            before = None
            self.first_node = self.last_node
            current = self.last_node
            while current is not None:
                before = current.previous
                current.previous = current.next
                current.next = before
                current = current.next

                if before is not None:
                    self.last_node = before

    result = doubly_linked_list(*args)
    return result

