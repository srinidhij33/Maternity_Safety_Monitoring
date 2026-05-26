# Maternity_Safety_Monitoring
Maternal Health Risk Assessment System
A web app that predicts pregnancy risk levels using machine learning.

# What it does
Enter 6 health measurements → get a risk result (Low / Mid / High) → receive an email alert.
The six inputs are: Age, Systolic BP, Diastolic BP, Blood Sugar, Body Temperature, Heart Rate.

# Tech Used

Python & Django
scikit-learn (Random Forest)
SQLite
Bootstrap 4
yagmail (for email alerts)


# User Roles
RoleWhat they can doPatientRegister, submit health data, get predictions, view historyDoctorRegister, view patient recordsAdminActivate patient and doctor accounts
Admin login — username: admin / password: admin

Setup
bash# 1. Clone the repo
git clone https://github.com/your-username/maternal-health-risk.git
cd maternal-health-risk

# 2. Install dependencies
pip install django scikit-learn pandas numpy yagmail

# 3. Run migrations
python manage.py migrate

# 4. Start the server
python manage.py runserver
Then open http://127.0.0.1:8000 in your browser.

Note: Update the CSV path in Heart/views.py and users/views.py to point to your local copy of the dataset before running.


Project Structure
├── Heart/       → settings, URLs, main views, ML model
├── users/       → patient registration, prediction, history
├── admins/      → account activation
├── doctor/      → doctor portal
├── media/       → dataset CSV + saved model (mra.pkl)
└── db.sqlite3   → database

# Dataset
Maternal Health Risk Dataset — UCI Machine Learning Repository

# Note
This project was built for academic purposes and is not intended for clinical use.
