class Stack:

    def __init__(self):
        self._lst = []

    def push(self, value):
        self._lst.append(value)

    def pop(self):
        return self._lst.pop()

    def peek(self):
        return self._lst[-1]

    def __len__(self):
        return len(self._lst)

    def __bool__(self):
        return len(self) == 0

    def __repr__(self):
        return "STACK: " + ", ".join([str(v) for v in self.__lst]) + " (top)"

    def __eq__(self, other):
        return self.__lst == other.__lst