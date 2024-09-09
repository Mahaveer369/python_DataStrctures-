class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class  LinkedList:
    def __init__(self):
        #type:ignore
        self.head=None
    def append(self,data):
        if not self.head:
            self.head=Node(data)
        else:
            current=self.head
            while current.next:
                current =current.next
            current.next=Node(data)
    def print_list(self):
        #start at the head of the list
        current = self.head
        while current:
            print(current.data)
            current=current.next
car=LinkedList()
car.append('lambo')
car.append('Range Rover')
car.append('Bently')
print("car Brands are : ")
car.print_list()
            
            

            
        
            