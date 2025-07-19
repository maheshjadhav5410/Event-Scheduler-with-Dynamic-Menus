# Event-Scheduler-with-Dynamic-Menus

A Django-based web application that allows users to schedule events (like parties, functions, or meetings) and select customizable food menus based on Veg/Non-Veg preferences and dynamic pricing.

---

## 📌 Features

- ✅ Schedule events with time slots, dates, and participant limits
- 🍛 Choose between Veg/Non-Veg menu types with ₹150 and ₹200 pricing options
- 🧑‍🍳 Customize menu items (max 5 per menu) with item replacement support
- 🔐 Admin panel to manage menus, pricing, and event data (no coding required)
- ⚙️ Frontend form validation using JavaScript for seamless user experience
- 🗂️ Data stored using Django ORM with SQLite backend

---

## 🛠️ Tech Stack

| Layer      | Technology             |
|------------|------------------------|
| Backend    | Python, Django         |
| Frontend   | HTML, CSS, JavaScript  |
| Database   | SQLite (Django ORM)    |
| Admin Tool | Django Admin Panel     |
| IDE/Tools  | VS Code, SQLite Browser|

---

## 📂 Project Structure
event_scheduler/
│
├── event_app/
│ ├── models.py # Event and Menu models
│ ├── views.py # Logic to handle event creation and menu selection
│ ├── forms.py # Django forms for scheduling
│ ├── templates/ # HTML templates
│ └── static/ # CSS/JS files
│
├── db.sqlite3
├── manage.py
└── README.md

---

## 🧩 Key Functionalities

### 1. Event Scheduling
- Choose event name, date, time slot, and number of persons.
- Form validations ensure required fields are filled and no overlap in time slots.

### 2. Menu Selection
- Two categories: **Veg** and **Non-Veg**
- Two pricing tiers: ₹150 and ₹200 per plate
- Each menu is pre-defined with 4–5 items, editable by admin

### 3. Menu Customization
- Users can replace items from the default menu (limit: 5 total items)
- Changes are stored and linked to the scheduled event

### 4. Admin Features
- Easily add/edit/delete menu options via Django Admin
- No need to update code for content changes

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/your-username/event-scheduler.git
cd event-scheduler
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Visit: http://127.0.0.1:8000/

