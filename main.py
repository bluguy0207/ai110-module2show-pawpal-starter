from datetime import date
from pawpal_system import Task, Pet, Owner, PawPalSystem

system = PawPalSystem()

owner = Owner("Troy")

dog = Pet("Buddy", "Dog", 3)
cat = Pet("Luna", "Cat", 2)

today = str(date.today())

dog.add_task(Task("Morning Walk", today, "09:00"))
dog.add_task(Task("Feed Breakfast", today, "08:30"))
cat.add_task(Task("Clean Litter Box", today, "09:00"))
cat.add_task(Task("Brush Fur", today, "15:00"))

owner.add_pet(dog)
owner.add_pet(cat)

system.add_owner(owner)

print("Today's Schedule")
print("-" * 30)

for pet_name, task in system.get_today_tasks():
    status = "✓" if task.completed else "✗"
    print(f"{pet_name}: {task.title} ({task.due_date}) [{status}]")


print("\nSorted Tasks")
print("-" * 30)

all_tasks = []

for pet in owner.pets:
    all_tasks.extend(pet.tasks)

for task in system.sort_by_time(all_tasks):
    print(task.time, task.title)

print("\nBuddy's Tasks")
print("-" * 30)

for task in system.filter_by_pet("Buddy"):
    print(task.title)

dog.tasks[0].mark_complete()

print("\nCompleted Tasks")
print("-" * 30)

for pet_name, task in system.filter_by_status(True):
    print(pet_name, task.title)

print("\nRecurring Tasks")
print("-" * 30)

daily = Task("Feed Dog", today, "08:00", "daily")
dog.add_task(daily)

system.mark_task_complete("Buddy", daily)

for task in dog.tasks:
    print(task.title, task.due_date, task.completed)
    
print("\nConflicts")
print("-" * 30)

warnings = system.detect_conflicts()

if warnings:
    for warning in warnings:
        print(warning)
else:
    print("No conflicts found.")