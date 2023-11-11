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
    tab = {title: [url]}
    tabs.append(tab)


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
