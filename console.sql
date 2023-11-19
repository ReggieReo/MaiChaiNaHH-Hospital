-- 1 room
SELECT p.*
FROM db_patient as p
JOIN db_room as r ON p.id = r.patient_id
WHERE r.room_number = 101;

-- 2 staff
SELECT p.*, s.name
FROM db_staff as s
         JOIN db_patient as p ON s.id = p.staff_id
where exists (
    select 1
    from db_role as r
    where s.role_id = r.id
) and s.name like '%sak%';


-- 2 name
SELECT p.*
from db_patient as p
where p.name like '%%';


-- 3. search patient by each department
SELECT p.name, d.name
FROM db_patient as p
JOIN db_department as d ON d.id = p.department_id
WHERE d.name like '%neu%';

-- 4. search patient with specific disease
SELECT p.*
FROM db_Patient as p
JOIN db_disease_patient as pd on p.id = pd.patient_id
JOIN db_Disease as d on pd.disease_ID = d.id
WHERE d.name like '%dia%';

SELECT SUM(a.balance) AS Total
FROM db_accounting as a
WHERE a.date >= '2023-05-23 00:01:24.863937'and
    a.date <= '2023-11-19 06:31:24.860249';