from dataclasses import dataclass, field
from datetime import date


@dataclass
class Task:
    title: str
    due_date: str  # Format: YYYY-MM-DD
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