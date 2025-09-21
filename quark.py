# CLI task tracking program created by Natsil

import json
import datetime
import os

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)

def load_tasks(filename="tasks.json"):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        return []
    with open(filename, "r") as f:
        data = json.load(f)
        return [Task.from_dict(d) for d in data]

class Task():
    id_counter = 0

    def __init__(self, description, status, createdAt, updatedAt, id=None):
        if id is None:
            Task.id_counter += 1
            self.id = Task.id_counter
        else:
            self.id = id
            Task.id_counter = max(Task.id_counter, id)
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data["description"],
            status=data["status"],
            createdAt=data["createdAt"],
            updatedAt=data["updatedAt"],
            id=data["id"]
        )

task_list = load_tasks()

while True:
    print()
    print ("""
             ,o888888o.     8 8888      88        .8.          8 888888888o.   8 8888     ,88' 
          . 8888     `88.   8 8888      88       .888.         8 8888    `88.  8 8888    ,88'  
         ,8 8888       `8b  8 8888      88      :88888.        8 8888     `88  8 8888   ,88'   
         88 8888        `8b 8 8888      88     . `88888.       8 8888     ,88  8 8888  ,88'    
         88 8888         88 8 8888      88    .8. `88888.      8 8888.   ,88'  8 8888 ,88'     
         88 8888     `8. 88 8 8888      88   .8`8. `88888.     8 888888888P'   8 8888 88'      
         88 8888      `8,8P 8 8888      88  .8' `8. `88888.    8 8888`8b       8 888888<       
         `8 8888       ;8P  ` 8888     ,8P .8'   `8. `88888.   8 8888 `8b.     8 8888 `Y8.     
          ` 8888     ,88'8.   8888   ,d8P .888888888. `88888.  8 8888   `8b.   8 8888   `Y8.   
             `8888888P'  `8.   `Y88888P' .8'       `8. `88888. 8 8888     `88. 8 8888     `Y8. 
                            
                        ~~~   Task Tracker Supreme | Developed by Natsil ~~~
             """)
    print()
    print("~~~ Your Current Tasks ~~~")
    for task in task_list:
                print()
                print(f"{task.id} | Description: {task.description} | Status: {task.status}")
    print()
    print("~~~ User Options ~~~")
    print()
    print("1: Add, edit, or delete a task")
    print("2: Update task status")
    print("3: List your tasks")
    print("4: Quit program")
    print()

    command = input("What would you like to do? ")

    if command == "1":
        print("1: Add a new task")
        print("2: Edit a task")
        print("3: Delete a task")
        command_2 = input("Pick an option: ")

        if command_2 == "1":
            while True:
                task_description = input("Enter a task to add to the list (Enter 'q' to finish entry!): ")
                created_time = datetime.datetime.now()
                created_time_formatted = created_time.strftime("%d-%m-%y %H:%M:%S")
                if task_description.lower() == "q":
                    break
                else:
                    task = Task(task_description, "Incomplete", created_time_formatted, created_time_formatted)
                    task_list.append(task)

        elif command_2 == "2":
            edit = input("Which task do you want to edit? (Enter task number): ")
            for task in task_list:
                if int(edit) == task.id:
                    task.description = input("Enter edited task description: ")

        elif command_2 == "3":
            delete = input("Which task do you want to delete? (Enter task number): ")
            for task in task_list:
                if int(delete) == task.id:
                    delete_id = task.id - 1
                    del task_list[delete_id]

    elif command == "2":
        status = input("Which task's status do you want to update? (Enter task number): ")
        for task in task_list:
            if int(status) == task.id:
                task_status = input("What is the status of the task? ")
                task.status = task_status

    elif command == "3":
        print()
        print("~~~ Your Current Tasks ~~~")
        if not task_list:
            print("No tasks yet!")
        else:
            for task in task_list:
                print()
                print(f"{task.id} | Description: {task.description} | Status: {task.status} | Created on: {task.createdAt} | Last updated: {task.updatedAt}")
        print()
        print("Press Enter to return to main menu...")
        input()

    elif command == "4":
        print("Goodbye!")
        save_tasks(task_list)
        break

    else:
        print("Incorrect input, please try again!")