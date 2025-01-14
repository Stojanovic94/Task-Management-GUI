# Task Management Application with GUI

This project demonstrates the development of a **Task Management Application** with a Graphical User Interface (GUI). The application allows users to efficiently manage their tasks by adding, updating, deleting, and filtering tasks based on their status.

---

## Features

1. **Add Tasks**  
   - Users can add new tasks with details such as title, description, due date, and status.
   
2. **Update Tasks**  
   - Existing tasks can be updated to modify any details or change their status.

3. **Delete Tasks**  
   - Unwanted tasks can be removed from the task list.

4. **Filter Tasks**  
   - Tasks can be filtered based on their status, such as "Pending," "In Progress," or "Completed."

5. **User-Friendly GUI**  
   - A clean and intuitive interface for task management, designed to enhance productivity.

---

## Technologies Used

- **Programming Language**: Python  
- **GUI Framework**: Tkinter or PyQt (depending on the implementation)  
- **Database**: SQLite (for persistent storage of tasks)  

---

## Application Architecture

### Task Model
Represents a single task with the following attributes:
- `title`: The title of the task.
- `description`: A brief description of the task.
- `due_date`: The deadline for completing the task.
- `status`: The current status of the task (e.g., Pending, In Progress, Completed).

### Task Controller
Handles the business logic, such as:
- Adding tasks to the database.
- Updating task details.
- Deleting tasks from the database.
- Filtering tasks based on their status.

### Task View (GUI)
Provides the graphical interface for users to interact with the application:
- Displays the list of tasks in a table format.
- Includes buttons and input fields for task operations.
- Provides dropdown menus or checkboxes for filtering tasks.

---
