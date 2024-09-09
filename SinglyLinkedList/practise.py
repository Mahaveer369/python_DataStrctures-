class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        if not self.head:
            self.head=Node(data)#if lsit empty creates the first node and make it the head node
        else:
            current=self.head
            while current.next:
                current = current.next
            current.next=Node(data)#Add a new node after the  existing node.
    def print_list(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
car=LinkedList()
car.append("ferrari 480CG")
car.append("Range rover vogue")
car.append("porsche  GT")        
car.print_list()
            
    