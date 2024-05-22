CREATE DATABASE FruitBasket:

USE FruitBasket:

CREATE TABLE Fruits (ID INT PRIMARY KEY, Name VARCHAR(50),Color VARCHAR(20)):

INSERT INTO Fruits (Назва_фрукта, Колір) VALUES
('Яблуко', 'Червоне'),
('Банан', 'Жовтий'),
('Апельсин', 'Помаранчевий');

UPDATE Fruits SET Колір = 'Зелене' WHERE Назва_фрукта = 'Яблуко';

SELECT * FROM Fruits WHERE Колір = 'Жовтий';

SELECT * FROM Fruits;

