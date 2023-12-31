def displayMenu():
    print(" 1.Singly Linked list"
          "\n 2.Check if Palindrome"
          "\n 3.Priority Queue"
          "\n 4.Evaluate and Infix Expression"
          "\n 5.Graph"
          "\n 6.Exit")

def nodeMenu():
    print("\n A. Add Nodes"
          "\n B.Display Nodes"
          "\n C.Search for & Delete Node"
          "\n D.Return to Main Menu\n")
def nodeMain():
    print("\nWelcome to the Nodes Menu: ")
    choice = ""
    LL = LinkedList()
    while choice != "D":
        nodeMenu()
        choice = input("Please enter the option you would like to access: ")
        if choice == "A":
            v = input("\nPlease enter the numerical value you would like to add: ")
            LL.addNode(v)
        elif choice == "B":
            LL.displayNodes()
        elif choice == "C":
            value = input("\nPlease enter the value of the Nodes you would like to delete: ")
            LL.deleteNode(value)
        elif choice != "D":
            print("Invalid option.")
    print("\nYou're returning to the Main Menu\n")


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
        if new_node.value.isnumeric():
            if not self.head:
                self.head = new_node
    # we check if the linked list is empty.
    # if it is empty is sets the new created node as head

            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
            print("\nYou have added ", value, "to the LinkedList.")
        else:
            print("\nInvalid value.")
    # if it's not empty we traverse the linked list until current.next is none then we set the new node as current.next
    # O(n) is the time complexity where n is the number of nodes entered by the user

    def displayNodes(self):
        current = self.head
        if current is None:
            print("\nNo Nodes to Display! Try Adding a Node first.")
# if current.next is none then there are no nodes to display
        while current is not None:
            print(current.value, end=" ")
            current = current.next
# if it is not empty we loop while printing the value updating current.next every time
# O(n) is the time complexity where n is the number of nodes entered by the user

    def deleteNode(self, value):
        if self.head is None:
            print("\nThe LinkedList is empty. No Nodes to Delete!")
            return
        while not value.isdigit():
            print("\nInvalid input. Please enter an integer.")
            value = input("\nPlease enter the value of the Nodes you would like to delete: ")
        # we validate the input to be a digit
        current = self.head
        previous = None

        while current is not None:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next
# after validating we iterate through the list removing all instances of the value in the linked list
# O(n) is the time complexity where n is the number of nodes entered by the user
class Stack:
    def __init__(self):
        self.value = []

    def push(self, value):
        self.value.append(value)
 #O(1) is the time complexity because the function is only appending once

    def pop(self):
        return self.value.pop()
# we create a class stack
 #O(1) is the time complexity because the function is only pops once


class Queue:
    def __init__(self):
        self.value = []

    def enqueue(self, value):
        self.value.append(value)
    # O(1) is the time complexity because the function is only appending once

    def dequeue(self):
        return self.value.pop(0)
 #O(1) is the time complexity because the function is only pops once

# we create a class queue


def isPalindrome(string):
    stack = Stack()
    queue = Queue()
# we create a stack and queue
    for char in string:
        stack.push(char)
        queue.enqueue(char)
# we place each character in both the queue and stack
    while len(stack.value) > 0 and len(queue.value) > 0:
        char_stack = stack.pop()
        char_queue = queue.dequeue()

        if char_stack != char_queue:
            return False

    return True
# we compare the dequeued and popped char
# using the fifo and lifo rules we get a comparison between the reverse of the word and the word in the right way
# this way we can tell is a word is a palindrome
# O(n) is the time complexity where n being the length of the string


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
# O(n) is the time complexity where n being the number of nodes in the queue

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
# O(1) is the time complexity because we pop once to get the student to interview



def createStudent():
    name = input("\nPlease enter the name of the student: ")
    midterm_grade = input("\nPlease enter their midterm grade: ")
    while not midterm_grade.isnumeric() or not (0 <= int(midterm_grade) <= 100):
        print("Invalid grade. It needs to be between 0 and 100")
        midterm_grade = input("\nPlease enter their midterm grade: ")

    final_grade = input("\nPlease enter their final grade: ")
    while not final_grade.isnumeric() or not (0 <= int(final_grade) <= 100):
        print("Invalid grade. It needs to be between 0 and 100")
        final_grade = input("\nPlease enter their final grade: ")

    good_attitude = input("\nPlease enter a boolean to describe their good attitude: ")
    # Keep looping until a valid boolean is entered
    while not (good_attitude == 'True' or good_attitude == 'False'):
        print("Invalid. Please enter 'True' or 'False'.")
        good_attitude = input("\nPlease enter 'True' or 'False' to describe their good attitude: ")

    student = Student(name, midterm_grade, final_grade, good_attitude)
    return student
