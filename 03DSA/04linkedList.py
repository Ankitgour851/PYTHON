class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        itr = self.head
        llstr = ' '
        while itr:
            suffix = ''
            if itr.next:
                suffix = '--->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr) 

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def insert_at_the_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)

    def insert_at(self,index,data):
        if index <0 or index > self.get_length():
            raise Exception("Invalid Index")     
        if index == 0:
            self.insert_at_the_beginning(data)   
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1

    def remove_at(self,index):
        if index <0 or index > self.get_length():
            raise Exception("Invalid Index") 

        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr .next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)
            # self.insert_at_the_beginning(data)


if __name__ == "__main__":
    # root = LinkedList()
    # root.print()
    # root.insert_at_the_end(567)
    # root.insert_at_the_end(99)
    # root.insert_at_the_end(344)
    # root.insert_at(2, 1000)
    # root.insert_at(1, 40)
    # root.insert_at(-1, 67)
    # root.print()
    # root.remove_at(0)
    # root.print()
    
    # root.insert_at_the_beginning(5)
    # root.insert_at_the_beginning(10)
    # root.insert_at_the_beginning(15)
    # print(root.get_length())
    # root.print()

    ll = LinkedList()
    ll.insert_values(["Banana","mango",'grapes','orange'])
    # ll.insert_at(1, 'blueberry')
    ll.insert_at_the_beginning('blueberry')
    ll.print()

