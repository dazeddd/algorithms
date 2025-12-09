-- # Write your MySQL query statement below
-- with ranking as (
--     select id, salary, dense_rank() over(order by salary desc) salary_ranking from Employee
-- )
-- select * from ranking;

-- select IFNULL(salary, NULL) SecondHighestSalary from ranking where salary_ranking = 2;


SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary;