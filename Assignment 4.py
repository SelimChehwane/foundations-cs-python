def displayMenu():
    user_name = input("Please enter your name: ")
    print()
    print("Hello", user_name,", welcome to my fourth assignment!")
    print()
    print("Please select an option to start: " 
          "\n 1.Singly Linked list"
          "\n 2.Check if Palindrome"
          "\n 3.Priority Queue"
          "\n 4.Evaluate and Infix Expression"
          "\n 5.Graph"
          "\n 6.Exit")

def nodeMenu():
    print("Welcome to the Nodes Menu: "
          "\n A. Add Nodes"
          "\n B.Display Nodes"
          "\n C.Search for & Delete Node"
          "\n D.Return to Main Menu")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, value):
        value = int(input("Please enter the value of the new Node: "))
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def displayNodes(self):
        current = self.head
        if current.next is None:
            print("No Nodes to Display! Try Adding a Node first.")
        while current != None:
            print(current.value, end=" ")
            current = current.next

    def deleteNode(self):
        value = int(input("Please enter the value of the Nodes you would like to delete: "))
        current = self.head
        previous = None
        if current.next is None:
            print("No Nodes to Delete!")
            return
        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                    current = current.next
            else:
                previous = current
            current = current.next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1

    def dequeue(self):
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value










