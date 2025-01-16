import os

# Define project structure
project_structure = {
    "django-chat-app/": {
        "chat/": {
            "migrations/": {},
            "static/": {
                "css/": {"style.css": "/* Add your styles here */"},
                "js/": {"chat.js": "// JavaScript for chat WebSocket functionality"},
                "images/": {},
            },
            "templates/": {
                "chat/": {
                    "home.html": "<!-- HTML for user list -->",
                    "room.html": "<!-- HTML for chat room -->",
                }
            },
            "__init__.py": "",
            "admin.py": "# Admin customization",
            "apps.py": "# App configuration",
            "consumers.py": "# WebSocket consumers code",
            "models.py": "# Models for chat and user",
            "routing.py": "# WebSocket routing",
            "tests.py": "# Tests for the app",
            "urls.py": "# URL routing for chat app",
            "views.py": "# Views for rendering and handling chat logic",
        },
        "chat_app/": {
            "__init__.py": "",
            "asgi.py": "# ASGI config for WebSocket",
            "settings.py": "# Django project settings",
            "urls.py": "# Main URL routing",
            "wsgi.py": "# WSGI configuration for deployment",
        },
        "db.sqlite3": "",  # Optional database file for SQLite
        "manage.py": "# Django management script",
        "requirements.txt": "Django\nchannels\nchannels-redis\n",
        "README.md": "# Documentation for the project",
    }
}

# Function to create files and directories
def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

# Generate the project
base_path = os.getcwd()  # Current directory
create_project_structure(base_path, project_structure)

print(f"Project structure created at {base_path}")
