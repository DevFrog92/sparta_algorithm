class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new = Node(value)
        if self.head == None:
            self.tail = new
            self.head = new

        self.tail.next = new
        self.tail = new
        return

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        prev = self.head
        self.head = self.head.next
        return prev.data

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.head is None


queue1 = Queue()
print(queue1.is_empty())
for i in range(5):
    queue1.enqueue(i)

for i in range(5):
    value = queue1.dequeue()
    print(value)

print(queue1.is_empty())