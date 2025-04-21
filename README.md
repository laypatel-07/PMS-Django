# WorkSync - Project Management System

WorkSync is a web-based project management system built with Django that allows users to create projects, manage tasks, and track progress. It features a modern, responsive interface with Tailwind CSS that provides a smooth user experience.


## Features

- **User Authentication**: Secure user registration and login
- **Project Management**: Create, view, edit, and delete projects
- **Task Management**: Create tasks with title, description, priority, and due dates
- **Task Assignment**: Assign tasks to team members
- **Kanban Board**: View tasks in a Kanban-style board with To Do, In Progress, and Done columns
- **Dashboard**: Get an overview of your projects and tasks with stats and metrics
- **Task Filtering**: Filter tasks by project, status, priority, or search terms
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

- **Backend**: Django 5.1.7
- **Frontend**: HTML, TailwindCSS
- **Database**: SQLite (default) / MySQL (optional)
- **Authentication**: Django built-in authentication system
- **File Storage**: Django's file storage for project images

## Installation

### Prerequisites

- Python 3.8+
- Node.js and npm (for Tailwind CSS)
- Git

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/worksync.git
cd worksync
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install Tailwind CSS**

```bash
python manage.py tailwind install
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Create a superuser**

```bash
python manage.py createsuperuser
```

7. **Start the development server**

```bash
python manage.py runserver
```

8. **In a separate terminal, start Tailwind build process**

```bash
python manage.py tailwind start
```

9. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000/projects/`

## Configuration

The project uses SQLite by default, but you can switch to MySQL by uncommenting the MySQL configuration in `settings.py`.

### Media Files

Media files (project photos) are stored in the `media/` directory. Make sure this directory has proper permissions.

### Secret Key

For production, replace the default secret key in `settings.py` with a secure key and store it as an environment variable.

## Usage

### Dashboard

The dashboard provides an overview of your projects and tasks, showing statistics like:
- Number of projects
- Task counts by status
- Completion percentage
- Upcoming and overdue tasks
- High priority tasks

### Project Management

- **View Projects**: Go to `/projects/` to see all projects
- **Create Project**: Click "Create Project" button
- **Edit/Delete Project**: Use the respective buttons on the project card

### Task Management

- **View Project Tasks**: Click "View Tasks" on a project card
- **Add Task**: Click "Add Task" on the task list page
- **Edit/Delete Task**: Use the respective buttons on each task card
- **Task Board**: Tasks are organized by status (To Do, In Progress, Done)

### User Management

- **Register**: Create a new account at `/accounts/register/`
- **Login**: Access your account at `/accounts/login/`
- **Logout**: End your session at `/accounts/logout/`

## Project Structure

```
worksync/
├── worksync/           # Project settings
├── projects/           # Main application
│   ├── models.py       # Data models
│   ├── views.py        # View functions
│   ├── forms.py        # Form definitions
│   ├── urls.py         # URL routing
│   └── admin.py        # Admin configurations
├── templates/          # HTML templates
├── static/             # Static files
├── media/              # User-uploaded content
└── theme/              # Tailwind CSS configuration
```

## Development

### Adding New Features

To add new features:
1. Create/modify models in `models.py`
2. Run migrations with `python manage.py makemigrations` and `python manage.py migrate`
3. Add views in `views.py`
4. Create templates in the `templates` directory
5. Update URL patterns in `urls.py`

### Styling

The project uses Tailwind CSS for styling. To modify styles:
1. Edit the Tailwind configuration in the `theme` directory
2. Make changes to the templates using Tailwind utility classes


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Django team for the amazing framework
- Tailwind CSS for the utility-first CSS framework
- All open-source contributors whose libraries made this project possible

