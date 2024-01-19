-- Creates a stored procedure ComputeAverageScoreForUser 
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score INT DEFAULT 0;
    DECLARE num_project INT DEFAULT 0;

    SELECT
        SUM(score), COUNT(*)
    INTO
        total_score, num_project
    FROM
        corrections
    WHERE
        user_id = user_id;


    UPDATE users
        SET average_score = IF(num_project = 0, 0, total_score / num_project)
        WHERE id = user_id;
END $$
DELIMITER ;