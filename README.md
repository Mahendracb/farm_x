# FarmX (Krishi Mitra AI)

A full-stack agricultural support platform built with Django (Backend) and React (Frontend). 
This project is specifically tailored for farmers **across the state of Karnataka**, featuring localized data for crop prices (from various APMCs like Kodagu, Shivamogga, Kalaburagi, Mandya), state government schemes (Krishi Bhagya, Raitha Vidya Nidhi), and major regional buyers.

## Prerequisites

Make sure you have the following installed on your machine:
- [Python 3.x](https://www.python.org/downloads/)
- [Node.js & npm](https://nodejs.org/en/download)

## How to Run the Project Locally

You will need to run the **Backend** and **Frontend** servers simultaneously in two separate terminal windows.

---

### 1. Run the Backend (Django)

Open a terminal and follow these steps:

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Install Python dependencies:**
   *(It's recommended to do this inside a virtual environment)*
   ```bash
   pip install django djangorestframework django-cors-headers
   ```

3. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the Django Development Server:**
   ```bash
   python manage.py runserver
   ```
   The backend API will now be running at `http://127.0.0.1:8000/`.

---

### 2. Run the Frontend (React)

Open a **second, new terminal window** and follow these steps:

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node modules (only needed the first time):**
   ```bash
   npm install
   ```
   *(Wait for the dependencies to finish installing)*

3. **Start the React Development Server:**
   ```bash
   npm start
   ```
   The frontend app will automatically open in your web browser at `http://localhost:3000/`.
