-- https://leetcode.com/problems/swap-salary/
-- https://leetcode.com/submissions/detail/830678621/
UPDATE Salary 
SET sex = CASE
    WHEN sex = "f"
    THEN "m"
    WHEN sex = "m"
    THEN "f"
    END