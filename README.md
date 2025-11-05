# VeedPal 🏃‍♂️💨

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Veedpal** A secure video streaming platform where users can watch, upload, and share videos. Support creators directly with payments and tips while enjoying a seamless streaming experience.  

Built with **Django**, **Django REST Framework**, and **JWT Authentication**, VeedPal is secure, scalable, and ready for real-world deployment.

---

## Features 🚀

### Core Features
- **User Registration & Authentication**
  - JWT-based login & signup
  - Password reset & profile management
- **Errand Requests**
  - Post, update, and delete errands
  - Browse available errands
  - Real-time status updates: Pending → In Progress → Completed
- **Runner Interaction**
  - Accept or decline errands
  - Communicate via comments/messages
- **Payments & Tips**
  - Pay for completed errands
  - Leave optional tips for excellent service
- **Ratings & Reviews**
  - Rate runners after task completion
  - View average ratings for service quality

### Admin Features
- Manage users, errands, and payments
- Track platform activity and generate reports

---

## Tech Stack 🛠️

- **Backend**: Django, Django REST Framework  
- **Authentication**: JWT (`djangorestframework-simplejwt`)  
- **Database**: PostgreSQL (recommended)  
- **Async Tasks**: Celery & Redis (notifications, payment processing)  
- **Payments**: Stripe / PayPal integration  
- **Storage**: AWS S3 / DigitalOcean Spaces (optional, for file uploads)  
- **Deployment**: Docker, GitLab CI/CD, or cloud providers (Heroku, AWS, DigitalOcean)

---

## Installation & Setup ⚙️

### Clone the repository
```bash
git clone https://github.com/samuelmwangi729/veedpal.git
cd veedpal
```

# Install the depedencies
_make sure pip is installed_
```bash
pip install -r requirements.txt
```

# Configure environment variables 
```bash
DEBUG=
SECRET_KEY=''
DATABASE_URL=''
STRIPE_API_KEY=''
MPESA_PRODUCTION_KEY=''
MPESA_SHORT_CODE=''
```
# Run migrations 
```bash
python manage.py makemigrations
```

# Create Super user 
```bash
python manage.py createsuperuser
```

# Run the server 
```bash
python manage.py runserver 
```

# End Points of the application

*Coming sooner*