# we take user input and create the student object

def evaluate():
    string = input("\nPlease enter the infix expression you want to evaluate: ")
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
# O(n) is the time complexity where n is the length of the infix statement

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adj_matrix = [[0]*vertices for _ in range(vertices)]

    def addVertex(self):
        self.vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.vertices)
        print("\nYou added a new vertex")

# O(n) is the time complexity where n is the number of vertices

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
# O(n) is the time complexity where n is the number of vertices

    def removeEdge(self,v1,v2):
        if ((v1 < 0 or v1 >= self.vertices) and (v2 < 0 or v2 >= self.vertices)):
            print("Invalid vertices", v1, "and", v2, "\n")
        else:
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0
            print("You removed edge between vertices", v1, "and", v2, "\n")
# basically removing the edge but using 2 inputted vertex
# O(1) is the time complexity because we remove 1 edge at a time.

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
# O(1) is the time complexity because we add 1 edge at a time.
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
# O(n^2) is the time complexity because we iterate over each row in the adjacency matrix where n is the number of vertices

def graphMenu():
    print("\n A.Add Vertex"
          "\n B.Add Edge"
          "\n C.Remove Vertex"
          "\n D.Remove Edge"
          "\n E.Display vertices with a degree of X or more"
          "\n F.Return to Main Menu")



def graphMain():
    print("\nWelcome to the Graph Menu: ")
    choice = ""
    graph = Graph(0)
    while choice != "F":
        graphMenu()
        choice = input("\nPlease enter the option you would like to access: ")
        if choice == "A":
            graph.addVertex()
        elif choice == "B":
            v1 = int(input("\nPlease enter the first vertex you would like to add an edge to: "))
            v2 = int(input("\nPlease enter the second vertex you would like to add an edge to: "))
            graph.addEdge(v1,v2)
        elif choice == "C":
            v = int(input("\nPlease enter the vertex you would like to remove: "))
            graph.removeVertex(v)
        elif choice == "D":
            v1 = int(input("\nPlease enter the first vertex you would like to remove the edge of: "))
            v2 = int(input("\nPlease enter the second vertex you would like to remove the edge of: "))
            graph.removeEdge(v1,v2)
        elif choice == "E":
            n = int(input("\nPlease enter the degree of the vertices you would like displayed: "))
            graph.displayGraph(n)
        elif choice != "F":
            print("\nInvalid option.")
    print("\nYou're returning to the Main Menu\n")

def pqMenu():

    print("\nWelcome to the Priority Queue Menu:\n "
          "\n A.Add Student"
          "\n B.Interview Student"
          "\n C.Return to Main Menu")
def pqMain():
    choice = ""
    pq = PriorityQueue()
    while choice != "C":
        pqMenu()
        choice = input("\nPlease enter the option you would like to access: ")
        if choice == "A":
            pq.addStudent()
        elif choice == "B":
            pq.interView()
        elif choice != "C":
            print("\nInvalid option.")
    print("\nYou're returning to the Main Menu\n")




def main():
    choice = 0
    user_name = input("Please enter your name: ")
    print()
    print("Hello", user_name,", welcome to my fourth assignment!")
    print()
    while choice != 6:
        displayMenu()
        print("")
        choice = input("Please enter the exersice you would like to access: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                nodeMain()
            elif choice == 2:
                string = input("Please enter a string to check: ")
                print("\nIt is", isPalindrome(string), "that", string, "is a Palindrome\n")
            elif choice == 3:
                pqMain()
            elif choice == 4:
                print("\n", evaluate())
                print("\nReturning to Main Menu\n")
            elif choice == 5:
                graphMain()
            elif choice != 6:
                print("\nInvalid choice")
    print("\nYou left the project, Goodbye.")




main()













