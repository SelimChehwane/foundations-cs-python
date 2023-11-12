
def displayMenu():
    print("-------------------------Hello there! Welcome to my Midterm Project-------------------------")
    print()
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


tabs = []
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

def switchTab():
    import requests
    index = input("Please enter the index of the tab you would like to display: ")
    while index != "":
        if index.isdigit():
            index = int(index)
            if 0 <= index < len(tabs):
                title, url = list(tabs[index].items())[0]
                r = requests.get(url)
                if r.status_code == 200:
                    print(r.text)
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
        print(r.text)
        return r.text

# the program prompt the user to input an index and loops until the input is valid
# if it is valid we use it to access the specific dictionary, transform it into a tuple and unpack it to access the url
# if the input is empty the program displays the last open Tab

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


def diplayTabs():
    for tab in tabs:
        print(list(tab.keys()))

def export():
    import os
    import requests
    path = input("Please enter the path you would like to use to save the open tabs in: ")
    open_tabs = tabs
    for i in range(len(open_tabs)):
        title, url = list(tabs[i].items())[0]
        r = requests.get(url)
        if r.status_code == 200:
            print(r.text)
        with open(path, 'w') as file:
            file.write(r.text)





tabs = [{"c":"https://www.youtube.com/watch?v=BzA7Lyw5zMk", "f":"https://www.youtube.com/watch?v=BzA7Lyw5zMk"}, {"e":"https://www.youtube.com/watch?v=BzA7Lyw5zMk"}]

export()