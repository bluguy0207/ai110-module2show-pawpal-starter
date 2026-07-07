# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

I designed four classes: Owner, Pet, Task, and PawPalSystem. The Owner class manages a user's pets. Each Pet stores information about an individual animal and its care tasks. The Task class represents activities like feeding, walking, or vet appointments and tracks whether they are completed. The PawPalSystem class manages all owners and provides methods to search for pets and retrieve daily tasks.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

During implementation, I expanded the Task class by adding time and frequency attributes. Originally, tasks only tracked basic information and completion status, but adding time allowed the system to sort tasks and detect scheduling conflicts. Adding frequency allowed recurring tasks, such as daily feeding, to automatically create future tasks after completion.


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers task time, completion status, pet assignment, and recurring schedules. Time was the most important constraint because pet owners need tasks organized in a realistic daily order. Completion status was also important because completed tasks should not be treated the same as unfinished tasks.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

My scheduler only checks for tasks with the exact same date and time. It does not detect overlapping task durations, which keeps the algorithm simple but makes conflict detection less accurate.


---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI tools to help design my classes, debug errors, improve my implementation, and understand Python concepts. Helpful prompts included asking how classes should interact, how to use `sorted()` with lambda functions, how to implement recurring tasks with `timedelta`, and how to organize Streamlit state using `st.session_state`.


**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One example was when implementing scheduling features. I modified some AI suggestions instead of copying them directly because I wanted to keep my class structure simple. I verified changes by running my CLI demo and pytest tests to make sure the functionality worked correctly.


---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested that tasks could be marked complete and that adding a task increased a pet's task count. These tests verified that the core Task and Pet behaviors worked correctly. I also manually tested sorting, filtering, recurring tasks, and conflict detection through my main.py demo.


**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am confident that my scheduler works for the scenarios tested. If I had more time, I would test more edge cases such as multiple owners with pets having the same name, tasks with overlapping durations, and invalid time formats.


---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with how the project evolved from simple class structures into a working scheduling system. The addition of sorting, filtering, recurring tasks, and conflict detection made the system more realistic and useful.


**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would improve the scheduling algorithm by considering task duration, priority levels, and owner availability. I would also improve the Streamlit interface by making the UI fully connected to the backend scheduling logic.


**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I learned that AI tools are most useful when used as collaborators rather than replacements for problem solving. The human developer still needs to make design decisions, test suggestions, and ensure the final system matches the project's goals.