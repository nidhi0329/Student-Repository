--Q3 - Most frequent grade for SSW 810 across all of the students
select Course, Grade, count(*)
from grades
where Course = 'SSW 810'
group by Course, Grade
order by count(*) desc
limit 1