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
            current= self.head
            while current.next:
                current = current.next
            current.next = new_node

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
        self.value = []

    def push(self, value):
        self.value.append(value)

    def pop(self):
        return self.value.pop()


class Queue:
    def __init__(self):
        self.value = []

    def enqueue(self, value):
        self.value.append(value)

    def dequeue(self):
        return self.value.pop(0)


def isPalindrome(string):
    stack = Stack()
    queue = Queue()
    for char in string:
        stack.push(char)
        queue.enqueue(char)
    while True:
        char = queue.dequeue()
        rev_char = stack.pop()
        if char != rev_char:
            return False


class Student:
    def __init__ (self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade= final_grade
        self.good_attitude = good_attitude


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0


    def addStudent(self, student):
        import random
        node = Node(student)
        if self.size == 0:
            self.head = node
            self.size += 1
        else:
            current = self.head
            while current.next and node.value.good_attitude:
                if node.value.final_grade > current.value.final_grade:
                    node.next = current
                    self.head = node
                    self.size += 1
                    return
                elif node.value.final_grade == current.value.final_grade:
                    if node.value.midterm_grade > current.value.midterm_grade:
                        node.next = current.next
                        current.next = node
                        self.size += 1
                        return
                    elif node.value.midterm_grade == current.value.midterm_grade:
                        if random.randint(0, 1) == 0:
                            node.next = self.head
                            self.head = node
                            self.size +=1
                        else:
                            current.next = self.head
                            self.head = current
                            self.size += 1
                        return
                current = current.next

            if not current.next and not node.value.good_attitude:
                current.next = node
                self.size += 1
            else:
                while current.next_node:
                    current = current.next
                current.next = node
                self.size +=1








