from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)


class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(Role, max_length=255)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Room(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    patient = models.OneToOneField(Patient, null=True, on_delete=models.SET_NULL)


class Accounting(models.Model):
    balance = models.FloatField()
    date = models.DateTimeField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)


class Appointment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    detail = models.CharField(max_length=255)


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    amount = models.IntegerField()


class Prescription(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class PrescriptionMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.medicine.name} {self.amount} units"

    def __repr__(self):
        return f"{self.medicine.name} {self.amount} units"


class Disease(models.Model):
    name = models.CharField(max_length=255)
    patient = models.ManyToManyField(Patient)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Treatment(models.Model):
    name = models.CharField(max_length=255)
    disease = models.ManyToManyField(Disease)
    patience = models.ManyToManyField(Patient)
