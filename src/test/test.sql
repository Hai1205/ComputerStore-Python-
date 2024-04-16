-- Tạo cơ sở dữ liệu
CREATE DATABASE imgSQL
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Sử dụng cơ sở dữ liệu mới tạo
USE imgSQL;

-- Tạo bảng Product
CREATE TABLE Product (
    productID VARCHAR(15) PRIMARY KEY,
    supplierName VARCHAR(15),
    productName VARCHAR(50),
    type VARCHAR(50),
    quantity INT,
    warrantyTime INT,
    price INT,
    img BLOB
);