class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
      
    def __repr__(self):
        return f"{self.value}"    
 
class LinkedList:
    def __init__(self, node):
        self.head = None
        self.node = node

    def printList(self):
         current_node = self.head 
         while current_node is not None:
            print(f"{current_node} ->")
            current_node = current_node.next

    def add_back(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

if __name__ == '__main__':
    ll = LinkedList(Node('a'))
    
    ll.printList()
    ll.add_back(Node('b'))
    ll.add_back(Node('c'))
    ll.add_back(Node('d'))    
    ll.printList()