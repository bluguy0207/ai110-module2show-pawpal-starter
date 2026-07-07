from datetime import date
from pawpal_system import Task, Pet, Owner, PawPalSystem

system = PawPalSystem()

owner = Owner("Troy")

dog = Pet("Buddy", "Dog", 3)
cat = Pet("Luna", "Cat", 2)

today = str(date.today())

dog.add_task(Task("Morning Walk", today))
dog.add_task(Task("Feed Breakfast", today))
cat.add_task(Task("Clean Litter Box", today))

owner.add_pet(dog)
owner.add_pet(cat)

system.add_owner(owner)

print("Today's Schedule")
print("-" * 30)

for pet_name, task in system.get_today_tasks():
    status = "✓" if task.completed else "✗"
    print(f"{pet_name}: {task.title} ({task.due_date}) [{status}]")