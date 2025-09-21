# CLI task tracking program created by Natsil


class Task():
    id_counter = 0

    def __init__(self, description, status, createdAt, updatedAt):
        Task.id_counter += 1
        self.id = Task.id_counter
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

task_list = []

while True:
    print("--- Quark 3000: Task Tracker Supreme ---")
    print()
    print("1: Add, edit, or delete a task")
    print("2: Update task status")
    print("3: List your tasks")
    print("4: Quit program")

    command = input("What would you like to do? ")

    if command == "1":
        print("1: Add a new task")
        print("2: Edit a task")
        print("3: Delete a task")
        command_2 = input("Pick an option: ")
        if command_2 == "1":
            while True:
                task_description = input("Enter a task to add to the list (Enter 'q' to finish entry!): ")
                if task_description.lower() == "q":
                    break
                else:
                    task = Task(task_description, "ongoing", "test", "test")
                    task_list.append(task)
        elif command_2 == "2":
            edit = input("Which task do you want to edit? (Enter task number): ")
            for task in task_list:
                if int(edit) == task.id:
                    task.description = input("Enter edited task description: ")
                else:
                    break

    elif command == "2":
        print("ok")
    elif command == "3":
        if not task_list:
            print("No tasks yet!")
        else:
            for task in task_list:
                    print(f"{task.id} - {task.description}")

    elif command == "4":
        print("Goodbye!")
        break

    else:
        print("Incorrect input, please try again!")