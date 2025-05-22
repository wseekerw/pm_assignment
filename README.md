# Django-React assignment App (Monorepo)

This is a Django-React monorepo project built for assignemnt.

## 📁 Project Structure

- **Backend (Django)** — Main server and API logic
- **Frontend (React)** — Located in the `frontend/` folder
- **Compiled React App** — Located in `fronted/dist/`, served by Django when the server is running

---

## 🚀 Getting Started

Clone the repository

git clone git@github.com:wseekerw/pm_assignment.git

Create the environment

python -m venv env / source env/bin/activate

Install the requirements

pip install -r requirements.txt

Migrate and run server

python manage.py migrate / python manage.py runserver
