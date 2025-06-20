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
## 📸 Screenshot

![COVID Dashboard Screenshot](https://github.com/nikitajadhav05/covid-dashboard-django/blob/main/screenshot.png?raw=true)


---

## 🚀 How to Run Locally


git clone https://github.com/nikitajadhav05/covid-dashboard-django.git
cd covid-dashboard-django
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py runserver





📁 Folder Structure

Covid_Report/
│
├── covid_app/                # Django app
│   ├── templates/            # HTML templates
│   └── views.py              # Main logic for API call + data rendering
│
├── Covid_Report/             # Project settings
├── db.sqlite3                # Local DB
└── manage.py


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




