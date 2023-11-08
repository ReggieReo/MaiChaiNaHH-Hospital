from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)


class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Role(models.Model):
    name = models.CharField(max_length=255)


class Staff(models.Model):
    name = models.CharField(Role, max_length=255)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Room(models.Model):
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    room_number = models.IntegerField()


class Patient(models.Model):
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    age = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)


class Accounting(models.Model):
    balance = models.FloatField()
    date = models.DateTimeField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Appointment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    detail = models.CharField(max_length=255)


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    amount = models.IntegerField()


class Precription(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)


class Disease(models.Model):
    name = models.CharField(max_length=255)
    patient = models.ManyToManyField(Patient)


class Treatment(models.Model):
    name = models.CharField(max_length=255)
    disease = models.ManyToManyField(Disease)
    patience = models.ManyToManyField(Patient)
