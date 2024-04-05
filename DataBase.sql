-- Tạo cơ sở dữ liệu
CREATE DATABASE ComputerStore
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Sử dụng cơ sở dữ liệu mới tạo
USE ComputerStore;

-- Tạo bảng Supplier
CREATE TABLE Supplier (
    supplierID VARCHAR(15) PRIMARY KEY,
    supplierName VARCHAR(100)
);

-- Tạo bảng Employee
CREATE TABLE Employee (
    employeeID VARCHAR(15) PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    DOB DATE,
    position VARCHAR(15),
    salary INT
);

-- Tạo bảng Customer
CREATE TABLE Customer (
    customerID VARCHAR(15) PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    address VARCHAR(100),
    phone VARCHAR(20)
);

-- Tạo bảng Account
CREATE TABLE Account (
    customerID VARCHAR(15),
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50)
);

-- Tạo bảng Product
CREATE TABLE Product (
    productID VARCHAR(15) PRIMARY KEY,
    supplierName VARCHAR(15),
    productName VARCHAR(50),
    type VARCHAR(50),
    quantity INT,
    warrantyTime INT,
    price INT
);

-- Tạo bảng ProductDetail
CREATE TABLE ProductDetail (
    productID VARCHAR(15) PRIMARY KEY,
    MFG VARCHAR(10),
    RAM VARCHAR(50),
    ROM VARCHAR(50),
    CPU VARCHAR(100),
    VGA VARCHAR(100),
    keyboard VARCHAR(50),
    screen VARCHAR(50),
    OS VARCHAR(50),
    size VARCHAR(50),
    pin VARCHAR(50),
    capacity VARCHAR(50),
    SPDspeed VARCHAR(50),
    CL VARCHAR(50),
    layout VARCHAR(50),
    LED VARCHAR(50),
    keycap VARCHAR(50),
    switch VARCHAR(50),
    hotswap VARCHAR(3),
    writeSpeed VARCHAR(50),
    readSpeed VARCHAR(50),
    scan VARCHAR(50),
    panel VARCHAR(50),
    resolution VARCHAR(50),
    cores INT,
    threads INT,
    series VARCHAR(50),
    GPUclock VARCHAR(50),
    type VARCHAR(50)
);

-- Tạo bảng Invoice
CREATE TABLE Invoice (
    invoiceID VARCHAR(15) PRIMARY KEY,
    employeeID VARCHAR(15),
    customerID VARCHAR(15),
    date DATE,
    totalCost INT
);

-- Tạo bảng InvoiceDetail
CREATE TABLE InvoiceDetail (
    invoiceID VARCHAR(15),
    productID VARCHAR(15),
    warrantyID VARCHAR(15),
    quantity INT,
    price INT,
    cost INT,
    PRIMARY KEY (invoiceID, productID, warrantyID)
);

-- Tạo bảng Warranty
CREATE TABLE Warranty (
    warrantyID VARCHAR(15) PRIMARY KEY,
    productID VARCHAR(15),
    invoiceID VARCHAR(15),
    customerID VARCHAR(15),
    purchaseDate DATE,
    EXP DATE,
    warrantyTime INT
);

-- Tạo bảng Import
CREATE TABLE Import (
    importID VARCHAR(15) PRIMARY KEY,
    employeeID VARCHAR(15),
    supplierID VARCHAR(15),
    date DATE,
    totalCost INT
);

-- Tạo bảng ImportDetail
CREATE TABLE ImportDetail (
    importID VARCHAR(15),
    productID VARCHAR(15),
    quantity INT,
    price INT,
    cost INT
    -- PRIMARY KEY (importID, productID)
);
