from doubly_linked_list import doubly_linked_list
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