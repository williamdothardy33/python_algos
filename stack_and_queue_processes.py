def reverse(ss):
    # can only push to the right of the array and pop the rightmost element of the array and read the rightmost element of the array
    # in python can only use append, pop with no arguments and stack[len(stack) - 1] operation for read
    # don't know how to make classes in python yet and don't have access to internet to import Stack, or Queue classes
    stack = []
    result = ''
    for s in ss:
        stack.append(s)

    while len(stack) != 0:
        result += stack.pop()

    return result

def test_reverse():
    ss = 'abcde'
    print(reverse(ss))

test_reverse()

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

    def show(self):
        return self.underlying