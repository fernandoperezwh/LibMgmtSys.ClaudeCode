# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LibMgmtSys is a Django web application for book library management. It features CRUD operations for books, authors, and publishers (editoriales) with a clean, Bootstrap 5-based UI. The project uses Django's class-based views and includes rich text editing capabilities via CKEditor.

## Development Commands

### Environment Setup
```bash
cd src/
pipenv install  # Install dependencies in virtual environment
pipenv shell    # Activate virtual environment
```

### Running the Application
```bash
cd src/
python manage.py runserver  # Start development server on http://localhost:8000/
```

### Database Operations
```bash
cd src/
python manage.py makemigrations  # Create new migrations
python manage.py migrate         # Apply database migrations
python manage.py createsuperuser # Create admin user (optional)
```

### Testing
```bash
cd src/
python manage.py test  # Run Django tests
```

### Static Files
```bash
cd src/
python manage.py collectstatic  # Collect static files (needed for CKEditor)
```

## Architecture

### Project Structure
```
src/
├── apps/biblioteca/     # Main Django app with models, views, templates
├── core/               # Django project configuration
├── templates/          # Global templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User-uploaded files (book covers)
└── manage.py           # Django management script
```

### Data Models
- **Editorial**: Publishers with slug URLs, location info, optional website
- **Autor**: Authors with name, surname, email
- **Libro**: Books with many-to-many authors, foreign key to publisher, rich text description, image upload

### Key Technologies
- Django 4.2 (LTS) with class-based views (ListView, CreateView, UpdateView, DeleteView, DetailView)
- SQLite database
- CKEditor for rich text fields with custom toolbar configuration
- Pillow for image handling
- Bootstrap 5 via CDN for responsive UI
- Automatic slug generation for SEO-friendly URLs

### Views Pattern
All views use Django's class-based views without authentication requirements. URLs use slug-based patterns for better SEO. The root URL (/) redirects to the book list view.

### Template System
Templates use Bootstrap 5 components with custom CSS for form styling. Base template includes CKEditor assets and initialization scripts.

### Important Configuration
- CKEditor configured with custom toolbar in `settings.py`
- Media files configured for image uploads
- Static files setup for CKEditor assets
- Spanish verbose names in model Meta classes