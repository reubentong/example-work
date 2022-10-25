-- https://leetcode.com/problems/recyclable-and-low-fat-products/
-- https://leetcode.com/submissions/detail/829920575/
SELECT product_id FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';