# EcommerceWithDjangoVueStripe

EcommerceWithDjangoVueStripe is a full-stack e-commerce platform combining a Django backend (`django_djakets`) with a Vue.js frontend (`vue_djakets`). The platform includes product management, user authentication, and a secure checkout process using Stripe.

## Project Structure

- **django_djakets**: Backend built with Django, handling API, authentication, and payment integration with Stripe.
- **vue_djakets**: Frontend built with Vue.js, providing a responsive and user-friendly interface for the e-commerce site.

## Features

- **Django Backend:**
  - Product and order management
  - User authentication
  - API endpoints for frontend integration
  - Stripe payment gateway

- **Vue Frontend:**
  - Dynamic product listings
  - Shopping cart management
  - User registration and login
  - Integrated Stripe checkout

## Getting Started

### Prerequisites

- Python 3.x
- Node.js 14.x or later
- Django 3.x or later
- Vue CLI
- Stripe API keys

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yantheo/EcommerceWithDjangoVueStripe.git
cd EcommerceWithDjangoVueStripe

2. Set Up the Backend (Django)
Navigate to the django_djakets directory:

bash
Copier le code
cd django_djakets
Create and activate a virtual environment:

bash
Copier le code
python -m venv venv
source venv/bin/activate
Install the required dependencies:

bash
Copier le code
pip install -r requirements.txt
Set up environment variables for Stripe API keys:

bash
Copier le code
export STRIPE_SECRET_KEY='your_secret_key'
export STRIPE_PUBLISHABLE_KEY='your_publishable_key'
Apply migrations:

bash
Copier le code
python manage.py migrate
Run the development server:

bash
Copier le code
python manage.py runserver
Usage:

Access the admin panel at /admin/ to manage products and orders.
The API endpoints for managing orders and integrating Stripe are available under /api/

3. Set Up the Frontend (Vue.js)
Navigate to the vue_djakets directory:

bash
Copier le code
cd ../vue_djakets
Install the required dependencies:

bash
Copier le code
npm install
Set up environment variables for API base URL and Stripe publishable key:

bash
Copier le code
echo "VUE_APP_API_BASE_URL=http://localhost:8000/api/" > .env
echo "VUE_APP_STRIPE_PUBLISHABLE_KEY=your_publishable_key" >> .env
Run the development server:

bash
Copier le code
npm run serve
