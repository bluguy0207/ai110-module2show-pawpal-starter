# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```text
============================= test session starts =============================
collected 2 items

tests/test_pawpal.py ..                                                   [100%]

============================== 2 passed in 0.03s =============================
```
# Paste your pytest output here
```
PS C:\Users\troyj\ai110-module2show-pawpal-starter> C:\Users\troyj\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pytest
======================================================================= test session starts =======================================================================
platform win32 -- Python 3.14.3, pytest-9.1.0, pluggy-1.6.0
rootdir: C:\Users\troyj\ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 2 items                                                                                                                                                  

tests\test_pawpal.py ..                                                                                                                                      [100%]

======================================================================== 2 passed in 0.03s ========================================================git add .=======
>> C:\Users\troyj\ai110-module2show-pawpal-starter> 
## 📐 Smarter Scheduling

### Sorting
Tasks are sorted by time using `PawPalSystem.sort_by_time()`.

### Filtering
Tasks can be filtered by pet name using `filter_by_pet()` and by completion status using `filter_by_status()`.

### Conflict Detection
`detect_conflicts()` checks for tasks that occur on the same date and time and returns warning messages.

### Recurring Tasks
`mark_task_complete()` automatically creates the next occurrence of daily and weekly tasks using `timedelta`.

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `sort_by_time()` | Sorts tasks chronologically using task time |
| Filtering | `filter_by_pet()`, `filter_by_status()` | Allows viewing tasks by pet or completion state |
| Conflict handling | `detect_conflicts()` | Detects tasks scheduled at the same date and time |
| Recurring tasks | `mark_task_complete()` | Creates the next daily or weekly task after completion |

## Confidence Level: 5

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Launch the Streamlit application and enter owner and pet information.
2. Add pets to the PawPal+ system.
3. Create tasks with due dates and times.
4. Generate and view the pet care schedule.
5. Review sorted tasks, recurring tasks, and conflict warnings.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
