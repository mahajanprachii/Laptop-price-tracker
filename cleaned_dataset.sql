USE laptop_tracker;

SELECT * FROM laptops_clean;

ALTER TABLE laptops_clean
ADD COLUMN laptop_id INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE laptops_clean
DROP COLUMN Page,
DROP COLUMN Item_No;

DELETE FROM laptops_clean
WHERE Name = 'Not Found';

UPDATE laptops_clean
SET Name = TRIM(SUBSTRING_INDEX(Name,'Intel',1))
WHERE Name LIKE '%Intel%';

UPDATE laptops_clean
SET Name = TRIM(SUBSTRING_INDEX(Name,'AMD',1))
WHERE Name LIKE '%AMD%';

UPDATE laptops_clean
SET Name = TRIM(SUBSTRING_INDEX(Name,'Snapdragon',1))
WHERE Name LIKE '%Snapdragon%';

UPDATE laptops_clean
SET Name = TRIM(SUBSTRING_INDEX(Name,'MediaTek',1))
WHERE Name LIKE '%MediaTek%';

UPDATE laptops_clean
SET Name = TRIM(SUBSTRING_INDEX(Name,'with',1))
WHERE Name LIKE '%with%';

UPDATE laptops_clean
SET Name = TRIM(SUBSTRING_INDEX(Name,'Backlit',1))
WHERE Name LIKE '%Backlit%';


ALTER TABLE laptops_clean
RENAME COLUMN Reviews TO Total_Reviews;

UPDATE laptops_clean
SET Total_Reviews = REPLACE(Total_Reviews,' Ratings','');

UPDATE laptops_clean
SET Total_Reviews = NULL
WHERE Total_Reviews = 'Not Found';

UPDATE laptops_clean
SET Total_Reviews = REPLACE(Total_Reviews,',','');

ALTER TABLE laptops_clean
MODIFY COLUMN Total_Reviews INT;

ALTER TABLE laptops_clean
DROP COLUMN Image_URL;



ALTER TABLE laptops_clean
ADD COLUMN Processor VARCHAR(255),
ADD COLUMN RAM VARCHAR(100),
ADD COLUMN Operating_System VARCHAR(150),
ADD COLUMN Storage VARCHAR(100),
ADD COLUMN Display_Size VARCHAR(100),
ADD COLUMN Warranty VARCHAR(255);

UPDATE laptops_clean
SET Processor = TRIM(SUBSTRING_INDEX(Specifications,'|',1));

UPDATE laptops_clean
SET RAM = TRIM(
SUBSTRING_INDEX(
SUBSTRING_INDEX(Specifications,'|',2),
'|',
-1
));

UPDATE laptops_clean
SET Operating_System = TRIM(
SUBSTRING_INDEX(
SUBSTRING_INDEX(Specifications,'|',3),
'|',
-1
));

UPDATE laptops_clean
SET Storage = TRIM(
SUBSTRING_INDEX(
SUBSTRING_INDEX(Specifications,'|',4),
'|',
-1
));

UPDATE laptops_clean
SET Display_Size = TRIM(
SUBSTRING_INDEX(
SUBSTRING_INDEX(Specifications,'|',5),
'|',
-1
));

UPDATE laptops_clean
SET Warranty = TRIM(SUBSTRING_INDEX(Specifications,'|',-1));

UPDATE laptops_clean
SET Operating_System = REPLACE(Operating_System,' Operating System','');

UPDATE laptops_clean
SET Storage = NULL
WHERE Storage LIKE '%Display%';

ALTER TABLE laptops_clean
DROP COLUMN Display_Size;

ALTER TABLE laptops_clean
DROP COLUMN Specifications;

ALTER TABLE laptops_clean
DROP COLUMN Display_Size;

UPDATE laptops_clean
SET Operating_System = 'ChromeOS'
WHERE Operating_System = 'Chrome';

UPDATE laptops_clean
SET Operating_System = '64 bit ChromeOS'
WHERE Operating_System = '64 bit Chrome';

SELECT *
FROM laptops_clean
WHERE Operating_System LIKE 'Graphics%';

UPDATE laptops_clean
SET Operating_System = NULL
WHERE laptop_id = 310;

