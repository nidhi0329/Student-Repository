--Q4 - Display the name and CWID of each student along with the total number of courses taken by the student
select s.Name, s.CWID, count(*) as courses
from students s join grades g on s.CWID=g.StudentCWID
group by s.Name


