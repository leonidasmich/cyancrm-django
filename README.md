# Django CRM: Manage Leads and Clients

This is a lightweight CRM (Customer Relationship Management) system built with Django. The application helps you manage leads, track their statuses, and convert them into clients effortlessly.

---

## Features

- **Lead Management**: Add and organize leads with detailed information.
- **Lead Status Tracking**: Monitor the progress of each lead with customizable statuses.
- **Client Conversion**: Seamlessly convert leads into clients when deals are closed.
- **Admin Dashboard**: Manage leads and clients from a simple and intuitive admin interface.

---

## Installation

### Prerequisites
- Python 3.9+
- Django 4.0+
- A database (SQLite is configured by default)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-crm.git
   cd django-crm
   ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate # On windows: venv/Scripts/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Usage

1. Add new leads with relevant details such as name, contact information, and status.

2. Update lead statuses to track their progress.

3. Convert a lead to a client when the deal is successful.

4. Manage all data via the admin interface at /admin/.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.