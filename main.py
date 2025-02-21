'''1. To-Do List CLI App:

Create a command-line to-do list with options to add, remove, and view tasks.
Learn file I/O to save tasks in a text file or JSON.'''

'''Learnings, I have learnt while true, general syntax errors and correct usage of .append and .remove, etc, 
I used a cheat sheet to see formatting and used chatgpt when stuck on the while true and a general overview of errors'''


tasks = []
options = {'a': 'Add Task', 'b':'Remove Task','c':'View Tasks','d':'Exit'}


def option_menu():
    print ("Entering TaskMaster 5000")
    while True:
        print (options)
        user_choice = input("What do you want to do? ")
        function = (user_choice)
        
        if  function == ('a'):
            task = input("1. Adding Task - what task would you like to add? ")
            add_task(task)
            
        elif(function) == ('b'):
            print(tasks) 
            task = input("2. Removing Task - What task would you like to remove? ")
            remove_task(task)
        
        elif(function) == ('c'):
            view(tasks)
            
        elif(function) == ('d'):
            print ("Exiting Taskmaster 5000")
            break      
    
def add_task(task):
    tasks.append(task)
    print("Task Added")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)    

def view(tasks):
    print (tasks)   
            

def main():
    option_menu()
    
main()
