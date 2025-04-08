# 📧 Mail Project
Mail Project is a web-based application designed to manage and send email campaigns. Built using Python and Django, it provides functionalities for user authentication, creating and managing mailing lists, and composing and sending emails.​

## 🚀 Features
> - User registration, authentication, and email verification
> 
> - Create and manage clients (recipients)
>
> - Write messages and set up recurring mailings (daily, weekly, monthly)
>
> - Admin interface for full control
>
> - Monitor the status and performance of email campaigns.​

## 🧰 Tech Stack
> - Backend:
>   - Python 3.11
>   - Django
>   - Django Rest Framework
>
> - Database: 
>   - PostgreSQL
>
> - Scheduling & Tasks:
>    - Celery
>
> - Tools:
>   - Docker
>   - Redis

## 📁 Project Structure
```bash
mail-project/
├── blog/            # Blog app for promoting the service
├── config/          # Project configuration
├── mailings/        # Mailing logic (messages, clients, schedules)
├── users/           # Custom user model & authentication
├── templates/       # HTML templates
├── static/          # Static assets
├── manage.py        # Django project manager
└── requirements.txt # Project dependencies
```

## Installation
### 💻 Local Development

#### Clone the Repository:
```bash
git clone https://github.com/xinis002/mail-project.git
```

#### Navigate to the Project Directory:
```bash
cd mail-project
```

#### Create and Activate a Virtual Environment:
##### Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
##### Windows
```bash
python3 -m venv venv
venv\Scripts\activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables:
Rename the ```.env_example``` file to ```.env``` and configure the necessary environment variables.

#### Apply Migrations
```bash
python manage.py migrate
```

#### Run the Development Server
```bash
python manage.py runserver
```

The application will be accessible at ```http://127.0.0.1:8000/```

## 🤝 Contributing
> Contributions are welcome! 
> Please fork the repository and submit a pull request with your changes.
> 1. Fork the repository
> 2. Create a new branch ```git checkout -b feature-name```
> 3. Commit your changes
> 4. Push to your fork
> 5. Open a pull request


## 📝 License
This project is open-source and available under the MIT License.















