-- https://leetcode.com/problems/find-customer-referee/
-- https://leetcode.com/submissions/detail/829923618/
SELECT name from Customer WHERE referee_id IS NULL OR NOT referee_id = 2;