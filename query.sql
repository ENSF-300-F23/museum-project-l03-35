-- 1
SELECT table_name FROM information_schema.tables WHERE table_schema = 'ArtCollection';


SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME, 
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM
    information_schema.KEY_COLUMN_USAGE
WHERE
    REFERENCED_TABLE_SCHEMA = 'ArtCollection'
    AND REFERENCED_TABLE_NAME IS NOT NULL;

-- 2

SELECT * FROM Artists;

-- 3

SELECT * FROM Artworks ORDER BY CreationYear;

-- 4

SELECT * FROM Artworks WHERE CreationYear < (SELECT YEAR('1801-01-01'));

-- 5

SELECT Artworks.Title, Artists.Name, Artworks.CreationYear 
FROM Artworks 
JOIN Artists ON Artworks.ArtistID = Artists.ArtistID;

-- 6


DELIMITER //

CREATE PROCEDURE AddOldBirthYearColumn()
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'Artists'
        AND COLUMN_NAME = 'OldBirthYear'
    ) THEN
        ALTER TABLE Artists
        ADD COLUMN OldBirthYear INT;
    END IF;
END;

//
DELIMITER ;


CALL AddOldBirthYearColumn();


DROP TRIGGER IF EXISTS ArtistBirthYearUpdate;


DELIMITER //

CREATE TRIGGER ArtistBirthYearUpdate
BEFORE UPDATE ON Artists
FOR EACH ROW
BEGIN
    IF OLD.BirthYear <> NEW.BirthYear THEN
        SET NEW.OldBirthYear = OLD.BirthYear;
    END IF;
END;

//
DELIMITER ;


-- 7

DELIMITER //
DROP TRIGGER IF EXISTS DeleteArtistOnStatusUpdate;
CREATE TRIGGER DeleteArtistOnStatusUpdate
AFTER UPDATE ON Artworks
FOR EACH ROW
BEGIN
    
    IF NEW.Status = 'DeleteArtist' THEN
        
        DELETE FROM Artists WHERE ArtistID = NEW.ArtistID;
    END IF;
END;

//
DELIMITER ;


INSERT INTO Artists (ArtistID, Name, BirthYear, Nationality) VALUES (20, 'Sample Artist', 1980, 'Nationality');


UPDATE Artworks SET Status = 'DeleteArtist' WHERE ArtistID = 20;






