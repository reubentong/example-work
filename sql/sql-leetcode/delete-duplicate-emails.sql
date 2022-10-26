-- https://leetcode.com/problems/delete-duplicate-emails/
-- https://leetcode.com/submissions/detail/830694720/
DELETE A FROM Person A, Person B WHERE A.email = B.email and A.id > B.id;