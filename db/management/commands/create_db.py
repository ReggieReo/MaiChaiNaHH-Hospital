from django.core.management.base import BaseCommand
from db.models import *
from db.models import *


class Command(BaseCommand):
    help = 'Create sample models for the app'

    def handle(self, *args, **kwargs):
        h = Hospital(name="Lat Yao Hospital", address="Lat Yao, Bangkok, Thailand", phone_number="021234567")
        h.save()

        # Create two departments
        d1 = Department(hospital=h, name="Neuro")
        d1.save()
        d2 = Department(hospital=h, name="Internal medicine")
        d2.save()

        # 2 role
        role1 = Role.objects.create(name="Doctor")
        role2 = Role.objects.create(name="Nurse")
        role3 = Role.objects.create(name="Pharmacist")

        # Create three staff per department
        s1 = Staff(name="Dr. Somchai", role=role1, department=d1)
        s1.save()
        s2 = Staff(name="Nurse Nong", role=role2, department=d1)
        s2.save()
        s3 = Staff(name="Pharmacist Ploy", role=role3, department=d1)
        s3.save()
        s4 = Staff(name="Dr. Somsak", role=role1, department=d2)
        s4.save()
        s5 = Staff(name="Nurse Noi", role=role2, department=d2)
        s5.save()
        s6 = Staff(name="Pharmacist Pim", role=role3, department=d2)
        s6.save()

        # Create 10 patients with 4 that are in rooms
        p1 = Patient(name="Arun", address="Bang Kapi, Bangkok, Thailand", phone_number="0812345678", department=d1,
                     staff=s1, age=45)
        p1.save()
        p2 = Patient(name="Boon", address="Bang Na, Bangkok, Thailand", phone_number="0823456789", department=d1,
                     staff=s1, age=50)
        p2.save()
        p3 = Patient(name="Chai", address="Chatuchak, Bangkok, Thailand", phone_number="0834567890", department=d1,
                     staff=s1, age=55)
        p3.save()
        p4 = Patient(name="Dao", address="Din Daeng, Bangkok, Thailand", phone_number="0845678901", department=d1,
                     staff=s1, age=60)
        p4.save()
        p5 = Patient(name="Eak", address="Ekkamai, Bangkok, Thailand", phone_number="0856789012", department=d1,
                     staff=s1, age=65)
        p5.save()
        p6 = Patient(name="Fah", address="Lat Phrao, Bangkok, Thailand", phone_number="0867890123", department=d2,
                     staff=s4, age=40)
        p6.save()
        p7 = Patient(name="Gai", address="Ladprao, Bangkok, Thailand", phone_number="0878901234", department=d2,
                     staff=s4, age=35)
        p7.save()
        p8 = Patient(name="Hong", address="Huai Khwang, Bangkok, Thailand", phone_number="0889012345", department=d2,
                     staff=s4, age=30)
        p8.save()
        p9 = Patient(name="In", address="Ratchathewi, Bangkok, Thailand", phone_number="0890123456", department=d2,
                     staff=s4, age=25)
        p9.save()
        p10 = Patient(name="Jai", address="Sathon, Bangkok, Thailand", phone_number="0901234567", department=d2,
                      staff=s4, age=20)
        p10.save()

        # Create three empty rooms per department
        r1 = Room(department=d1, room_number=101, patient=p1)
        r1.save()
        r2 = Room(department=d1, room_number=102, patient=p2)
        r2.save()
        r3 = Room(department=d1, room_number=103)
        r3.save()
        r4 = Room(department=d2, room_number=201, patient=p6)
        r4.save()
        r5 = Room(department=d2, room_number=202, patient=p7)
        r5.save()
        r6 = Room(department=d2, room_number=203)
        r6.save()

        # Create 10 accounting records that date from today to back 1 year
        from datetime import datetime, timedelta
        a1 = Accounting(balance=1000, date=datetime.now(), hospital=h, patient=p1)
        a1.save()
        a2 = Accounting(balance=2000, date=datetime.now() - timedelta(days=30, hours=1, minutes=15), hospital=h,
                        patient=p2)
        a2.save()
        a3 = Accounting(balance=3000, date=datetime.now() - timedelta(days=60, hours=2, minutes=30), hospital=h,
                        patient=p3)
        a3.save()
        a4 = Accounting(balance=4000, date=datetime.now() - timedelta(days=90, hours=3, minutes=45), hospital=h,
                        patient=p4)
        a4.save()
        a5 = Accounting(balance=5000, date=datetime.now() - timedelta(days=120, hours=4, minutes=0), hospital=h,
                        patient=p5)
        a5.save()
        a6 = Accounting(balance=6000, date=datetime.now() - timedelta(days=150, hours=5, minutes=15), hospital=h,
                        patient=p6)
        a6.save()
        a7 = Accounting(balance=7000, date=datetime.now() - timedelta(days=180, hours=6, minutes=30), hospital=h,
                        patient=p7)
        a7.save()
        a8 = Accounting(balance=8000, date=datetime.now() - timedelta(days=210, hours=7, minutes=45), hospital=h,
                        patient=p8)
        a8.save()
        a9 = Accounting(balance=9000, date=datetime.now() - timedelta(days=240, hours=8, minutes=0), hospital=h,
                        patient=p9)
        a9.save()
        a10 = Accounting(balance=10000, date=datetime.now() - timedelta(days=270, hours=9, minutes=15), hospital=h,
                         patient=p10)
        a10.save()
        a11 = Accounting(balance=-1500, date=datetime.now() - timedelta(days=20, hours=8, minutes=0), hospital=h)
        a11.save()
        a12 = Accounting(balance=-2500, date=datetime.now() - timedelta(days=46, hours=5, minutes=15), hospital=h)
        a12.save()
        a13 = Accounting(balance=-3500, date=datetime.now() - timedelta(days=95, hours=3, minutes=45), hospital=h)
        a13.save()
        a14 = Accounting(balance=-4500, date=datetime.now() - timedelta(days=122, hours=2, minutes=30), hospital=h)
        a14.save()
        a15 = Accounting(balance=-5500, date=datetime.now() - timedelta(days=156, hours=1, minutes=30), hospital=h)
        a15.save()

        # Create 5 appointments
        ap1 = Appointment(staff=s1, patient=p1, dateTime=datetime.now() + timedelta(days=1, hours=1, minutes=22),
                          detail="Follow-up checkup")
        ap1.save()
        ap2 = Appointment(staff=s1, patient=p2, dateTime=datetime.now() + timedelta(days=2, hours=3, minutes=53),
                          detail="Blood test")
        ap2.save()
        ap3 = Appointment(staff=s4, patient=p6, dateTime=datetime.now() + timedelta(days=3, hours=5, minutes=23),
                          detail="MRI scan")
        ap3.save()
        ap4 = Appointment(staff=s4, patient=p7, dateTime=datetime.now() + timedelta(days=4, hours=7, minutes=45),
                          detail="Medication refill")
        ap4.save()
        ap5 = Appointment(staff=s4, patient=p8, dateTime=datetime.now() + timedelta(days=5, hours=9, minutes=10),
                          detail="Physical therapy")
        ap5.save()

        # Create 20 medicines with real medicine names
        m1 = Medicine(name="Paracetamol", price=10, amount=100)  # Flu
        m1.save()
        m2 = Medicine(name="Ibuprofen", price=20, amount=100)
        m2.save()
        m3 = Medicine(name="Aspirin", price=30, amount=100)
        m3.save()
        m4 = Medicine(name="Amoxicillin", price=40, amount=100)  # Flu
        m4.save()
        m5 = Medicine(name="Ciprofloxacin", price=50, amount=100)  # Antibiotic
        m5.save()
        m6 = Medicine(name="Metronidazole", price=60, amount=100)  # Antibiotic
        m6.save()
        m7 = Medicine(name="Benralizumab", price=70, amount=100)  # Asthma
        m7.save()
        m8 = Medicine(name="Lansoprazole", price=80, amount=100)
        m8.save()
        m9 = Medicine(name="Simvastatin", price=90, amount=100)  # Hypertension
        m9.save()
        m10 = Medicine(name="Atorvastatin", price=100, amount=100)  # Diabete(New)
        m10.save()
        m11 = Medicine(name="Metformin", price=110, amount=100)  # Diabete
        m11.save()
        m12 = Medicine(name="Gliclazide", price=120, amount=100)  # Diabete (New)
        m12.save()
        m13 = Medicine(name="Amlodipine", price=130, amount=100)  # Hypertension(New)
        m13.save()
        m14 = Medicine(name="Losartan", price=140, amount=100)  # Hypertension(New)
        m14.save()
        m15 = Medicine(name="Bromhexine", price=150, amount=100)  # Flu
        m15.save()
        m16 = Medicine(name="Salbutamol", price=160, amount=100)  # Asthma(new)
        m16.save()
        m17 = Medicine(name="Prednisolone", price=170, amount=100)
        m17.save()
        m18 = Medicine(name="Levothyroxine", price=180, amount=100)
        m18.save()
        m19 = Medicine(name="Prenapril", price=190, amount=100)  # Alzhimer
        m19.save()
        m20 = Medicine(name="Brexpiprazole", price=200, amount=100)  # Alzhimer
        m20.save()

        # Create 3 diseases with real disease names
        d1 = Disease(name="Hypertension")  # internal
        d1.save()
        d2 = Disease(name="Diabete")  # internal
        d2.save()
        d3 = Disease(name="Asthma")  # internal
        d3.save()
        d4 = Disease(name="Alzhimer")  # neuro
        d4.save()
        d5 = Disease(name="Sundowner syndrome")  # neuro
        d5.save()
        d6 = Disease(name="Flu")  # internal
        d6.save()

        # patein dicise
        d1.patient.add(p6)  # Hypertension
        d2.patient.add(p7)  # Diabete
        d3.patient.add(p8)  # Asthma

        d4.patient.add(p1, p2, p3)  # Alzhimer neuro
        d5.patient.add(p4, p5)  # Sundowner syndrome neuro

        d6.patient.add(p9, p10)  # Flu

        # Create 5 prescriptions
        pr1 = Prescription(staff=s4, patient=p6)
        pr1.save()
        pr2 = Prescription(staff=s4, patient=p7)
        pr2.save()
        pr3 = Prescription(staff=s4, patient=p8)
        pr3.save()
        pr4 = Prescription(staff=s4, patient=p9)
        pr4.save()
        pr5 = Prescription(staff=s4, patient=p10)
        pr5.save()
        pr6 = Prescription(staff=s1, patient=p1)
        pr6.save()
        pr7 = Prescription(staff=s1, patient=p2)
        pr7.save()
        pr8 = Prescription(staff=s1, patient=p3)
        pr8.save()

        # Create 10 relation 
        pc1 = PrescriptionMedicine.objects.create(medicine=m9, prescription=pr1, amount=30)
        pc2 = PrescriptionMedicine.objects.create(medicine=m11, prescription=pr2, amount=90)
        pc3 = PrescriptionMedicine.objects.create(medicine=m7, prescription=pr3, amount=50)
        pc4 = PrescriptionMedicine.objects.create(medicine=m1, prescription=pr4, amount=21)
        pc5 = PrescriptionMedicine.objects.create(medicine=m4, prescription=pr4, amount=7)
        pc6 = PrescriptionMedicine.objects.create(medicine=m15, prescription=pr4, amount=20)
        pc7 = PrescriptionMedicine.objects.create(medicine=m1, prescription=pr5, amount=21)
        pc8 = PrescriptionMedicine.objects.create(medicine=m4, prescription=pr5, amount=7)
        pc9 = PrescriptionMedicine.objects.create(medicine=m15, prescription=pr5, amount=20)
        pc10 = PrescriptionMedicine.objects.create(medicine=m20, prescription=pr6, amount=21)
        pc11 = PrescriptionMedicine.objects.create(medicine=m19, prescription=pr6, amount=7)
        pc12 = PrescriptionMedicine.objects.create(medicine=m20, prescription=pr7, amount=20)
        pc13 = PrescriptionMedicine.objects.create(medicine=m19, prescription=pr7, amount=21)
        pc14 = PrescriptionMedicine.objects.create(medicine=m20, prescription=pr8, amount=20)
        pc15 = PrescriptionMedicine.objects.create(medicine=m19, prescription=pr8, amount=20)
