# CLI task tracking program created by Natsil

class Task():
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

print("--- Quark 3000: Task Tracker Supreme ---")
print()
print("1: Add, update, or delete a task")
print("2: Update task status")
print("3: List your tasks")

command = input("What would you like to do? ")

if command == "1":
    print("ok")
elif command == "2":
    print("ok")
elif command == "3":
    print("ok")
else:
    print("Incorrect input, please try again!")