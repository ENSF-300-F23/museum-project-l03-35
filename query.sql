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

CREATE TRIGGER LogArtistNameChange AFTER UPDATE ON Artists FOR EACH ROW
BEGIN
    IF OLD.Name <> NEW.Name THEN
        INSERT INTO ArtistNameChangeLog (ArtistID, OldName, NewName)
        VALUES (NEW.ArtistID, OLD.Name, NEW.Name);
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
    -- Check if the Status column is updated to a specific value (e.g., 'DeleteArtist')
    IF NEW.Status = 'DeleteArtist' THEN
        -- Delete the artist record with the corresponding ArtistID
        DELETE FROM Artists WHERE ArtistID = NEW.ArtistID;
    END IF;
END;

//
DELIMITER ;


INSERT INTO Artists (ArtistID, Name, BirthYear, Nationality) VALUES (20, 'Sample Artist', 1980, 'Nationality');


UPDATE Artworks SET Status = 'DeleteArtist' WHERE ArtistID = 20;






