# django-setup

## How to run the application

### 1. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run database migrations

```bash
python manage.py migrate
```

### 4. Start the development server

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`. You can verify the health check endpoint at `http://127.0.0.1:8000/health/`.
