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

    def insert_after_values(self,data_after,data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,itr.next)
            return
        
        itr = self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break

            itr=itr.next
        
    def remove_by_vale(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next


if __name__ == "__main__":
    ll=LinkedList()
    ll.insert_values(["banana","mango",'grapes','orange'])
    ll.print()
    ll.insert_after_values("mango", "apple")
    ll.print()
    ll.remove_by_vale("orange")
    ll.print()
    ll.remove_by_vale("mango")
    ll.remove_by_vale("apple")
    ll.remove_by_vale("banana")
    ll.remove_by_vale("grapes")

    ll.print()