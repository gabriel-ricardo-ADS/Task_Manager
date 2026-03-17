from manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            index = int(input("Task number to remove: ")) - 1
            manager.remove_task(index)

        elif choice == "4":
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

    
    