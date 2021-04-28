--Q2-what is the total number of students by major?
select major, count(*)
from students
group by major