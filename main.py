''' 
1. To-Do List CLI App:

Create a command-line to-do list with options to add, remove, and view tasks.
Learn file I/O to save tasks in a text file or CSV.
'''

import csv  # Import the CSV module to handle saving/loading tasks

tasks = []  # Using a list to store tasks. (A dictionary could be used for numbered entries, but a list works for simplicity.)

options = {'a': 'Add Task', 'b':'Remove Task','c':'View Tasks','d':'Exit'}  # Menu options for user interaction

def option_menu():
    """Displays the main menu, handles user choices, and manages the app flow."""
    print(" Entering TaskMaster 5000")  # Inform the user the app is starting
    load_tasks(tasks)  # Load tasks from 'tasks.csv' to restore previously saved tasks

    while True:  # Infinite loop to keep the menu running until the user chooses to exit
        print(options)  # Display the menu options
        user_choice = input("What do you want to do? ")  # Prompt the user to select an option
        function = user_choice  # Store user input (duplicated variable but clear for learning)

        if function == 'a':  # Add Task option
            task = input("1. Adding Task - what task would you like to add? ")  # Prompt for task input
            add_task(task)  # Call the add_task function to add it to the list
            
        elif function == 'b':  # Remove Task option
            print(tasks)  # Display the current list of tasks
            task = input("2. Removing Task - What task would you like to remove? ")  # Prompt user for task to remove
            remove_task(task)  # Call the remove_task function

        elif function == 'c':  # View Tasks option
            view_task(tasks)  # Call view_task to display tasks
            
        elif function == 'd':  # Exit option
            print("👋 Exiting TaskMaster 5000")  # Notify user of exit
            break  # Exit the while loop to end the program


def add_task(task):
    """Adds a new task to the task list."""
    tasks.append(task)  # Append the provided task to the end of the tasks list
    print("✅ Task added.")  # Confirm task addition to the user


def remove_task(task):
    """Removes a task from the list if it exists."""
    if task in tasks:  # Check if the specified task exists in the tasks list
        tasks.remove(task)  # Remove the matching task
        print(f"🗑️ Removed task: '{task}'")  # Notify the user of successful removal
    else:
        print("⚠️ Task not found. Make sure the task name matches exactly.")  # Warn if task doesn't exist


def view_task(tasks):
    """Displays all tasks and prompts to save them to a CSV file."""
    print(tasks)  # Show the current list of tasks
    save_choice = input("Would you like to save your tasks to CSV? Y/N ")  # Prompt the user to save tasks

    if save_choice.upper() == "Y":  # Convert input to uppercase to handle lowercase input
        save_tasks(tasks)  # Call the save_tasks function
    elif save_choice.upper() == "N":
        print("❌ Tasks not saved.")  # Confirm that tasks won't be saved
    else:
        print("⚠️ Invalid input. Please enter 'Y' or 'N'.")  # Handle invalid input


def save_tasks(task):
    """Saves the current tasks to 'tasks.csv'."""
    # Using 'with' ensures the file is automatically closed after writing
    with open("tasks.csv", "w", newline='') as Document:  
        writer = csv.writer(Document)  # Create a CSV writer object
        for task in tasks:  # Loop through each task in the list
            writer.writerow([task])  # Write the task to the CSV file as a single row
    print("💾 Tasks saved successfully.")  # Confirm that the tasks have been saved


def load_tasks(tasks):
    """Loads tasks from 'tasks.csv' into the tasks list."""
    try:
        with open("tasks.csv", "r", newline='') as previous_tasks:  # Safely open the CSV file for reading
            reader = csv.reader(previous_tasks)  # Create a CSV reader to read the file
            for row in reader:  # Loop through each row in the CSV
                if row:  # Check that the row is not empty
                    tasks.append(row[0])  # Add the task (first column of the row) to the tasks list
        print("✅ Tasks loaded successfully.")  # Notify user of successful load
    except FileNotFoundError:
        print("⚠️ No saved tasks found. Starting with an empty task list.")  # Handle case when no CSV exists


def main():
    """Main entry point for the program."""
    option_menu()  # Run the option menu to handle user interactions


main()  # Start the application
