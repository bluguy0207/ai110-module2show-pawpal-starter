from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    due_date: str
    completed: bool = False

    def mark_complete(self):
        pass

    def is_due_today(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def remove_task(self, task: Task):
        pass


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet: Pet):
        pass

    def view_tasks(self):
        pass


class PawPalSystem:
    def __init__(self):
        self.owners = []

    def add_owner(self, owner: Owner):
        pass

    def find_pet(self, pet_name: str):
        pass

    def get_today_tasks(self):
        pass