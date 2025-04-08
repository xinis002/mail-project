# 📩 Mail Project
Mail Project is a web-based application designed to manage and send email campaigns. Built using Python and Django, it provides functionalities for user authentication, creating and managing mailing lists, and composing and sending emails.​

## Features
> - User Authentication: Secure user registration and login system.​
>
> - Mailing Lists Management: Create, edit, and delete mailing lists to organize contacts.​
>
> - Email Composition: Compose emails with rich text formatting.​
>
> - Campaign Tracking: Monitor the status and performance of email campaigns.​

## Project Structure
>The project is organized into the following main directories:
>
>blog: Handles the blog-related functionalities.​
>
>config: Contains configuration files for the project.​
>
>mailings: Manages the email-related operations, including templates and sending mechanisms.​
>
>users: Manages user authentication and profile management.​

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

## Contributing
> Contributions are welcome! 
> Please fork the repository and submit a pull request with your changes.

















