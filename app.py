import streamlit as st
from pawpal_system import Owner, Pet, Task, PawPalSystem

# ----------------------------
# Initialize session state
# ----------------------------
if "system" not in st.session_state:
    st.session_state.system = PawPalSystem()

if "owner" not in st.session_state:
    owner = Owner("Jordan")
    st.session_state.owner = owner
    st.session_state.system.add_owner(owner)

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

st.divider()

# ----------------------------
# Add a Pet
# ----------------------------
st.subheader("Add a Pet")

owner_name = st.text_input("Owner name", value=st.session_state.owner.name)

# Update owner's name if changed
st.session_state.owner.name = owner_name

pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["dog", "cat", "other"])
age = st.number_input("Age", min_value=0, value=1)

if st.button("Add Pet"):
    if pet_name.strip():
        pet = Pet(pet_name, species, age)
        st.session_state.owner.add_pet(pet)
        st.success(f"{pet_name} added!")
    else:
        st.error("Please enter a pet name.")

# Display current pets
if st.session_state.owner.pets:
    st.write("### Current Pets")
    for pet in st.session_state.owner.pets:
        st.write(f"🐾 **{pet.name}** ({pet.species}, {pet.age} years old)")
else:
    st.info("No pets added yet.")

st.divider()

# ----------------------------
# Add a Task
# ----------------------------
st.subheader("Add a Task")

if st.session_state.owner.pets:

    selected_pet = st.selectbox(
        "Assign task to",
        st.session_state.owner.pets,
        format_func=lambda pet: pet.name,
    )

    task_title = st.text_input("Task title")
    due_date = st.date_input("Due date")

    frequency = st.selectbox(
    "Frequency",
    ["once", "daily", "weekly"]
)

    if st.button("Add Task"):
        if task_title.strip():
            task = Task(
            task_title,
            str(due_date),
            "09:00",
            frequency
            )
            selected_pet.add_task(task)
            st.success("Task added!")
        else:
            st.error("Please enter a task title.")

else:
    st.info("Add a pet before adding tasks.")

st.divider()

# ----------------------------
# Current Tasks
# ----------------------------
st.subheader("Current Tasks")

if st.session_state.owner.pets:

    has_tasks = False

    for pet in st.session_state.owner.pets:
        st.markdown(f"### 🐾 {pet.name}")

        if pet.tasks:
            has_tasks = True
            for task in pet.tasks:
                status = "✅" if task.completed else "❌"
                st.write(f"{status} **{task.title}** — {task.due_date}")
        else:
            st.write("No tasks.")

    if not has_tasks:
        st.info("No tasks have been added yet.")

st.divider()

# ----------------------------
# Today's Schedule
# ----------------------------
st.subheader("Today's Schedule")

if st.button("Generate Schedule"):

    today_tasks = st.session_state.system.get_today_tasks()

    if today_tasks:

        # Extract only Task objects for sorting
        tasks = [task for _, task in today_tasks]

        sorted_tasks = st.session_state.system.sort_by_time(tasks)

        st.success("Schedule generated!")

        for task in sorted_tasks:
            st.write(
                f"⏰ {task.time} - {task.title}"
            )

        # Show conflicts
        conflicts = st.session_state.system.detect_conflicts()

        if conflicts:
            st.warning("⚠️ Scheduling Conflicts Found")

            for conflict in conflicts:
                st.warning(conflict)

        else:
            st.success("No scheduling conflicts detected.")

    else:
        st.info("No tasks due today.")