/* Write your T-SQL query statement below */
Select score, dense_rank() OVER (order by score desc) as Rank 
From Scores
Order by Score Desc
