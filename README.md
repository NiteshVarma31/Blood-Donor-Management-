# Blood Donor Management System

A web-based application designed to manage and streamline blood donation activities between donors, hospitals, and administrators.

---

## 🛠️ Technologies Used

- **Backend**: Python (Django)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite

---

## 🚀 Features

### Donor Module

- Donor registration and profile management
- Blood donation request initiation and tracking
- View donation history and request status

### Admin Module

- Dashboard with donation stats
- Manage donors and their records
- Approve or reject blood donation requests
- Generate donation reports

---

## 📁 Project Structure

Blood-Donor-Management/
├── manage.py
├── db.sqlite3
├── blood_bank/
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ └── urls.py
└── requirements.txt


---

## 🔧 Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/NiteshVarma31/Blood-Donor-Management-.git
cd Blood-Donor-Management-

python -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
