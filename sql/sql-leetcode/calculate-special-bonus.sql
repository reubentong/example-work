-- https://leetcode.com/problems/calculate-special-bonus/
-- https://leetcode.com/submissions/detail/830675054/
SELECT employee_id, CASE 
    WHEN employee_id %2 != 0 
    AND name NOT LIKE 'M%'
    THEN salary
    ELSE 0
    END as bonus
FROM Employees order by employee_id;
