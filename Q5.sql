--Q5 - Display each student's name,  CWID, course, grade, and the instructor's name  for all students and grades
select s.Name as Student, s.CWID, g.Course, g.Grade, i.Name as instructor
from students s
join grades g on s.CWID = g.StudentCWID
join instructors i on g.InstructorCWID = i.CWID
order by s.Name