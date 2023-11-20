# IntercityRailwayReservationSystem
HospitalManagementSystem is a proposed project for the "Database Systems for 
Software and Knowledge Engineers" (01219231) course. This web application is 
designed to manage and streamline various aspects of hospital operations through 
an effective database system. The project's goal is to simulate a real-world 
hospital management system, integrating a comprehensive database to handle various 
operations and queries efficiently.


## Goals
- Patient Management: Efficiently handle patient records, including medical history and treatments.
- Appointment Scheduling: Enable easy booking, rescheduling, or cancellation of appointments.
- Billing: Process and track billing.
- Medical Records: Maintain records of disease.
- Search Feature: Offer robust search functionality for quick data access.

## Installation
**For macOS**:

1) Clone the repository:
```
git clone https://github.com/ReggieReo/SuperDuperHospitle.git
cd SuperDuperHospitle
```
2) Check if Python is installed:
```
python --version || python --version
```

3) Create a virtual environment:
```
python -m venv venv
. venv/bin/activate
```
4) Install dependencies:
```
pip install -r requirements.txt
```
5) Migrate the database:
```
python manage.py migrate
```
6) Load sample data:
```
python manage.py create_db
```
7) Run the server:
```
python manage.py runserver
```

For Windows:

1) Clone the repository:
```
git clone https://github.com/ReggieReo/SuperDuperHospitle.git
cd SuperDuperHospitle
```
2) Check if Python is installed
```
python --version || python --version
```
3) Create a virtual environment:
```
python -m venv venv
.\venv\Scripts\activate
```
4) Install dependencies:
```
pip install -r requirements.txt
```
5) Migrate the database:
```
python manage.py migrate
```
6) Load sample data:
```
python manage.py create_db

```
7) Run the server:
```
python manage.py runserver
```