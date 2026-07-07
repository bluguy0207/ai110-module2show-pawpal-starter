from pawpal_system import Task, Pet


def test_mark_complete():
    task = Task("Walk", "2026-07-06")
    task.mark_complete()
    assert task.completed is True


def test_add_task():
    pet = Pet("Buddy", "Dog", 3)
    pet.add_task(Task("Feed", "2026-07-06"))
    assert len(pet.tasks) == 1