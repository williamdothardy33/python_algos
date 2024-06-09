from min_binary_heap import min_binary_heap
def min_priority_queue(priority, data):
    class min_priority_queue(object):
        underlying = min_binary_heap()
        def __init__(self, priority, data):
            self.underlying.insert_item(priority, data)

        def enqueue(self, priority, data):
            self.underlying.insert_item(priority, data)

        def dequeue(self):
            return self.underlying.delete()
        
        def show(self):
            return self.underlying.show()
        
        def peek(self):
            return self.underlying.peek()
        
        def not_empty(self):
            return self.underlying.is_empty() == False

    result = min_priority_queue(priority, data)
    return result