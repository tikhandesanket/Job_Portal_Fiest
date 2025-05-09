# 🎉 Job Portal Fiesta

A simple Django-based job portal web application that allows users to view job listings and recruiters to post/manage job offers. Includes user authentication and application functionality.

---

## 🚀 Features

- ✅ User registration and login system
- 💼 Recruiters can post, update, and manage job listings
- 🔍 Job seekers can browse and apply for jobs
- 👥 Role-based content display (`recruiter` vs `job_seeker`)
- 🎨 Bootstrap 5-based responsive UI
- 🧠 Context-aware navigation bar
- 💾 SQLite database for development

---

## 🛠️ Tech Stack

- **Backend:** Python, Django 4.2
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite3
- **Packages:**

  - `widget_tweaks` (for form customization)
  - Django built-in apps

---

## 📂 Project Structure

```
JOB_PORTAL_FIESTA/
├── accounts/
│   ├── models.py         # Job, Application, Profile
│   ├── views.py
│   ├── forms.py
│   ├── context_processors.py
│   ├── urls.py
│   └── templates/accounts/
│       ├── base.html
│       ├── login.html
│       ├── job_list.html
│       ├── job_create.html
│       ├── apply_job.html
├── jobs/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/jobs/
│       ├── job_list.html
│       ├── job_create.html
│       ├── apply_job.html
├── Job_Portal_Fiesta/
│   ├── settings.py
│   ├── urls.py
└── manage.py
```

---

## ⚙️ Django Settings Highlights

- 🔐 `SECRET_KEY`: Keep this secret in production
- 🛑 `DEBUG = True`: Change to `False` in production
- 🌐 `ALLOWED_HOSTS`: Empty for now (add domains/IPs when deploying)
- 🔗 `INSTALLED_APPS`: Includes `accounts`, `jobs`, `widget_tweaks`, and default Django apps
- 📁 `TEMPLATES`: Uses `'DIRS': [BASE_DIR / 'accounts/templates']` and app directories
- 📦 `DATABASE`: SQLite3 by default
- 🔄 `LOGIN_REDIRECT_URL`: Redirects users after login

---

## 🧪 How to Run

1. 🐍 Create virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

2. 📦 Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. 🛠️ Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. 🚀 Start development server:

   ```bash
   python manage.py runserver
   ```

5. 🌐 Open in browser:

   - Visit: `http://127.0.0.1:8000/`

---

## 👨‍💻 Admin Access

To create a superuser for admin access:

```bash
python manage.py createsuperuser
```

Then visit `/admin` to manage models.

---

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📃 License

MIT License © 2025 NexaBinaryX Technologies Team
