USE ComputerStore;

-- DEMO INSERT
INSERT INTO account (customerID, username, password)
VALUES ('admin', 'admin', '123');

INSERT INTO account (customerID, username, password)
VALUES ('CTM0000000001', 'panda', '1205');

INSERT INTO customer (customerID, firstname, lastname, address, phone)
VALUES ('CTM0000000001', 'Nguyen Hoang', 'Hai', 'Sai Gon', '0782748863');

INSERT INTO employee (employeeID, firstname, lastname, DOB, position, salary)
VALUES ('EP0000000001', 'Nguyen Van', 'Hieu', NULL, 'Sale', 500);

INSERT INTO supplier (supplierID, supplierName)
VALUES ('SP0000000001', 'Asus');

INSERT INTO product (productID, productName, type, quantity, warrantyTime, price)
VALUES ('PD0000000001', 'VivoBook 14 OLED M1405YA KM047W', 'Laptop', 50, 24, 525);

INSERT INTO productdetail (productID, supplierID, MFG, RAM, ROM, CPU, VGA, keyboard, screen, OS, size, pin, type)
VALUES ('PD0000000001', 'SP0000000001', '2023', '8GB', '512GB', 'Ryzen™ 5 7530U', 'AMD Radeon™ Graphics', 'Chiclet Keyboard', 'OLED', 'Windows 11 Home', '31.71 x 22.20 x 1.99', '50WHrs', 'Gaming');

INSERT INTO import (importID, employeeID, supplierID, date, totalCost)
VALUES ('IP0000000001', 'EP0000000001', 'SP0000000001', '2024-03-26', 25000);

INSERT INTO importdetail (importID, productID, quantity, price, cost)
VALUES ('IP0000000001', 'PD0000000001', 50, 500, 25000);

INSERT INTO invoice (invoiceID, employeeID, customerID, date, totalCost)
VALUES ('IV0000000001', 'EP0000000001', 'CTM0000000001', '2024-03-26', 525);

INSERT INTO invoicedetail (invoiceID, productID, warrantyID, quantity, price, cost)
VALUES ('IV0000000001', 'PD0000000001', 'WRT0000000001', 1, 525, 525);

INSERT INTO warranty (warrantyID, productID, invoiceID, customerID, purchaseDate, warrantyTime, EXP)
VALUES ('WRT0000000001', 'PD0000000001', 'IV0000000001', 'CTM0000000001', '2024-03-26', 24, '2026-03-26');

-- DEMO LOGIN
SELECT customerID FROM account WHERE username LIKE 'panda' AND password LIKE '1205';

-- DEMO ADD TO CART
UPDATE customer SET cart = 'PD0000000001, PD0000000002, PD0000000003, PD0000000004, PD0000000005' WHERE customerID = 'CTM0000000001';

-- DEMO UPDATE
UPDATE account SET password = '12052004' WHERE username = 'panda';

UPDATE customer SET firstname = '{firstname}', lastname = '{lastname}', address = '{address}', phone = '{phone}' WHERE customerID = 'CTM0000000001';

UPDATE employee SET firstname = '{firstname}', lastname = '{lastname}', DOB = '{DOB}', position = '{position}', salary = 0 WHERE employeeID = 'EP0000000001';

UPDATE import SET date = '{date}' WHERE importID = 'IP0000000001';

UPDATE invoice SET date = '{date}' WHERE invoiceID = 'IV0000000001';

UPDATE product SET productName = '{productName}', type = '{type}', quantity = 0, warrantyTime = 0, price = 0 WHERE productID = 'PD0000000001';

UPDATE productdetail SET MFG = '{MFG}', RAM = '{RAM}', ROM = '{ROM}', CPU = '{CPU}', VGA = '{VGA}', keyboard = '{keyboard}', screen = '{screen}', OS = '{OS}', size = '{size}', pin = '{pin}', type = '{type}' WHERE productID = 'PD0000000001';

UPDATE supplier SET supplierName = '{supplierName}' WHERE supplierID = 'SP0000000001';

UPDATE warranty SET purchaseDate = '{purchaseDate}', warrantyTime = 1, EXP = '{EXP}' WHERE warrantyID = 'WRT0000000001';

-- DEMO DELETE
DELETE FROM account WHERE username = 'panda';

DELETE FROM customer WHERE customerID = 'CTM0000000001';

DELETE FROM employee WHERE employeeID = 'EP0000000001';

DELETE FROM import WHERE importID = 'IP0000000001';

DELETE FROM importdetail WHERE importID = 'IP0000000001';

DELETE FROM invoice WHERE invoiceID = 'IV0000000001';

DELETE FROM invoicedetail WHERE invoiceID = 'IV0000000001';

DELETE FROM product WHERE productID = 'PD0000000001';

DELETE FROM productdetail WHERE productID = 'PD0000000001';

DELETE FROM supplier WHERE supplierID = 'SP0000000001';

DELETE FROM warranty WHERE warrantyID = 'WRT0000000001';