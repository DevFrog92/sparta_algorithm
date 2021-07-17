class Node:
    def __init__(self,data):
        self.data = data
        self.before = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
            return

        prev = self.head
        new = Node(value)
        new.before = prev
        self.head = new
        return

    def pop(self):
        if self.head == None:
            return 'Stack에 어떠한 요소도 없습니다.'
        now = self.head
        self.head = now.before
        return now.data

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None


stack1 = Stack()
print(stack1.is_empty())
for i in range(5):
    stack1.push(i)
print(stack1.is_empty())

for _ in range(5):
    pop_value = stack1.pop()
    print(pop_value)

print(stack1.is_empty())