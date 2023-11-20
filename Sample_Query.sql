-- Sample Query that based on slide, but usable with sqlite3 of this django application with sample data.
-- So all queries in this sample file are a little difference from the one in the slide,
-- but they produce the same result.

--Patient
--1 Search patient by name
SELECT p.*
from db_patient as p
where p.name like '%<patient_name>%';

--2 Search patient by staff’s name
SELECT p.name, s.name
FROM db_staff as s
         JOIN db_patient as p ON s.id = p.staff_id
where s.name like '%<staff_name>%';

--3 Search patient by department
SELECT p.*
from db_patient as p
         join db_department as d on d.id = p.department_id
where p.name like '%<department_name>%';

--4 Search patient by disease
SELECT p.*
FROM db_patient as p
         JOIN db_disease_patient as dp on p.id = dp.patient_id
         JOIN db_disease as d on dp.disease_id = d.id
WHERE d.name like '%<disease_name>%';

--5
SELECT p.*
FROM db_patient as p
         JOIN db_room as r ON p.id = r.patient_id
WHERE r.room_number = '<room_number>';


--6 Update patient
UPDATE db_patient
SET name          = '<new_name>',
    department_id = '<new_department>',
    staff_id      = '<new_staff>',
    age           = '<new_age>',
    address       = '<new_address>',
    phone_number  = '<new_phoneNumber>'
WHERE id = '<patient_id>';

--7 Delete patient by ID
DELETE
from db_patient
WHERE id = '<patient_id>';


-- Staff
-- 1 Search staff by name
SELECT s.*
from db_staff as s
where s.name like '%<staff_name>%';

--2 Search staff by department
SELECT s.name as 'Staff''s name', d.name as 'Department''s name'
FROM db_staff as s
         Join db_department as d
              on d.id = s.department_id
where d.name like
      '%<department_name>%';

--3 Search staff by role
SELECT s.*
from db_staff as s
         Join db_role as r on r.id = s.role_id
where r.name like '%<role_name>%';

--4 Delete staff by ID
DELETE
FROM db_staff
WHERE id = '<staff_id>';

--5 Update staff
UPDATE db_staff
SET name          = '<new_name>',
    department_id = '<new_department>',
    role_id       = '<new_role>'
WHERE id = '<staff_id>';

--Medicine
-- 1. Search medicine by name
SELECT m.*
from db_medicine as m
where m.name like '%<medicine_name>%';

-- 2. Delete medicine by ID
DELETE
from db_medicine
where id = '<medicine_id>';

-- 3. Update medicine
UPDATE db_medicine
SET name   = '<medicine_name>',
    price  = '<price>',
    amount = '<amount>'
where id = '<medicine_id>';

--Disease

-- 1. Search disease by name
SELECT d.*
from db_disease as d
where d.name like '%<disease_name>%';

-- 2. Search disease by patient‘s name
SELECT d.*, p.name
from db_disease as d
         Join db_disease_patient as pd on pd.disease_ID = d.id
         Join db_patient as p on p.ID = pd.patient_ID
where p.Name like '%<patient_name%';

-- 3. Delete disease by ID
DELETE
from db_disease
where id = '<disease_id>';

-- 4. Update disease
UPDATE db_disease
SET name = '<disease_name>'
where id = '<disease_id>';

-- Appointment

-- 1. Search appointment by date
SELECT *
FROM db_appointment
WHERE dateTime >= '<start_date>' AND
dateTime < '<end_date>';

-- 2. Search appointment by appointee‘s name
SELECT p.name, ap.*
FROM db_appointment as ap
JOIN db_patient as p on ap.patient_ID = p.id
WHERE p.Name like '%<patient_name>%';

-- 3. Delete appointment
DELETE from db_appointment
WHERE ID = '<appointment_id>';

-- 4. Update appointment
UPDATE db_appointment
SET dateTime = '<new_date>',
    detail = '<update_detail>',
    patient_id = '<new_patient>',
    staff_id = '<new_staff>'
WHERE id = '<appointment>';

-- ACCOUNTING
-- 1.Search accounting by date
SELECT *
FROM db_accounting
WHERE date >= '<start_date>' AND
      date <= '<end_date>';

-- 2.Search accounting by payer‘s name
SELECT p.name, ac.*
FROM db_accounting as ac
JOIN db_patient as p on ac.patient_ID = p.ID
WHERE p.Name like '%%';

-- 3.sum balance of Accounting by a given date range
SELECT SUM(ac.balance) AS Total
FROM db_Accounting as ac
WHERE date >= '<start_date>' AND
      date <= '<end_date>';

-- Prescription
-- 1. Search prescription by staff‘s name
SELECT s.name, pc.*
from db_prescription as pc
Join db_staff as s on s.ID = pc.staff_ID
where s.Name like '%Dr.%';

-- 2. Search prescription by patient’s name
SELECT p.Name, pc.*
from db_prescription as pc
Join db_patient as p on p.ID = pc.patient_ID
where p.Name like '%<patient_name>%';

-- 3. Delete prescription by ID
DELETE from db_prescription
where ID = 1;

-- 4. Update prescription
UPDATE db_prescription
SET staff_ID = '<new_staff_id>', patient_ID = '<new_patient_id>'
where ID = '<prescription_id>';

-- 5. Search prescription by contains medicine
SELECT pc.*, m.name
from db_prescription as pc
join db_prescriptionmedicine as pm on
                             pc.ID = pm.prescription_ID
join db_medicine as m on
                   m.ID = pm.medicine_ID
where m.Name like '%<medicine_name>%';