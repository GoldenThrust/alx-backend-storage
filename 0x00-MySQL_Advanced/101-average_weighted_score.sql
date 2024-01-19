-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER ||
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE user_id INT;

    DECLARE user_cursor CURSOR FOR
    SELECT id FROM users;
    
    OPEN user_cursor;

    FETCH user_cursor INTO user_id;

    WHILE user_id IS NOT NULL DO
        DECLARE total_weighted_score INT;
        DECLARE total_weight INT;

        SELECT 
            SUM(c.score * p.weight),
            SUM(p.weight)
        INTO 
            total_weighted_score,
            total_weight
        FROM 
            corrections c
        JOIN 
            projects p ON c.project_id = p.id
        WHERE 
            c.user_id = user_id;

        UPDATE 
            users
        SET 
            average_score = IFNULL(total_weighted_score / NULLIF(total_weight, 0), 0)
        WHERE 
            id = user_id;

        -- Fetch the next user_id
        FETCH user_cursor INTO user_id;
    END WHILE;

    CLOSE user_cursor;
END ||
DELIMITER ;