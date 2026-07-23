-- EMPLOYEE EARNING MORE THAN THEIR MANAGER
  
select e1.name as Employee from Employee e1
join Employee e2
on e1.managerId is not null and e1.managerId=e2.id and e1.salary>e2.salary 


-- 570 MANAGER WITH ALTEAST 5 DIRECTS REPORTS

with cte as (SELECT managerId from Employee 
where managerId is not null
group by managerId
having count(id)>=5)

select name from Employee
where id in (select managerId from cte)


-- https://datalemur.com/questions/completed-trades

WITH cte AS (
    SELECT 
        u.city,
        t.user_id AS completed_user_id
    FROM users u 
    inner JOIN trades t 
        ON u.user_id = t.user_id 
       AND t.status = 'Completed'  
)

SELECT 
    city, 
    COUNT(completed_user_id) AS total_orders 
FROM cte 
GROUP BY city 
ORDER BY total_orders DESC 
LIMIT 3;


-- OPNING AND CLOSING SNAP ->https://datalemur.com/questions/time-spent-snaps

select a1.age_bucket,
round(sum(case when a2.activity_type='send' then a2.time_spent else 0 end)*100.0/sum(a2.time_spent),2) as send_perc,
round(sum(case when a2.activity_type='open' then a2.time_spent else 0 end)*100.0/sum(a2.time_spent),2)as open_perc

from age_breakdown a1
inner join activities  a2
on a1.user_id=a2.user_id and a2.activity_type!='chat'
group by a1.age_bucket


-- TOP 3 UNIQUE SALARIES->https://datalemur.com/questions/sql-top-three-salaries
 
 select department_name,	name	,salary 
 from(
 select d.department_name,	e.name	,e.salary,
 dense_rank() over(partition by e.department_id order by e.salary desc)as rnk
 from department d 
 left join employee e 
 on d.department_id=e.department_id
 )temp
 
 where rnk<=3
 order by department_name,salary desc, name asc


-- VERY GOOD QUESTION ->https://leetcode.com/problems/human-traffic-of-stadium/

-- Bhai, ye id - ROW_NUMBER() wali trick LeetCode ki Human Traffic of Stadium (Problem 601) ki sabse smart aur famous trick hai!

with cte as(

select *,id-row_number() over() as id_diff
from Stadium
where people>99
)

select id ,visit_date , people 
from cte 
where id_diff in (select id_diff from cte group by id_diff having count(id_diff)>2)
group by id_diff
order by visit_date

 

-- Y-on-Y Growth Rate RESPECT TO EACH PRODUCT->https://datalemur.com/questions/yoy-growth-rate
-- NICE QUESTION
 select EXTRACT(YEAR FROM transaction_date) as year,
 product_id,
 spend as curr_year_spend,
 lag(spend,1) over(partition by product_id  order by transaction_date) as prev_year_spend,
 round((spend -lag(spend,1) over(partition by product_id  order by transaction_date))*100/lag(spend,1) over(partition by product_id  order by transaction_date),2) as yoy_rate
 
 from user_transactions 
  order by product_id,year