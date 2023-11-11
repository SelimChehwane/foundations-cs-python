                                        ###############
                                        # Assignment 3#
                                        ###############
def displayYMenu():
    print("Menu:\n" + "\t1.Add Matrices\n"+"\t2.Check Rotation\n"+"\t3.Invert Dictionary\n"
          +"\t4.Covert Matrix to Dictionary \n"+"\t5.Check Palindrome\n"
          +"\t6.Search for an Element & Merge Sort \n"+"\t7.Exit\n")

def addMatrices():
    matrix1 = []
    matrix2 = []
    matrix3 = []
# define the matrecies
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
# user input of the numbers of rows and columns
    for i in range(rows):
        row = []
# create sub-list row
        for j in range(columns):
            value = int(input("Enter the elements of column {}".format((j+1)) + " at row {}".format(i+1)
                              + " of the first Matrix: "))
# user input of elements in matrix1
            row.append(value)
# append the input element to sub-list row
        matrix1.append(row)
# append sub-list row to matrix1
    for i in range(rows):
        row = []
# create sub-list row
        for j in range(columns):
            value = int(input("Enter the elements of row {}".format((j + 1)) + " at row {}".format(i+1)
                            + " of the Second Matrix: "))
# user input of elements in matrix2
            row.append(value)
# append the input element to sub-list row
        matrix2.append(row)
# append sub-list row to matrix2
    for i in range(len(matrix1)):
        row = []
# create sub-list row
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
# append the sum of indexed elements in matrix1 and matrix2 to sub-list row
        matrix3.append(row)
# append sub-list row to matrix3

    print(matrix1, "+", matrix2, "=", matrix3)
# print the result
# the time complexity is N^2 because we have 3 nested loops that are dependent on user input



def checKRotation():
    matrix1 = []
    matrix2 = []
    rows = int(input("Enter number of rows of matrix1: "))
    columns = int(input("Enter number of columns of matrix1: "))
    for i in range(rows):
        row = []
# create sub-list row
        for j in range(columns):
            value = int(input("Enter the elements of column {}".format((j + 1)) + " at row {}".format(i + 1)
                              + " of the first Matrix: "))
# user input of elements in matrix1
            row.append(value)
# append the input element to sub-list row
        matrix1.append(row)
# append the sub-list row to matrix1

    rows = int(input("Enter number of rows of matrix2: "))
    columns = int(input("Enter number of columns of matrix2: "))
    for i in range(rows):
        row = []
# create sub-list row
        for j in range(columns):
            value = int(input("Enter the elements of column {}".format((j + 1)) + " at row {}".format(i + 1)
                              + " of the second Matrix: "))
# user input of elements in matrix2
            row.append(value)
# append the input element to sub-list row
        matrix2.append(row)
# append the sub-list row to matrix2
    if len(matrix1) != len(matrix2[0]) or len(matrix1[0]) != len(matrix2):
        result = False
# if the columns of X are not rows in Y and the rows in Y are nt columns in X it is false
    for i in range(len(matrix1)):
# we take the lenghth of matrix1 (columns) and iterate over it
        for j in range(len(matrix2[0])):
# we iterate over the indexed matrix2 (rows)
            if matrix1[i][j] != matrix2[j][i]:
                result = False
            else:
                result = True
# we compare matrix1 and matrix2 at [i][j] to determine if it is a rotation
    print("It is", result, "that", matrix1, "is a rotation of", matrix2)
# the time complexity is 0(N^2) because we have nested loops that are dependent on user input

def dicTReverse():
    dict1 = {}
    # we create a dictionary dict1
    rows = eval(input("Please enter the number of rows you would like to add : "))
    # user input the number of rows they want in dict1
    for i in range(rows):
        # we iterate over rows
        values = input("Please enter a value : ")
        key = i+1
        dict1.update({key: values})
    #     with each entered value, the key is auto-generated based on the index of rows at that value + 1
    print(dict1)

    inverted_dict = {}
    # create an inverted dictdicT

    for key, value in dict1.items():
        # we iterate over the key, value pairs using .items()
        if value in inverted_dict:
            # if the value is duplicated in the inverted list
            inverted_dict[value].append(key)
        #     we append the key to the value list
        else:
            inverted_dict[value] = [key]
        # we pass the values in dict1 as keys in the inverted dict
        # we pass the keys in dict1 as values in the inverted dict

    print(inverted_dict)
