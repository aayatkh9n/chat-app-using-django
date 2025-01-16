

Django Chat Application
A real-time chat application built with Django and WebSockets, providing user authentication, user-friendly chat interfaces, and persistent message storage.

Features
User Authentication: Users can sign up, log in, and log out securely.
Real-time Messaging: WebSocket-based communication for instant messaging.
Persistent Chat History: Messages are stored in the database and can be retrieved anytime.
User List: View all registered users in a collapsible side menu.
Chat Interface: User-friendly interface to exchange messages with other users.
Responsive Design: The interface adapts seamlessly to various devices.
Tech Stack
Backend: Django, Django REST Framework, Channels
Frontend: HTML, CSS, JavaScript
Database: SQLite (default) or any Django-supported database
WebSocket Support: Channels with Redis
Installation and Setup
Follow these steps to set up and run the project locally:

1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/django-chat-app.git
cd django-chat-app
2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Start the Redis Server
Ensure Redis is installed and running on your system:

bash
Copy
Edit
redis-server
6. Run the Development Server
bash
Copy
Edit
python manage.py runserver
7. Access the Application
Open your browser and navigate to:

arduino
Copy
Edit
http://127.0.0.1:8000/
Usage
Sign Up and Log In:
Create a new account or log in with existing credentials.
View User List:
Access the list of registered users from the collapsible side menu.
Initiate a Chat:
Select a user from the menu to start a chat.
Send Messages:
Type a message in the chat interface and press Enter to send.
View Chat History:
Scroll up to see the chat history with a user.
Project Structure
php
Copy
Edit
django-chat-app/
│
├── chat/                     # Chat application
│   ├── migrations/           # Database migrations
│   ├── static/               # Static files (CSS, JS)
│   ├── templates/            # HTML templates
│   ├── models.py             # Database models
│   ├── views.py              # Views for user and chat
│   ├── consumers.py          # WebSocket consumers
│   └── routing.py            # WebSocket routes
│
├── chat_app/                 # Main project
│   ├── settings.py           # Project settings
│   ├── urls.py               # Application routes
│   ├── asgi.py               # ASGI configuration
│   └── wsgi.py               # WSGI configuration
│
├── manage.py                 # Django management script
└── requirements.txt          # Project dependencies
Dependencies
Django
Django REST Framework
Channels
Channels Redis
Redis (server)
Contributing
Fork the repository.
Create a new branch:
bash
Copy
Edit
git checkout -b feature/your-feature-name
Commit your changes:
bash
Copy
Edit
git commit -m "Add your message here"
Push to your branch:
bash
Copy
Edit
git push origin feature/your-feature-name
Open a Pull Request.
License
This project is licensed under the MIT License.

Acknowledgments
Django Documentation
Channels Documentation
