# Write your MySQL query statement below
select
case
    when id % 2 = 0 then id - 1
    when id % 2 = 1 and id + 1 not in ( -- Last student in case of odd number of students
        select id from seat
    ) then id
    else id + 1
end 
as id,
student
from seat
order by id;