# the time complexity is 0(N^2) because we have nested loops that are dependent on user input

def lisTDict():
    rows = eval(input("Please enter the number of profiles you would like to add : "))
    # user input the amount of profiles they want to create
    data = ["First Name", "Last Name", "ID", "Job Title", "Company"]
    # organize data to be entered in  list
    profiles = []
    dict2 = {}

    for i in range(rows):
        # we iterate over the rows (number of profiles)
        profile = []
        # define empty profile list
        for j in data:
            # iterate over the data list.
            profile_data = input("Please enter the {} of profile {}".format(j,i+1) + ": ")
            # input the data
            profile .append(profile_data)
            # append the data to the empty profile list
        profiles.append(profile)
        # append the profile to the list of profiles

    for i in range(len(profiles)):
        # iterate over the range of the list of profiles' range
        id = profiles[i][2]
        # save the ID number in a variable
        del profiles[i][2]
        # delete the id data
        dict2[id] = profiles[i]
    #     create the dict
    # the time complexity is 0(N) because the output is dependant on user input


    print(dict2)

def reverseString(s):
    if len(s) != 1:
        s1 = reverseString(s[1:])+s[0]
        # we slice the string at each recursion and append the first character of the slice string
        return s1
    else:
        return s
#     base case to stop recursion
# the time complexity is 0(N) because the output is dependent on user input

def isPalindrome():
    s = input("Enter a word to determine if it's a palindrome: ")
    if s == reverseString(s):
        # we compare the string to its reversed version
        return True
    else:
        return False
    # the time complexity is 0(N) because the output is dependent on user input



def mergeSort(lst):
    if len(lst) > 1:
        lst1 = lst[:len(lst)//2]
        lst2 = lst[len(lst)//2:]
        # we split the list into 2 list
        mergeSort(lst1)
        mergeSort(lst2)
        # we call the function to split the lists
        # in half recursively to get 1 element in per list
        i = 0
        j = 0
        k = 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                # if the first element of the first list
                # is smaller than that of the second list
                lst[k] = lst1[i]
                # we place it at index 0 in the bigger list
                i += 1
            # we update the value i
            else:
                lst[k] = lst2[j]
                # else we place the first element
                # of the second list at index 0 in the bigger list
                j += 1
                # we update the value j
            k += 1
            # we update the value k

        while i < len(lst1):
            lst[k] = lst1[i]
            i += 1
            k += 1
        # merge lst1 to lst

        while j < len(lst2):
            lst[k] = lst2[j]
            j += 1
            k += 1
        # merge lst2 to lst
# the time complexity is 0(nlog(n)) because it splits the list in half depending on user input

def searchList():
    lst = []
    lst_len = int(input("Please enter the length of the list: "))
    for i in range(lst_len):
        lst.append(input("Enter element {} ".format(i+1) + "of the list"))

    x = input("Enter element you want to find in the list: ")
    mergeSort(lst)

    for i in range(len(lst)):
        if lst[i] == x:
            print(x, "is at index {}".format(i))
    #         iterate over lst to find x and print its index
    if x not in lst:
        print(x, "was not found in the list")
    # if x not found in the list
     # the time complexity is 0(N^2) because the nested loops are dependant on user input


def assignment3():
    name_user = input("Please enter your name: ")
    print("Hello ", name_user, ", welcome to my third assignment!")

    choice_user = 0
    while choice_user != 7:
        displayYMenu()
        choice_user = eval(input("Please enter the exersice you would like to access: "))
        if choice_user == 1:
            addMatrices()
        elif choice_user == 2:
            checKRotation()
        elif choice_user == 3:
            dicTReverse()
        elif choice_user == 4:
            lisTDict()
        elif choice_user == 5:
            isPalindrome()
        elif choice_user == 6:
            searchList()
        elif choice_user != 7:
            print("Invalid choice")
    print("You left assignment3, Goodbye.")


assignment3()
