-- Rank country origins of bands by the number of (non-unique) fans
SELECT
    origin,
    COUNT(fans) AS nb_fans
FROM
    band_fans
GROUP BY
    origin
ORDER BY
    nb_fans DESC;