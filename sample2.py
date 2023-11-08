I can help you create some data for your Django models. Here is the code you can use in the Django shell:

# Create a hospital
hospital = Hospital.objects.create(name="Lat Yao Hospital", address="123 Lat Yao Road, Bangkok, Thailand", phone_number="021234567")

# Create two departments
dept1 = Department.objects.create(hospital=hospital, name="Cardiology")
dept2 = Department.objects.create(hospital=hospital, name="Neurology")

# Create three staff per department
staff1 = Staff.objects.create(name="Dr. Somchai", role=Role.objects.get(name="Doctor"), department=dept1)
staff2 = Staff.objects.create(name="Nurse Suda", role=Role.objects.get(name="Nurse"), department=dept1)
staff3 = Staff.objects.create(name="Pharmacist Nattawut", role=Role.objects.get(name="Pharmacist"), department=dept1)
staff4 = Staff.objects.create(name="Dr. Somsak", role=Role.objects.get(name="Doctor"), department=dept2)
staff5 = Staff.objects.create(name="Nurse Nuch", role=Role.objects.get(name="Nurse"), department=dept2)
staff6 = Staff.objects.create(name="Pharmacist Nong", role=Role.objects.get(name="Pharmacist"), department=dept2)

# Create three empty rooms per department
room1 = Room.objects.create(department=dept1, room_number=101)
room2 = Room.objects.create(department=dept1, room_number=102)
room3 = Room.objects.create(department=dept1, room_number=103)
room4 = Room.objects.create(department=dept2, room_number=201)
room5 = Room.objects.create(department=dept2, room_number=202)
room6 = Room.objects.create(department=dept2, room_number=203)

# Create 10 patients with 2 that are in rooms
patient1 = Patient.objects.create(name="Mr. A", address="456 Lat Yao Road, Bangkok, Thailand", phone_number="0812345678", department=dept1, staff=staff1, age=50, room=room1)
patient2 = Patient.objects.create(name="Mrs. B", address="789 Lat Yao Road, Bangkok, Thailand", phone_number="0912345678", department=dept1, staff=staff2, age=45, room=room2)
patient3 = Patient.objects.create(name="Mr. C", address="123 Rama IX Road, Bangkok, Thailand", phone_number="0612345678", department=dept1, staff=staff3, age=60, room=None)
patient4 = Patient.objects.create(name="Mrs. D", address="456 Rama IX Road, Bangkok, Thailand", phone_number="0712345678", department=dept1, staff=staff1, age=55, room=None)
patient5 = Patient.objects.create(name="Mr. E", address="789 Rama IX Road, Bangkok, Thailand", phone_number="0812345679", department=dept1, staff=staff2, age=65, room=None)
patient6 = Patient.objects.create(name="Mrs. F", address="123 Sukhumvit Road, Bangkok, Thailand", phone_number="0912345679", department=dept2, staff=staff4, age=40, room=room4)
patient7 = Patient.objects.create(name="Mr. G", address="456 Sukhumvit Road, Bangkok, Thailand", phone_number="0612345679", department=dept2, staff=staff5, age=35, room=room5)
patient8 = Patient.objects.create(name="Mrs. H", address="789 Sukhumvit Road, Bangkok, Thailand", phone_number="0712345679", department=dept2, staff=staff6, age=50, room=None)
patient9 = Patient.objects.create(name="Mr. I", address="123 Silom Road, Bangkok, Thailand", phone_number="0812345680", department=dept2, staff=staff4, age=45, room=None)
patient10 = Patient.objects.create(name="Mrs. J", address="456 Silom Road, Bangkok, Thailand", phone_number="0912345680", department=dept2, staff=staff5, age=55, room=None)

