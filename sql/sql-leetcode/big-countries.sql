-- https://leetcode.com/problems/big-countries/
-- https://leetcode.com/submissions/detail/829917662/
SELECT name, population, area FROM World 
WHERE area >= 3000000 or population >= 25000000