<!-- Header Section -->
<p align="center">
  <img src="https://firebasestorage.googleapis.com/v0/b/valid-form-af9a9.appspot.com/o/Logos%2FAliendoce_logo.png?alt=media&token=75e998bf-f022-485c-afae-b0413b673ffd" alt="Aliencode Logo" width="300">
</p>

<h1 align="center">ALIENCODE</h1>

<h3 align="center">PRT_G16 – SUPPLIERS AND EMPLOYEES MANAGEMENT SYSTEM</h3>

<p align="center">
  <strong>This project was developed by Aliencode to efficiently manage suppliers and employees in educational or business environments.</strong>
</p>

<!-- Badges Section -->
<p align="center">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-blue.svg" height="30">
  <img alt="Version" src="https://img.shields.io/badge/Version-1.0.0-green.svg" height="30">
</p>

---

## 📌 Description

**PRT_G16** is a web application developed with Django that allows you to register, view, update, and delete **suppliers** and **employees** in an organized, visual, and intuitive interface.

It is intended for institutions or companies that require internal control of both national and international suppliers and staff.

---

## ✨ Key Features

- ✅ Full CRUD operations for employees and suppliers.
- 📷 Image upload and preview for employees.
- 🌍 Country flags display based on supplier location.
- 🧱 Modular design with a clean, mockup-style interface.
- 🔒 Secure forms with CSRF protection.
- 📁 Image and file handling using `Pillow`.

---

## 🛠 Technologies Used

- **Language:** Python 3.11
- **Framework:** Django 5.2.3
- **Database:** PostgreSQL (via `psycopg2`)
- **Libraries and Packages:**
  - `pillow` – Image processing.
  - `sqlparse` – Django's internal SQL parser.
  - `tzdata` – Timezone support for Python apps.

---

## 🚀 Project Installation (Django Backend)

1. **Installation:**

    ```bash
    # Clone the repository
    git clone https://github.com/MichaelPaucar07/PRT_G16.git
    cd PRT_G16

    # Create and activate a virtual environment
    python -m venv venv
    venv\Scripts\activate  # For Windows

    # Install dependencies
    pip install -r requirements.txt

    # Run initial migrations
    python manage.py makemigrations
    python manage.py migrate
2. **Start the application:**

    python manage.py runserver

## Quick Start

1. **Run the application:**
   ```bash
   python manage.py runserver

<!-- Support Section -->
## Support

For additional help or to discuss ideas, feel free to get in touch:

- ✉️ Email:
  - [michael.paucar@espoch.edu.ec](mailto:michael.paucar@espoch.edu.ec)
  - [michaelpaucar77@gmail.com](mailto:michaelpaucar77@gmail.com)

- 👥 LinkedIn: [Michael Paucar](https://www.linkedin.com/in/michaelpaucar/)

<!-- License Section -->
## License
This project is under the [MIT License](LICENSE). Refer to the [LICENSE.md](LICENSE.md) file for more details.

<!-- Copyright Section -->
## Copyright
<div style="background-color: #f2f2f2; padding: 20px; text-align: center;">
  <p style="font-family: 'Arial', sans-serif; font-size: 7px; font-weight: normal; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; color: #555;">
    <span style="border-bottom: 1px solid #555; text-align: center;">© 2025 Copyright Aliencode. All rights reserved.</span>
  </p>
