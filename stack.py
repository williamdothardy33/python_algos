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