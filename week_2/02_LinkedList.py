# LinkedList
# 노드는 값과 포인터로 구성된다.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first_node = Node(5)
second_node = Node(12)
first_node.next = second_node

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)

    def append(self,data):
        if self.head == "":
            self.head = Node(data)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data)
        return

    def print_all(self):
        if self.head == '':
            print('아직 어떠한 노드도 생성되지 않았습니다.')
            return
        cur_node = self.head
        while cur_node:
            print(cur_node.data,end=' ')
            cur_node = cur_node.next
        return

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()