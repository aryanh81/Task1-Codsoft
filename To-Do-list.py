def menu():
    print("Menu: ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark as Done")
    print("4. Exit")

def addTask(tasks):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully")

def viewTask(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, start = 1):
        print(i,'.', task)

def markDone(tasks):
    if  len(tasks) == 0:
        print("No tasks")
        return
    viewTask(tasks)
    index = int(input("Enter task number to marks as done: "))-1

    if 0<=index<len(tasks):
        removed_task = tasks.pop(index)
        print(removed_task, ' marked as DONE')
    else:
        print('No task found')

def main():
    tasks = []

    while True:

        print("\n")
        menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            addTask(tasks)
        elif choice == '2':
            viewTask(tasks)
        elif choice == '3':
            markDone(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again")

main()
