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
# we create class node


class LinkedList:
    def __init__(self):

        self.head = None

    def addNode(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
# we check if the linked list is empty.
# if it is empty is sets the new created node as head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
# if it's not empty we traverse the linked list until current.next is none then we set the new node as current.next

    def displayNodes(self):
        current = self.head
        if current.next is None:
            print("No Nodes to Display! Try Adding a Node first.")
# if current.next is none then there are no nodes to display
        while current.next is not None:
            print(current.value, end=" ")
            current = current.next
# if it is not empty we loop while printing the value updating current.next every time

    def deleteNode(self):
        value = int(input("Please enter the value of the Nodes you would like to delete: "))
        current = self.head
        previous = None
        if current.next is None:
            print("No Nodes to Delete!")
            return
        while current is not None:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
# if the node to be delete is the head we update the head to skip it
                else:
                    previous.next = current.next
                    current = current.next
# if the node to be deleted is not the head we use the pointer previous and assign it to skip the node
            else:
                previous = current
            current = current.next
# if the value we input is not in the node we update the current node to check the next one


class Stack:
    def __init__(self):
        self.value = []

    def push(self, value):
        self.value.append(value)

    def pop(self):
        return self.value.pop()
# we create a class stack


class Queue:
    def __init__(self):
        self.value = []

    def enqueue(self, value):
        self.value.append(value)

    def dequeue(self):
        return self.value.pop(0)

# we create a class queue


def isPalindrome(string):
    stack = Stack()
    queue = Queue()
# we create a stack and queue
    for char in string:
        stack.push(char)
        queue.enqueue(char)
# we place each character in both the queue and stack
    while True:
        char = queue.dequeue()
        rev_char = stack.pop()
        if char != rev_char:
            return False
# we compare the dequeued and popped char
# using the fifo and lifo rules we get a comparison between the reverse of the word and the word in the right way
# this way we can tell is a word is a palindrome


class Student:
    def __init__ (self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade= final_grade
        self.good_attitude = good_attitude
# we create a class student that takes multiples parameters


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
# we create a priority queue

    def addStudent(self):
        import random
        student = createStudent()
# we create an object student
        node = Node(student)
# we put student as value in a node
        if self.size == 0:
            self.head = node
            self.size += 1
# if the pq is empty the node becomes the head
        else:
            current = self.head
# we create a pointer current

            if node.value.good_attitude:
# if the student has a good attitude we place it in the front queue
                if node.value.final_grade > current.value.final_grade:
                    node.next = self.head
                    self.head = node
                    self.size += 1
                    return
# if the final grade of the new node is bigger than that of  current node we add the node in front of that node

                elif node.value.final_grade == current.value.final_grade:
                    if node.value.midterm_grade > current.value.midterm_grade:
                        node.next = self.head
                        self.head = node
                        self.size += 1
                        return
# if they are equal we compare the midterm grade and place
                    elif node.value.midterm_grade == current.value.midterm_grade:
                        if random.randint(0, 1) == 0:
                            node.next = self.head
                            self.head = node
                            self.size += 1
                            return
# we use the random module to randomly generate 0 or 1 to place students if they have the same grade and good attitude
                while current.next and current.next.value.good_attitude:
                    current = current.next
# we iterate over the node to find one without a good attitude
                node.next = current.next
                current.next = node
                self.size += 1
# students with bad attitude are placed last regardless of grade
            else:
                while current.next:
                    current = current.next

                node.next = current.next
                current.next = node
                self.size += 1
# this loop makes sure students with good attitudes and lower grades than existing student are placed correctly


    def interView(self):
        if self.size == 0:
            print("No student to interview. Try adding a student first.")
        elif self.size == 1:
            print("You should interview:", self.head.value.name)
            self.head = None
            self.size -= 1
        else:
            print("You should interview:", self.head.value.name)
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1
# this function uses the fifo rule to pop the student to be interviewed


def createStudent():
    name = input("Please enter the name of the student: ")
    midterm_grade = input("Please enter their midterm grade: ")
    final_grade = input("Please enter their final grade: ")
    good_attitude = eval(input("Please enter a boolean to describe their good attitude: "))
    student = Student(name, midterm_grade, final_grade, good_attitude)
    return student
# we take user input and create the student object

def evaluate(string):
    operators_lst = {"+", "-", "*", "/"}
    parentheses = {"(", ")"}
# we create 2 set of operators and parentheses

    def precedence(op):
        if op in {"+", "-"}:
            return 1
        elif op in {"*", "/"}:
            return 2
        else:
            return 0
# we assign a precedent to the sets

    def applyOperator():
        op = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        result = int(eval(operand1 + op + operand2))
        operands.push(str(result))
# it pops the operands and operator the evaluates them
    operators = Stack()
    operands = Stack()

    for char in string:
        if char.isnumeric():
            operands.push(char)
# we take a string and iterate over it
        elif char in operators_lst or char in parentheses:
            if char == "(":
                operators.push(char)
# if the char is a number it is added to the stack operands
            # If it's a closing parenthesis, apply operators until an open parenthesis is encountered
            elif char == ")":
                while operators.value[-1] != "(":
                    applyOperator()
                operators.pop()
# If it's a closing parenthesis, apply operators until an open parenthesis is encountered

            else:
                while operators.value and operators.value[-1] in operators_lst \
                        and precedence(operators.value[-1]) >= precedence(char):
                    applyOperator()
                operators.push(char)
# we apply operators based on precedence before adding the current operator

    while operators.value:
        applyOperator()
# we apply remaining operators

    return operands.pop()
# return the result
# this function implements the shunting Yard algorithm to make sure the order of operators is correct.
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adj_matrix = [[0]*vertices for _ in range(vertices)]

    def addVertex(self):
        self.vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.vertices)
        print("You added", self.vertices-1," as a vertex\n")


    def removeVertex(self, vertex):
        if vertex < 0 or vertex >= self.vertices:
            print("Invalid vertex", vertex, "\n")
        else:
            del self.adj_matrix[vertex]
            for row in self.adj_matrix:
                del row[vertex]
            self.vertices -= 1
            print("You removed vertex", vertex, "\n")
# we take an input and use it to remove the vertex and its row in the adjacency matrix
    def removeEdge(self,v1,v2):
        if ((v1 < 0 or v1 >= self.vertices) and (v2 < 0 or v2 >= self.vertices)):
            print("Invalid vertices", v1, "and", v2, "\n")
        else:
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0
            print("You removed edge between vertices", v1, "and", v2, "\n")
# basically removing the edge but using 2 inputted vertex
    def addEdge(self, v1, v2):
        if 0 <= v1 < self.vertices and 0 <= v2 < self.vertices:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1
            print("You added an edge between vertices", v1, "and", v2, "\n")
        elif ((v1 < 0 or v1 >= self.vertices)
              and (v2 < 0 or v2 >= self.vertices)):
            print("Invalid vertices", v1, "and", v2, "\n")
        elif v1 < 0 or v1 >= self.vertices:
            print("Invalid vertex", v1, "\n")
        else:
            print("Invalid vertex", v2, "\n")

    def displayGraph(self, n):
        if len(self.adj_matrix) == 0:
            print("Graph is empty!\n")
            return
        for i in range(len(self.adj_matrix)):
            degree = sum(self.adj_matrix[i])
            if degree >= n:
                print(i, end=" ")
        print("\n")
# the program takes a degree as n as print the vertices that are equal or more than n


def graphMenu():
    print("Welcome to the Graph Menu: "
          "\n A. Add Vertex"
          "\n B.Display Edge"
          "\n C.Remove Vertex"
          "\n D.Remove Edge"
          "\n E.Display vertices with a degree of X or more"
          "\n F.Return to Main Menu")




















