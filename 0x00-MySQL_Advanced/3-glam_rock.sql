-- List bands with Glam rock as their
-- main style, ranked by longevity
SELECT
    band_name,
    TIMESTAMPDIFF(YEAR, formed, IFNULL(split, '2022-01-01')) AS lifespan
FROM
    metal_bands
WHERE
    FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY
    lifespan DESC;