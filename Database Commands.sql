import sqlite3

CREATE TABLE IF NOT EXISTS BookManagementTable (TITLE, AUTHOR, PBLICATION_DATE, PRICE_PER_UNIT, QUANTITY, EDITION_DATE, EDITOR, SUPPLIER);
CREATE TABLE IF NOT EXISTS EditorManagementTable (COMPANY_NAME, LOCATION, PHONE_NUMBER, EMAIL, EDITION_DATE);
CREATE TABLE IF NOT EXISTS AuthorManagementTable (NAME, GENDER, AGE);
CREATE TABLE IF NOT EXISTS SupplierManagementTable (NAME, LOCATION, PHONE_NUMBER, EMAIL);

INSERT INTO `BookManagementTable` (`TITLE`, `AUTHOR`, `PBLICATION_DATE`, `PRICE_PER_UNIT`, `QUANTITY`, `EDITION_DATE`, `EDITOR`, `SUPPLIER`) VALUES
('Legend', 'John', '2021-01-15 21:41:00', '10000', '100', '2021-01-15 21:41:00', 'kings', 'CamBooks'),
('Dawn', 'Mary', '2021-02-15 21:41:00', '20000', '200', '2021-02-15 21:41:00', 'kings', 'CamBooks'),
('Break', 'Ronan', '2021-03-15 21:41:00', '30000', '300', '2021-03-15 21:41:00', 'kings', 'CamBooks'),
('Season', 'Rodney', '2021-04-15 21:41:00', '40000', '400', '2021-04-15 21:41:00', 'kings', 'CamBooks'),
('Sun', 'Sidney', '2021-05-15 21:41:00', '50000', '500', '2021-05-15 21:41:00', 'kings', 'CamBooks'),
('Day', 'Melany', '2021-06-15 21:41:00', '60000', '600', '2021-06-15 21:41:00', 'kings', 'CamBooks'),
('Night', 'Kerry', '2021-07-15 21:41:00', '70000', '700', '2021-07-15 21:41:00', 'kings', 'CamBooks'),
('Morning', 'Hannah', '2021-08-15 21:41:00', '80000', '800', '2021-08-15 21:41:00', 'kings', 'CamBooks'),
('Time', 'Calson', '2021-09-15 21:41:00', '90000', '900', '2021-09-15 21:41:00', 'kings', 'CamBooks'),
('Chronos', 'Sam', '2021-10-15 21:41:00', '95000', '950', '2021-10-15 21:41:00', 'kings', 'CamBooks');

INSERT INTO `EditorManagementTable` (`COMPANY_NAME`, `LOCATION`, `PHONE_NUMBER`, `EMAIL`, `EDITION_DATE`) VALUES
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/01/2020'),
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/02/2020'),
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/03/2020'),
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/04/2020'),
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/05/2020'),
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/06/2020'),
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/07/2020'),
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/08/2020'),
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/09/2020'),
('Maxx', 'Yaounde', '623458912', 'maxx@gmail.com', '15/10/2020');

INSERT INTO `SupplierManagementTable` (`NAME`, `LOCATION`, `PHONE_NUMBER`, `EMAIL`) VALUES
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com'),
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com'),
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com'),
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com'),
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com'),
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com'),
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com'),
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com'),
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com'),
('GenBooks', 'Yaounde', '665894123', 'genbooks@gmail.com');

