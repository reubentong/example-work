-- https://leetcode.com/problems/customers-who-never-order/
-- https://leetcode.com/submissions/detail/829932626/
SELECT name as Customers FROM Customers WHERE id NOT IN (SELECT customerId FROM Orders);