# Create 10 accounting records that date from today to back 1 year
import datetime
accounting1 = Accounting.objects.create(balance=10000, date=datetime.date.today(), hospital=hospital, patient=patient1)
accounting2 = Accounting.objects.create(balance=8000, date=datetime.date.today() - datetime.timedelta(days=30), hospital=hospital, patient=patient2)
accounting3 = Accounting.objects.create(balance=5000, date=datetime.date.today() - datetime.timedelta(days=60), hospital=hospital, patient=patient3)
accounting4 = Accounting.objects.create(balance=4000, date=datetime.date.today() - datetime.timedelta(days=90), hospital=hospital, patient=patient4)
accounting5 = Accounting.objects.create(balance=3000, date=datetime.date.today() - datetime.timedelta(days=120), hospital=hospital, patient=patient5)
accounting6 = Accounting.objects.create(balance=2000, date=datetime.date.today() - datetime.timedelta(days=150), hospital=hospital, patient=patient6)
accounting7 = Accounting.objects.create(balance=1000, date=datetime.date.today() - datetime.timedelta(days=180), hospital=hospital, patient=patient7)
accounting8 = Accounting.objects.create(balance=500, date=datetime.date.today() - datetime.timedelta(days=210), hospital=hospital, patient=patient8)
accounting9 = Accounting.objects.create(balance=300, date=datetime.date.today() - datetime.timedelta(days=240), hospital=hospital, patient=patient9)
accounting10 = Accounting.objects.create(balance=100, date=datetime.date.today() - datetime.timedelta(days=270), hospital=hospital, patient=patient10)

# Create 5 appointments
appointment1 = Appointment.objects.create(staff=staff1, patient=patient3, dateTime=datetime.datetime.now(), detail="Check-up")
appointment2 = Appointment.objects.create(staff=staff2, patient=patient4, dateTime=datetime.datetime.now() + datetime.timedelta(hours=1), detail="Blood test")
appointment3 = Appointment.objects.create(staff=staff4, patient=patient8, dateTime=datetime.datetime.now() + datetime.timedelta(hours=2), detail="MRI scan")
appointment4 = Appointment.objects.create(staff=staff5, patient=patient9, dateTime=datetime.datetime.now() + datetime.timedelta(hours=3), detail="Physical therapy")
appointment5 = Appointment.objects.create(staff=staff6, patient=patient10, dateTime=datetime.datetime.now() + datetime.timedelta(hours=4), detail="Medication refill")

# Create 20 medicines with real medicine names
medicine1 = Medicine.objects.create(name="Paracetamol", price=10, amount=100)
medicine2 = Medicine.objects.create(name="Ibuprofen", price=15, amount=80)
medicine3 = Medicine.objects.create(name="Aspirin", price=20, amount=60)
medicine4 = Medicine.objects.create(name="Amoxicillin", price=25, amount=50)
medicine5 = Medicine.objects.create(name="Ciprofloxacin", price=30, amount=40)
medicine6 = Medicine.objects.create(name="Metformin", price=35, amount=30)
medicine7 = Medicine.objects.create(name="Atorvastatin", price=40, amount=20)
medicine8 = Medicine.objects.create(name="Lisinopril", price=45, amount=10)
medicine9 = Medicine.objects.create(name="Omeprazole", price=50, amount=5)
medicine10 = Medicine.objects.create(name="Loratadine", price=55, amount=0)
medicine11 = Medicine.objects.create(name="Diphenhydramine", price=60, amount=100)
medicine12 = Medicine.objects.create(name="Albuterol", price=65, amount=80)
medicine13 = Medicine.objects.create(name="Prednisone", price=70, amount=60)
medicine14 = Medicine.objects.create(name="Hydrocortisone", price=75, amount=50)
medicine15 = Medicine.objects.create(name="Gabapentin", price=80, amount=40)
medicine16 = Medicine.objects.create(name="Tramadol", price=85, amount=30)
medicine17 = Medicine.objects.create(name="Codeine", price=90, amount=20)
medicine18 = Medicine.objects.create(name="Morphine", price=95, amount=10)
medicine19 = Medicine.objects.create(name="Fentanyl", price=100, amount=5)
medicine20 = Medicine.objects.create(name="Naloxone", price=105, amount=0)

# Create 3 diseases with real disease names
disease1 = Disease.objects.create(name="Hypertension")
disease2 = Disease.objects.create(name="Diabetes")
disease3 = Disease.objects.create(name="Stroke")

# Create 3 treatments with real treatment names
treatment1 = Treatment.objects.create(name="Lifestyle modification")
treatment2 = Treatment.objects.create(name="Insulin therapy")
treatment3 = Treatment.objects.create(name="Thrombolysis")

# Create 10 prescriptions
prescription1 = Prescription.objects.create(staff=staff1, patient=patient1)
prescription2 = Prescription.objects.create(staff=staff1, patient=patient2)
prescription3 = Prescription.objects.create(staff=staff1, patient=patient3)
prescription4 = Prescription.objects.create(staff=staff1, patient=patient4)
prescription5 = Prescription.objects.create(staff=staff1, patient=patient5)
prescription6 = Prescription.objects.create(staff=staff4, patient=patient