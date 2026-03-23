class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None

        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, data):
        new_node = Node(data)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        if self.end is None:
                return None
        current = self.end
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.pref

        print(", ".join(elements))

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(10)
stack.print()

val = stack.pop()
print(f"Извлечённый элемент: {val}")

print("Стек после извлечения")
stack.print()

stack.push(20)
stack.print()
