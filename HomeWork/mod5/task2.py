class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.end is None:
            return None

        val = self.end.data
        self.end = self.end.nref

        if self.start is None:
            self.start.pref = None
        else:
            self.end = None

        return val

    def push(self, data):
        new_node = Node(data)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref=self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, data):

        if n<0:
            return

        new_node = Node(data)
        if n ==0:
            new_node.pref = self.start
            if self.start is None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return
        current = self.start
        position = 0
        while current is not None and position <n -1:
            current = current.pref
            position += 1

        if current is None:
            print(f"Позиция {n} выходит за границы списка")
            return
        next_node = current.nref
        new_node.pref = current
        new_node.nref = next_node
        current.nref = new_node

        if next_node is None:
            next_node.pref = new_node
        else:
            self.end = new_node

    def print(self):
        if self.start is None:
                return None
        current = self.start
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.nref

        print(", ".join(elements))

queue = Queue()

queue.push(1)
queue.push(2)
queue.push(10)
queue.print()

val = queue.pop()
print(f"Извлечённый элемент: {val}")

print("Очередь после извлечения")
queue.print()

queue.insert(1,22, )

print("Очердь после вставки")
queue.print()

queue.push(20)
queue.print()
