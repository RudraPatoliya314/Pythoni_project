todo_list = []

while True:
    task = input("Enter a task (or 'done' to stop): ")
    if task.lower() == 'done':
        break
    todo_list.append(task)

print("\nYour To-Do List:")
for i, t in enumerate(todo_list, 1):
    print(f"{i}. {t}")
