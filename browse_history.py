# BrowserHistory.py

from queue import LifoQueue

# Initialize LifoQueue objects
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

# Prompt user for number of URLs visited
NoOfVisits = int(input("Enter the number of URLs you have visited: "))

# Store URL history
for _ in range(NoOfVisits):
    url = input("Enter the URL you visited: ")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url

# Print current page URL
print(f"Current page: {current_page}")

# Backward navigation
while input("Do you want to go back? (yes/no): ").lower() == "yes":
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to: {current_page}")
    else:
        print("No previous pages available to navigate back to.")

# Forward navigation
while input("Do you want to go forward? (yes/no): ").lower() == "yes":
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to: {current_page}")
    else:
        print("No forward pages available to navigate forward to.")
