-- creates a stored procedure ComputeAverageWeightedScoreForUser
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER ||
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
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
END ||
DELIMITER ;