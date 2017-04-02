Table A: p_table.csv
This file contains information about the album reviews from pitchfork data set in CSV format. It has 
18391 rows and 4 columns. The first row is the header followed followed by rows containing
album information. The columns include information such as title (album name), artist and year (album release), 
Each row is uniquely identified by the 'reviewid' column.

Table B: d_table.csv
This file contains information about the album reviews from discogs data set in CSV format. It has 
466936 rows and 4 columns. The first row is the header followed followed by rows containing
album information. The columns include information such as title (album name), artist and year (album release), 
Each row is uniquely identified by the 'id' column.

Table C: tuples_after_blocking.csv
These are the remaining tuples after applying overlap blocker and attribute equivalence blocker to the column'title'.
There are 7682 tuples remaining.

Table G: labeled_tuples.csv
3000 tuples sampled from Table C and labeled as match (1), non-match (0). There are 2075 positive examples and
925 negative ones.

Sets I and J: set_I.csv, set_j.csv
Splitted G such that 1800 examples in development set I and 1200 in test set J. Both I and J are converted to tables H, K 
respectively and all missing values are filled.