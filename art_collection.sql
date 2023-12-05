DROP DATABASE IF EXISTS ArtCollection;

CREATE DATABASE ArtCollection;

USE ArtCollection;

DROP TABLE IF EXISTS Artists;

CREATE TABLE Artists (
  ArtistID INT NOT NULL PRIMARY KEY,
  Name VARCHAR(255) NOT NULL,
  BirthYear INT,
  Nationality VARCHAR(100)
);

DROP TABLE IF EXISTS Artworks;

CREATE TABLE Artworks (
  ArtworkID INT AUTO_INCREMENT PRIMARY KEY,
  Title VARCHAR(255) NOT NULL,
  ArtistID INT,
  CreationYear INT,
  Medium VARCHAR(255),
  CollectionName VARCHAR(255),
  Category VARCHAR(50),
  Status VARCHAR(100),
  FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID)
);

INSERT INTO Artists (ArtistID, Name, BirthYear, Nationality) VALUES 
(12345, 'Leonardo da Vinci', 1452, 'Italian'),
(23456, 'Johannes Vermeer', 1632, 'Dutch'),
(34567, 'Vincent van Gogh', 1853, 'Dutch'),
(45678, 'Auguste Rodin', 1840, 'French'),
(56789, 'Donatello', 1386, 'Italian');

INSERT INTO Artworks (Title, ArtistID, CreationYear, Medium, CollectionName, Category, Status) 
VALUES 
('Mona Lisa', 12345, 1503, 'Oil on wood panel','MASTERPIECES OF THE LOUVRE' ,'Painting', 'Borrowed'),
('The Lacemaker', 23456, 1670, 'Oil on canvas','MASTERPIECES OF THE LOUVRE' , 'Painting', 'Borrowed'),
('Starry Night', 34567, 1889, 'Oil on canvas','MASTERPIECES OF THE LOUVRE' , 'Painting', 'Borrowed'),
('The Thinker', 45678, 1902, 'Bronze','NATIONAL MUSEUMS RECOVERY' , 'Sculpture', 'Borrowed'),
('Venus de Milo', 56789, 100, 'Marble', 'NATIONAL MUSEUMS RECOVERY' ,'Sculpture', 'Borrowed'),
('David', 56789, 1504, 'Marble', 'NATIONAL MUSEUMS RECOVERY' ,'Sculpture', 'Borrowed');
