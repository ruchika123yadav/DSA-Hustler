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



-- Marketing Touch Streak->https://datalemur.com/questions/marketing-touch-streak
-- VERY VERY NICE AND COMPLICATED ALSO
 DATE_TRUNC('week', event_date))


WITH consecutive_events_cte AS (
  SELECT
    event_id,
    contact_id, 
    event_type, 
    DATE_TRUNC('week', event_date) AS current_week,
    LAG(DATE_TRUNC('week', event_date)) OVER (
      PARTITION BY contact_id 
      ORDER BY DATE_TRUNC('week', event_date)) AS lag_week,
    LEAD(DATE_TRUNC('week', event_date)) OVER (
      PARTITION BY contact_id 
      ORDER BY DATE_TRUNC('week', event_date)) AS lead_week
FROM marketing_touches)

SELECT DISTINCT contacts.email
FROM consecutive_events_cte AS events
INNER JOIN crm_contacts AS contacts
  ON events.contact_id = contacts.contact_id
WHERE events.lag_week = events.current_week - INTERVAL '1 week'
  OR events.lead_week = events.current_week + INTERVAL '1 week'
  AND events.contact_id IN (
    SELECT contact_id 
    FROM marketing_touches 
    WHERE event_type = 'trial_request'
  );



-- RESTRAURANT GROWTH->https://leetcode.com/problems/restaurant-growth/description/


select distinct visited_on,
        sum(amount) over w as amount,
        round((sum(amount) over w)/7, 2) as average_amount
    from customer
    WINDOW w AS ( 
            order by visited_on
            range between interval 6 day PRECEDING and current row
    )
    Limit 6, 999




-- Tweets' Rolling Averages
-- Given a table of tweet data over a specified time period, calculate the 3-day rolling average of tweets for each user. Output the user ID, tweet date, and rolling averages rounded to 2 decimal places.



select user_id,tweet_date,
round(avg(tweet_count) over(partition by user_id order by tweet_date
rows between 2 preceding and current row),2) as rolling_avg_3d
from tweets



-- Server Utilization Time->https://datalemur.com/questions/total-utilization-time

WITH running_time AS (
  SELECT 
    server_id,
    session_status,
    status_time AS start_time,
    LEAD(status_time) OVER (
      PARTITION BY server_id 
      ORDER BY status_time
    ) AS stop_time
  FROM server_utilization
)
SELECT 
  FLOOR(
    SUM(EXTRACT(EPOCH FROM (stop_time - start_time)) / 86400)
  ) AS total_uptime_days
FROM running_time
WHERE session_status = 'start';



-- ODD AND EVEN MEASUREMENTS->https://datalemur.com/questions/odd-even-measurements
with cte as(
select *,row_number() over(partition by measurement_time::date order by measurement_time ) as timee
from measurements
)

select measurement_time::date as measurement_day,
sum(case when timee%2!=0 then measurement_value else 0 end) as odd_sum,
sum(case when timee%2=0. then measurement_value else 0 end) as even_sum
from cte
-- from measurements 
group by  measurement_time::date
order by measurement_day
-- -- group by measurement_time


-- 

-- COUNT SALARY CATEGORIES->https://leetcode.com/problems/count-salary-categories/submissions/2086260091/


SELECT
    'Low Salary' AS category,
    COUNT(CASE WHEN income < 20000 THEN 1 END) AS accounts_count
FROM Accounts

UNION ALL

SELECT
    'Average Salary' AS category,
    COUNT(
        CASE
            WHEN income BETWEEN 20000 AND 50000 THEN 1
        END
    ) AS accounts_count
FROM Accounts

UNION ALL

SELECT
    'High Salary' AS category,
    COUNT(CASE WHEN income > 50000 THEN 1 END) AS accounts_count
FROM Accounts;


