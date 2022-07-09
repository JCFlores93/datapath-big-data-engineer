-- Crear una bd
sqlite3 test.db

-- Listar bds
.databases

-- Listar tablas
.tables

-- Create table Company
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);