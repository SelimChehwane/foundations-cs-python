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



