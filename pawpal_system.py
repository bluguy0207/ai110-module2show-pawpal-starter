from dataclasses import dataclass, field
from datetime import date, datetime, timedelta


@dataclass
class Task:
    title: str
    due_date: str      # YYYY-MM-DD
    time: str          # HH:MM
    frequency: str = "once"   # once, daily, weekly
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def is_due_today(self):
        """Return True if the task is due today."""
        return self.due_date == str(date.today())


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from this pet."""
        if task in self.tasks:
            self.tasks.remove(task)


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet from this owner."""
        if pet in self.pets:
            self.pets.remove(pet)

    def view_tasks(self):
        """Return all pets and their tasks."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks


class PawPalSystem:
    def __init__(self):
        self.owners = []

    def add_owner(self, owner: Owner):
        """Add an owner to the system."""
        self.owners.append(owner)

    def find_pet(self, pet_name: str):
        """Find a pet by name."""
        for owner in self.owners:
            for pet in owner.pets:
                if pet.name.lower() == pet_name.lower():
                    return pet
        return None

    def get_today_tasks(self):
        """Return all tasks due today."""
        today_tasks = []

        for owner in self.owners:
            for pet in owner.pets:
                for task in pet.tasks:
                    if task.is_due_today():
                        today_tasks.append((pet.name, task))

        return today_tasks
    
    def sort_by_time(self, tasks):
        """Return tasks sorted by time."""
        return sorted(tasks, key=lambda task: task.time)

    def filter_by_pet(self, pet_name: str):
        """Return all tasks for a specific pet."""
        pet = self.find_pet(pet_name)

        if pet:
            return pet.tasks

        return []

    def filter_by_status(self, completed: bool):
        """Return tasks matching the completion status."""
        results = []

        for owner in self.owners:
            for pet in owner.pets:
                for task in pet.tasks:
                    if task.completed == completed:
                        results.append((pet.name, task))

        return results

    def detect_conflicts(self):
        """Detect tasks scheduled at the same date and time."""
        warnings = []

        all_tasks = []

        for owner in self.owners:
            for pet in owner.pets:
                for task in pet.tasks:
                    all_tasks.append((pet.name, task))

        for i in range(len(all_tasks)):
            pet1, task1 = all_tasks[i]

            for j in range(i + 1, len(all_tasks)):
                pet2, task2 = all_tasks[j]

                if (
                    task1.due_date == task2.due_date
                    and task1.time == task2.time
                ):
                    warnings.append(
                        f"Conflict: {pet1} and {pet2} both have tasks at {task1.time}"
                    )

        return warnings

    def mark_task_complete(self, pet_name: str, task: Task):
        """Complete a task and create the next recurring task if needed."""
        task.mark_complete()

        pet = self.find_pet(pet_name)

        if pet is None:
            return

        if task.frequency == "daily":
            next_date = (
                datetime.strptime(task.due_date, "%Y-%m-%d")
                + timedelta(days=1)
            ).strftime("%Y-%m-%d")

            pet.add_task(
                Task(task.title, next_date, task.time, "daily")
            )

        elif task.frequency == "weekly":
            next_date = (
                datetime.strptime(task.due_date, "%Y-%m-%d")
                + timedelta(days=7)
            ).strftime("%Y-%m-%d")

            pet.add_task(
                Task(task.title, next_date, task.time, "weekly")
            )