# 🦠 COVID-19 India Dashboard (Django + API Project)

A real-time web dashboard built using **Django** and data from the [Rootnet API](https://api.rootnet.in/covid19-in/stats/latest), displaying COVID-19 stats across Indian states with a responsive and searchable UI.

---

## ✨ Features

- ✅ Fetches live COVID-19 data from API
- ✅ Total cases summary
- ✅ Per-state stats (confirmed, discharged, deaths)
- ✅ Mobile-friendly and searchable table
- ✅ Clean, responsive UI with HTML + CSS

---

## 🧰 Tech Stack

- 🐍 Python
- 🌿 Django
- 🌐 HTML, CSS, JavaScript
- 🔗 REST API (Rootnet)
- ⚙️ Bootstrap (optional for styling)

---

## 📸 Screenshots

### Login Page
<p align="center">
  <img src="https://github.com/nikitajadhav05/covid-dashboard-django/blob/main/Assets/img/LOGINscreenshot.png?raw=true" 
       alt="Login Screenshot" width="600">
</p>

### Dashboard Page
<p align="center">
  <img src="https://github.com/nikitajadhav05/covid-dashboard-django/blob/main/Assets/img/DASHBOARDscreenshot.png?raw=true" 
       alt="Dashboard Screenshot" width="700">
</p>

---

## 🎥 Demo Video

See the dashboard in action! 🎬

<p align="center">
  <img src="https://github.com/nikitajadhav05/covid-dashboard-django/blob/main/Assets/gif/Covid_Report.gif?raw=true" 
       alt="COVID Dashboard Demo" width="700">
</p>


---

## 🚀 How to Run Locally


git clone https://github.com/nikitajadhav05/covid-dashboard-django.git
cd covid-dashboard-django
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py runserver





## 📁 Folder Structure
Covid_Report/
├── covid_app/
│ ├── migrations/ # DB migrations
│ ├── static/ # Static files (CSS, JS, etc.)
│ ├── templates/ # HTML templates
│ ├── admin.py # Django admin config
│ ├── models.py # Database models
│ ├── urls.py # URL routing for app
│ └── views.py # Logic for API and data rendering
├── Covid_Report/
│ ├── init.py
│ ├── settings.py # Django settings
│ ├── urls.py # URL routing (project level)
│ └── wsgi.py # WSGI entry point
├── db.sqlite3 # SQLite database file
├── manage.py # Django CLI entry point
└── screenshot.png # Project screenshot for README






📌 Purpose
This project was built to learn how to:

Work with external APIs in Django

Structure Django projects properly

Create responsive, user-friendly dashboards


🙋‍♀️ Author
Nikita Jadhav
📧 [nikitajadhav9322@gmail.com](mailto:nikitajadhav9322@gmail.com)  
🔗 [GitHub: nikitajadhav05](https://github.com/nikitajadhav05)
🔗 [LinkedIn: Nikita Jadhav](https://www.linkedin.com/in/nikita-jadhav-899867316)





⭐ If you found this project helpful, consider giving it a star!




