# MaiChaiNaHH Hospital
MaiChaiNaHH Hospital is a proposed project for the "Database Systems for 
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

1) Clone the repository:
```
git clone https://github.com/ReggieReo/SuperDuperHospitle.git
cd SuperDuperHospitle
```
2) Check if Python is installed:
```
python3 --version || python --version
```
3) Create a virtual environment:
```
python3 -m venv venv
. venv/bin/activate
```
4) Install dependencies:
```
pip install -r requirements.txt
```
5) Migrate the database:
```
python3 manage.py migrate
```
6) Load sample data:
```
python3 manage.py create_db
```
7) Run the server:
```
python3 manage.py runserver
```
