tabs = []
# We define the lists of tab outside to be able to update it consistently
def displayMenu():
    print("-------------------------------------------")
    print("Please select an option to start:\n "
          "1.Open Tab\n "
          "2.Close Tab\n "
          "3.Switch Tab\n "
          "4.Display All Tabs\n "
          "5.Open Nested Tab\n "
          "6.Clear All Tabs\n "
          "7.Save Tabs\n "
          "8.Import tabs\n "
          "9.Exit")
# Time complexity is 0(1) because no statement in displayMenu() is dependant on an inputted variable

# We define the lists of tab outside to be able to update it consistently
def openTab():
    title = input("Please enter the title of the tab: ")
    url = input("Please enter the URL of the tab: ")
    while not url.startswith("https://"):
        print("Invalid URL. Please enter a URL starting with 'https://'.")
        url = input("Please enter the URL of the tab: ")
    tab = {title: url}
    tabs.append(tab)
    return tab

# the function prompts the user for a title and a URL
# it then checks for the "https://" at the beginning of the URL using the string function ".startswith()"
# if the URL doesn't start with "https://" it enters a loop that doesn't stop until the URL inputted is valid
# it then creates the tab dictionary and appends it to the list of tabs
# the time complexity is 0(n) because the while loop depends on the user inputting correctly, or they will be
# prompted to re-input as many times as it takes for a valid input

def closeTab():
    index = input("Please enter the index of the tab you would like to close: ")

    while index != "":
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(tabs):
                print("Removing", tabs[index])
                tabs.remove(tabs[index])
                break
            else:
                print("Index out of range.")
        else:
            print("Invalid Index.")
        index = input("Please enter the index of the tab you would like to close: ")

    if index == "":
        print("Removing", tabs[-1])
        tabs.remove(tabs[-1])
# the function takes the inputted index and compares it to the conditions
# when the input is invalid it continually prompts the user for an input until it is valid
# when the input is valid it removes the indexed element.
# if the input is empty it removes the last element from the list
# the time complexity is 0(n) because the program keeps looping until a valid input is entered
def switchTab():
    import requests
    from bs4 import BeautifulSoup
    index = input("Please enter the index of the tab you would like to display: ")
    while index != "":
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(tabs):
                title, url = list(tabs[index].items())[0]
                r = requests.get(url)
                if r.status_code == 200:
                    print(BeautifulSoup(r.text, 'html.parser'))
                else:
                    print("An Error occurred!")
            else:
                print("Index out of range")
        else:
            print("Index Invalid")
        index = input("Please enter the index of the tab you would like to display: ")
    if index == "":
        title, url = list(tabs[-1].items())[0]
        r = requests.get(url)
        print(BeautifulSoup(r.text, 'html.parser'))
        return r.text

# the program prompt the user to input an index and loops until the input is valid
# if it is valid we use it to access the specific dictionary, transform it into a tuple and unpack it to access the url
# if the input is empty the program displays the last open Tab
# the time complexity is 0(n) because the while loop will keep looping until a valid input is entered
def openNestedtabs():
    index = input("Please enter the index of the tab you would like to nest in: ")
    while not index.isdigit() or int(index) >= len(tabs):
        print("Invalid index")
        index = input("Please enter the index of the tab you would like to nest in: ")
    index = int(index)
    if 0 <= index < len(tabs):
        nested_tab = openTab()
        tabs.remove(nested_tab)
        nested_list = tabs[index]
        nested_list.update(nested_tab)
# the program prompts for an index which it validates. if valid we call opentab() to create a tab
# the program then removes the addition of the nested tab to tabs because of how openTab is coded.
# then it updates the tabs list at the entered index with the openTab/nested tab
# the time complexity is 0(n) because it will keep looping until the user's input is valid

def diplayTabs():
    for tab in tabs:
        print(list(tab.keys()))





def export():
    import os
    from bs4 import BeautifulSoup
    import requests
    import json
    file_name = input("Please provide the name of the file you would like to export: ")
    path = input("Please enter the path you would like to use to save the open tabs in: ")
    path = os.path.join(os.path.dirname(__file__), file_name)
    with open(path, 'a') as file:
        for i in range(len(tabs)):
            title, url = list(tabs[i].items())[0]
            r = requests.get(url)
            if r.status_code == 200:
                content = BeautifulSoup(r.text, 'html.parser')
                json_data ={'titles': title, 'url':url,'content': str(content)}
                file.write(json.dumps(json_data))

def import_tabs():
    path = input("Please enter the path of the file you would like to open: ")
    with open(path, 'r') as file:
        imported_tabs = file.read()
        print(imported_tabs)
        tabs.append(imported_tabs)
        print(tabs)
# you import the string representation of a dictionary you'll have to fix it

def clearTabs():
    global tabs
    tabs = []
    return tabs

def main():
    print("-------------------------Hello there! Welcome to my Midterm Project-------------------------")
    print()
    choice = 0
    while choice != 9:
        displayMenu()
        choice = eval(input("Please enter the exersice you would like to access: "))
        if choice == 1:
            openTab()
        elif choice == 2:
            closeTab()
        elif choice == 3:
            switchTab()
        elif choice == 4:
            diplayTabs()
        elif choice == 5:
            openNestedtabs()
        elif choice == 6:
            clearTabs()
        elif choice == 7:
            export()
        elif choice == 8:
            import_tabs()
        elif choice != 9:
            print("Invalid choice")
    print("You left the project, Goodbye.")


main()