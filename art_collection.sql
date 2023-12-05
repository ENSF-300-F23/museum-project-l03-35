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
(56789, 'Donatello', 1386, 'Italian'),
(47283, 'Hieronymus Bosch', 1450, 'Dutch'),
(47123, 'Caravaggio', 1571, 'Italian'),
(81731, 'Denis Foyatier', 1793, 'French'),
(71321, 'Grego Erhart', 1470, 'German'),
(14236, 'Antonio Canova', 1757, 'Italian');


INSERT INTO Artworks (Title, ArtistID, CreationYear, Medium, CollectionName, Category, Status) 
VALUES 
('Mona Lisa', 12345, 1503, 'Oil on wood panel','MASTERPIECES OF THE LOUVRE' ,'Painting', 'Borrowed'),
('The Lacemaker', 23456, 1670, 'Oil on canvas','MASTERPIECES OF THE LOUVRE' , 'Painting', 'Borrowed'),
('Starry Night', 34567, 1889, 'Oil on canvas','MASTERPIECES OF THE LOUVRE' , 'Painting', 'Borrowed'),
('The Thinker', 45678, 1902, 'Bronze','NATIONAL MUSEUMS RECOVERY' , 'Sculpture', 'Borrowed'),
('Venus de Milo', 56789, 100, 'Marble', 'NATIONAL MUSEUMS RECOVERY' ,'Sculpture', 'Borrowed'),
('David', 56789, 1504, 'Marble', 'NATIONAL MUSEUMS RECOVERY' ,'Sculpture', 'Borrowed'),
('Ship of Fools', 47283, 1490, 'Oil on Wood', 'DRAWINGS & ENGRAVINGS', 'Painting', 'Owned'),
('Death of the Virgin', 47123, 1605, 'Oil on Canvas', 'DRAWINGS & ENGRAVINGS', 'Painting', 'Owned'),
('Portrait of Alof de Wignacourt and his Page', 47123, 1607, 'Oil on Canvas', 'DRAWINGS & ENGRAVINGS', 'Painting', 'Owned'),
('Spartacus', 81731, 1827, 'Carrara Marble', 'SCULPTURES', 'Sculpture', 'Owned'),
('Saint Mary Magdalene', 71321, 1515, 'Lindenwood and Polychrome', 'SCULPTURES', 'Sculpture', 'Owned'),
('Pysche Revived by Cupids Kiss', 14236, 1787, 'Marbe', 'SCULPTURES', 'Sculpture', 'Owned');


