[README.md](https://github.com/user-attachments/files/26633963/README.md)
# To-Do List App 📝

A beginner Python project — manage your daily tasks directly from the terminal.

## Features

- View all tasks with completion status
- Add new tasks
- Mark tasks as complete ✅
- Delete tasks
- Input validation — handles empty names and invalid numbers gracefully
- Clean looping menu interface

## How to Run

Make sure you have Python installed, then run:

```
python todo.py
```

## Example

```
==============================
      To-Do List App 📝       
==============================

What would you like to do?
  1 — View all tasks
  2 — Add a task
  3 — Complete a task ✅
  4 — Delete a task
  5 — Quit
------------------------------
Choose an option (1/2/3/4/5): 2
Enter task name: Learn Python
Task 'Learn Python' added!

Choose an option (1/2/3/4/5): 1

--- Your Tasks ---
  1. ⬜ Learn Python
------------------
```

## What I Learned

- Working with **lists** to store multiple items
- Using **dictionaries** to store structured data (`name` and `done` status)
- Using **enumerate()** to loop with index numbers
- Separating code into clean **functions**
- Handling **user input errors** with try/except
