* Hospital(__hospitalID__, name, address, phoneNumber)

* Department(__departmentID__, hospital, name)

* Role(__roleID__, role)

* Staff(__staffID__, name, role, department)

* Room(__roomNumber__, department)

* Patient(__patientID__, name, address, phoneNumber, department, staff, age, room)

* Accounting(__accountingID__, balance, date, hospital, patient)

* Appointment(__appointmentID__, staff, patient, date, detail)

* Medicine(__medID__, name, price, amount)

* Prescription(__prescriptionID__, patient, staff)

Prescription contains Medicine
* PrescriptionMedicine(__prescriptionID__, __medID__, amount)

* Disease(__diseaseID__, name)

* Treatment(__treatmentID__, name)

one patient can have many PatientDisease
* PatientDisease(__patientID__, __diseaseID__)

Disease can have multiple Treatment
* DiseaseTreatment(__diseaseID__, __treatmentID__)

Patient can recieve multiple Treatment
* PatientTreatment(__patientID__, __treatmentID__)