import json


tasks = []



def add_task(description):
    task = {"description": description, "done": False}
    tasks.append(task)
    print("Task added.")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed task: {removed['description']}")
    else:
        print("Invalid task number.")

def mark_task_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f"Task '{tasks[index]['description']}' marked as done.")
    else:
        print("Invalid task number.")

def view_tasks():
    if not tasks:
        print("No tasks added yet.")
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['description']} - {status}")

# File Operations

def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)
    print("Tasks saved.")

def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks found.")

# Main Program Loop

def main():
    load_tasks()  # Load saved tasks when the app starts

    while True:
        print("\nChoose an option: add, remove, done, view, save, quit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "add":
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == "remove":
            index = int(input("Enter task number to remove: "))
            remove_task(index)
        elif choice == "done":
            index = int(input("Enter task number to mark as done: "))
            mark_task_done(index)
        elif choice == "view":
            view_tasks()
        elif choice == "save":
            save_tasks()
        elif choice == "quit":
            save_tasks()  # Save tasks before quitting
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main loop if the script is executed directly
if __name__ == "__main__":
    main()
