from stack_and_queue_processes import stack

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

        # def reverse(self):
        #     s = stack()
        #     while self.first_node is not None:
        #         data = self.delete_first()
        #         s.push(data)

        #     while s.is_empty() == False:
        #         data = s.pop()

        #         print(f'data from stack pop: {data}')
        #         self.insert_last(data)
            

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

def queue(*args):
    class queue(object):
        underlying = doubly_linked_list(*args)
        def __init__(self, *args):
            self.underlying = doubly_linked_list(*args)

        def enqueue(self, data):
            self.underlying.insert_last(data)

        def dequeue(self):
            return self.underlying.delete_first()
        
        def show(self):
            return self.underlying.show()
        
        def peek(self):
            return self.underlying.read(0)

    return queue(*args)    

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
                        if rest.next is not None:
                            current.next = rest.next
                            return rest.data
                        else:
                            current.next = None
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
            s = stack()
            while self.first_node is not None:
                data = self.delete_first()
                s.push(data)

            while s.is_empty() == False:
                data = s.pop()

                print(f'data from stack pop: {data}')
                self.insert_last(data)
            
    result = doubly_linked_list(*args)
    return result        

        




def test_node():
    ll = doubly_linked_list(1,2,3,4)
    result = ll.show()
    print(result)
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
    print(f'show original: {ll.show()}')
    print(f'delete first: {ll.delete_first()}')
    print(f'show after delete first: {ll.show()}')
    print(f'delete last: {ll.delete_last()}')
    print(f'show after delete last: {ll.show()}')
    print(f'delete all')
    while ll.first_node is not None:
        ll.delete_first()
    print(f'show after delete all: {ll.show()}')
    print('populate 3,5,7,9')
    for n in range(3,10,2):
        ll.insert_last(n)
    print(f'after populating: {ll.show()}')
    print(f'fill in 2,4,6,8,10')
    for data, index in zip(range(2,11,2), range(0, 9, 2)):
        ll.insert_at(data, index)
    print(f'show after filling in: {ll.show()}')
    print(f'insert at index that 20')
    ll.insert_at(20,20)
    print(f'show after inserting at 20: {ll.show()}')


    ll_d = doubly_linked_list(1,5)
    print(f'show original: {ll_d.show()}')
    print(f'deleting index 2 of ll_d: {ll_d.delete_at(2)}')
    print(f'show ll_d after deleting index 2: {ll_d.show()}')
    print(f'deleting index 1 of ll_d: {ll_d.delete_at(1)}')
    print(f'show ll_d after deleting index 1: {ll_d.show()}')
    print(f'first node of ll_d: {ll_d.first_node.data}')
    print(f'last node of ll_d: {ll_d.last_node.data}')
    print(f'deleting index 0: {ll_d.delete_at(0)}')
    print(f'show after deleting index 0: {ll_d.show()}')
    print(f'delete index 20 of emtpy array: {ll_d.delete_at(20)}')
    print(f'no arg doubly linked list:')

    q1 = queue()
    print(f'q1 is {q1}: {q1.show()}')

    q2 = queue(1,2,3,4,5)
    print(f'q2 is {q2}: {q2.show()}')

    print(f'add 1 to q1')
    q1.enqueue(1)
    print(f'show after adding 1: {q1.show()}')

    ll_rv = doubly_linked_list(1,2,3,4,5,6)
    print(f'original ll_rv: {ll_rv.show()}')
    ll_rv.reverse()
    print(f'll_rv reverse: {ll_rv.show()}')



    








test_node()