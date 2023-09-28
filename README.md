# Django Rest Framework TODO App

This is a simple Django Rest Framework (DRF) application for managing tasks in a TODO list.

## Features
- Create, Read, Update, and Delete tasks.
- Filter tasks by title and completion status.
- Bulk delete completed tasks.

## Installation & Setup

1. Clone the repository:
 ```bash
 git clone https://github.com/GiorgiTarsaidze/todo-server
 ```
2. Migrate the database:
 ```bash
 python manage.py migrate
 python mannage.py makemigrations
 ```
3.Start the development server:
 ```bash
 python manage.py runserver
 ```

## API Endpoints
- List Tasks: `GET /api/tasks/` - Retrieve a list of all tasks.
- Create Task: `POST /api/tasks/` - Create a new task.
- Retrieve Task: `GET /api/tasks/{task_id}/` - Retrieve details of a specific task.
- Update Task: `PUT /api/tasks/{task_id}/` - Update an existing task.
- Delete Task: `DELETE /api/tasks/{task_id}/` - Delete an existing task.
- Filter Tasks: `GET /api/tasks/?title={title}&completed={true/false}` - Filter tasks by title and completion status.
- Bulk Delete Completed Tasks: `DELETE /api/tasks/delete_tasks/` - Bulk delete completed tasks. Send a list of task IDs as taskIds in the request body.

## Usage
- Use frontend application created for this project https://github.com/GiorgiTarsaidze/todo-server
- You can interact with the API using tools like **curl** or **Postman**, creating a frontend application to consume the API endpoints or directly with DRF GUI.
