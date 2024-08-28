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
- Navigate to the django_djakets directory:
- cd django_djakets

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

Install the required dependencies:
pip install -r requirements.txt

Set up environment variables for Stripe API keys:
export STRIPE_SECRET_KEY='your_secret_key'
export STRIPE_PUBLISHABLE_KEY='your_publishable_key'

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Usage:

- Access the admin panel at /admin/ to manage products and orders.
- The API endpoints for managing orders and integrating Stripe are available under /api/



