--SQLite script for creating CSV from pitchfork_reviews dataset:
--First, open the sqlite database (sqlite3 Pitchfork.sqlite)
--Combine multiple years for the same album using slashes (for example, "1971/2005")
CREATE TABLE years_combined AS
SELECT reviewid, GROUP_CONCAT(year, '/') AS year
FROM (
   SELECT reviewid, year
   FROM years
   ORDER BY reviewid, year
   )
GROUP BY reviewid;
--Combine multiple genres for the same album using slashes (for example, "jazz/rock")
CREATE TABLE genres_combined AS
SELECT reviewid, GROUP_CONCAT(genre, '/') AS genre
FROM (
   SELECT reviewid, genre
   FROM genres
   ORDER BY reviewid, genre
   )
GROUP BY reviewid;
--Combine multiple genres for the same album using slashes (for example, "interscope/nothing")
CREATE TABLE labels_combined AS
SELECT reviewid, GROUP_CONCAT(label, '/') AS label
FROM (
   SELECT reviewid, label
   FROM labels
   ORDER BY reviewid, label
   )
GROUP BY reviewid;
--Now, combine all of the relevant data into a single table
CREATE TABLE pitchfork_reviews AS
SELECT reviews.reviewid,
       reviews.title,
       reviews.artist,
       labels_combined.label,
       reviews.pub_year,
       years_combined.year,
       genres_combined.genre,
       reviews.score,
       reviews.best_new_music
FROM reviews
JOIN years_combined ON reviews.reviewid = years_combined.reviewid
JOIN genres_combined ON reviews.reviewid = genres_combined.reviewid
JOIN labels_combined ON reviews.reviewid = labels_combined.reviewid;
.quit
--Now that these tables are in the database, you can output the new table to a CSV via the following command:
--sqlite3 -header -csv Pitchfork.sqlite "SELECT * FROM pitchfork_reviews ORDER BY reviewid;" > pitchfork_reviews.csv