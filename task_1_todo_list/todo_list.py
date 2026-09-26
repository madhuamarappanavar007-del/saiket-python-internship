class TodoList:
    """A simple class for managing to-do tasks."""

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        """Add a new task if its title is not empty."""
        title = title.strip()

        if not title:
            print("Task cannot be empty.")
            return

        task = {
            "title": title,
            "completed": False,
        }
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        """Display all tasks and their current status."""
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n--- To-Do List ---")
        for number, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{number}. {task['title']} [{status}]")

    def mark_task_completed(self, task_number):
        """Mark a task as completed using its displayed number."""
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return

        self.tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")


def display_menu():
    """Display the available menu choices."""
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Exit")


def main():
    todo_list = TodoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            title = input("Enter the task: ")
            todo_list.add_task(title)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            if not todo_list.tasks:
                print("No tasks available.")
                continue

            todo_list.view_tasks()

            try:
                task_number = int(input("Enter the task number: "))
                todo_list.mark_task_completed(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()
