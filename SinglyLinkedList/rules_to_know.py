"""In a LinkedList, you can use either append or insert to add data, depending on where you want to add the new node:
Append:
Adds a new node at the end of the LinkedList.
Efficient, as it only requires updating the next reference of the last node.
Typical implementation:
Python """
def append(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
    else:
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
"""


**Insert**:


*   Adds a new node at a **specific position** in the LinkedList.
*   May require shifting existing nodes, making it less efficient than append.
*   Typical implementation:


```python """
def insert(self, data, position):
    new_node = Node(data)
    if position == 0:
        new_node.next = self.head
        self.head = new_node
    else:
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node



"""  **Other insertion methods**:


*   `insert_at_head(data)`: Adds a new node at the beginning of the LinkedList.
*   `insert_after_node(node, data)`: Adds a new node after a specific node.


Choose the method that best fits your use case:


*   Use `append` when adding nodes to the end of the list.
*   Use `insert` when adding nodes at specific positions.
*   Use specialized insertion methods for specific requirements.


Example usage:


```python"""

ll = LinkedList()
ll.append('A')  # A
ll.append('B')  # A -> B
ll.insert('C', 0)  # C -> A -> B
ll.insert('D', 2)  # C -> A -> D -> B