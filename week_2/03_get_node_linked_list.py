class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        current_node = self.head
        while current_node:
            print(current_node.data,end=' ')
            current_node = current_node.next
        return

    def get_node(self,index):
        if self.head == '':
            return '아직 어떠한 노드도 생성되지 않았습니다.'
        
        current_node = self.head
        count = 0
        while current_node:
            if count == index:
                return current_node.data
            count += 1
            current_node = current_node.next
        return '해당하는 인덱스의 값이 없습니다.'

linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(11))
