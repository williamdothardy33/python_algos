def stack():
    class stack(object):
        underlying = []
    
        def __init__(self) -> None:
            pass
        def push(self, e):
            self.underlying.append(e)
    
        def pop(self):
            return self.underlying.pop()
    
        def is_empty(self):
            if len(self.underlying) == 0:
                return True
            else:
                return False
            
        def peek(self):
            return self.underlying[len(self.underlying) - 1]
        
        def to_array(self):
            result = []
            pointer = 0
            while pointer < len(self.underlying):
                result.append(self.underlying[pointer])
                pointer += 1
    
            return result
    
        def show(self):
            return self.to_array()
    result = stack()
    return result