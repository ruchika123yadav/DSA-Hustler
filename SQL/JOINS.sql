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