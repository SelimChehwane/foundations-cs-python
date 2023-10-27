                                        ###############
                                        # Assignment 3#
                                        ###############
def displayYMenu():
    print("Menu:\n" + "\t1.Add Matrices\n"+"\t2.Check Rotation\n"+"\t3.Invert Dictionary\n"
          +"\t 4.Covert Matrix to Dictionary \n"+"\t5.Check Palindrome\n"
          +"\t 6.Search for an Element & Merge Sort \n"+"\t7.Exit\n")

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

    print(dict2)



