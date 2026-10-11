# BlogSpace — Stories That Matter
Live Website: "Visit BlogSpace" (https://blogspace-8ohz.onrender.com)

BlogSpace is a Django-based blogging platform where users can explore blog posts, read stories, search by title, and organize posts into categories. It features a clean, Pinterest-inspired design with soft colors and a bookish aesthetic.

## Features

- View all blog posts on the homepage.
- Create new blog posts.
- Read individual blog posts.
- Edit and delete existing posts.
- Search posts by title.
- Organize posts into categories.
- Use Django Admin to manage blog posts.
- Responsive styling for different screen sizes.

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git and GitHub

## Project Structure

```text
BlogSpace/
├── blog/
│   ├── migrations/
│   ├── static/
│   │   └── blog/
│   │       └── style.css
│   ├── templates/
│   │   └── blog/
│   │       ├── home.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── post_confirm_delete.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd BlogSpace
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create and activate a virtual environment

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an admin account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your account.

### 6. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

The Django admin panel is available at http://127.0.0.1:8000/admin/.

## Sample Data

Create sample blog posts through the website or Django Admin to explore the application's features.

## Future Improvements

- User registration and login.
- Comments and likes.
- Blog cover image uploads.
- Improved search and filtering.
- Deployment to a public hosting service.

## Project Reference

This project was inspired by the Blogging Platform project listed on GeeksforGeeks' Django Projects page.

Reference: https://www.geeksforgeeks.org/python/django-projects/

## Author

Developed as a practical Django project for academic learning.

## License

This project is intended for educational purposes.
