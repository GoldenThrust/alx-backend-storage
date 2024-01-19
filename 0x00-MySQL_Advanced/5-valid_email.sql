-- Create a trigger to reset valid_email only
-- when email is changed
DROP TRIGGER IF EXISTS valid_email;
DELIMITER ||
CREATE TRIGGER
    valid_email
BEFORE UPDATE ON
    users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    ELSE
        SET NEW.valid_email = 1;
    END IF;
END ||
DELIMITER ;