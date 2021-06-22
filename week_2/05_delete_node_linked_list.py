class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)

    def head_validation(self):
        if self.head == '':
            return '아직 어떠한 노드도 생성되지 않았습니다.'

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
        if index < 0:
            return '양의 인데스를 입력하세요'

        current_node = self.head
        count = 0
        while current_node:
            if count == index:
                return current_node
            count += 1
            current_node = current_node.next
        return '해당하는 인덱스의 값이 없습니다.'

    def add_node(self,index,data):

        if self.head == '':
            return '아직 어떠한 노드도 생성되지 않았습니다.'

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            return

        if index < 0 :
            return '범위 밖에서는 값을 추가할 수 없습니다.'

        # current_node = self.head
        # count = 0
        # while current_node:
        #     if count == index-1:
        #         break
        #     count +=1
        #     current_node = current_node.next

        # refactoring
        current_node = self.get_node(index-1)
        next_node = current_node.next
        current_node.next = new_node
        new_node.next = next_node
        return

    def delete_node(self,index):
        if self.head == '':
            return '아직 어떠한 노드도 생성되지 않았습니다.'
        if index <0:
            return '범위 밖에서는 값을 삭제할 수 없습니다.'
        # head node에 대한 예외처리가 필요하다.
        if index == 0:
            self.head = self.head.next
            return

        target_node = self.get_node(index-1)
        deleted_node = target_node.next
        target_node.next = deleted_node.next
        return



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(1,10)
linked_list.add_node(1,100)
linked_list.add_node(1,200)
linked_list.print_all()
print()
linked_list.delete_node(1)
linked_list.print_all()
print()
linked_list.delete_node(1)
linked_list.print_all()
