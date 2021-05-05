"""
author: Nidhi Chovatiya
CWID : 10457344
Objective: To write the test class in order to test HW11
"""

import unittest
from Student_Repository_Nidhi_Chovatiya import Repository, Student, Instructor, Major
from typing import List, Dict
from prettytable import PrettyTable


class HW10TestCase(unittest.TestCase):
    """
    class to test the HW10 assignment
    """

    def setUp(self) -> None:
        """
        this method is to set the file path
        """
        self.file_path = "C:\\Users\\Nidhi\\Desktop\\SEM3\\810\\HW11"
        self.dbpath = "C:\\Users\\Nidhi\\Desktop\\SEM3\\810\\HW11\\810_startup.db"
        self.repo = Repository(self.file_path, self.dbpath, False)

    def test_students(self) -> None:
        """
        this method is to test student
        """
        cwid: List[str] = list()
        name: List[str] = list()
        major: List[str] = list()
        completed_courses: List[List[str]] = list()
        remaining_electives: List[List[str]] = list()
        remaining_required: List[List[str]] = list()
        gpa: List[float] = list()
        result: PrettyTable = self.repo.student_pt()
        for r in result:
            r.border = False
            r.header = False
            cwid.append(r.get_string(fields=["CWID"]).strip())
            name.append(r.get_string(fields=["Name"]).strip())
            major.append(r.get_string(fields=["Major"]).strip())
            completed_courses.append(r.get_string(
                fields=["Completed Courses"]).strip())
            remaining_required.append(r.get_string(
                fields=["Remaining Required"]).strip())
            remaining_electives.append(r.get_string(
                fields=["Remaining Electives"]).strip())
            gpa.append(r.get_string(fields=["GPA"]).strip())
        check_cwid: List[str] = ['10103', '10115', '10183', '11714']
        check_name: List[str] = ['Jobs, S', 'Bezos, J', 'Musk, E', 'Gates, B']
        check_major: List[str] = ['SFEN', 'SFEN', 'SFEN', 'CS']
        check_cc: List[List[str]] = ["['CS 501', 'SSW 810']", "['SSW 810']",
                                     "['SSW 555', 'SSW 810']", "['CS 546', 'CS 570', 'SSW 810']"]
        check_re: List[List[str]] = [
            "[]", "['CS 501', 'CS 546']", "['CS 501', 'CS 546']", "[]"]
        check_gpa: List[float] = ['3.38', '2.00', '4.00', '3.50']
        check_rr: List[List[str]] = ["['SSW 540', 'SSW 555']",
                                     "['SSW 540', 'SSW 555']", "['SSW 540']", "[]"]
        self.assertEqual(cwid, check_cwid)
        self.assertEqual(name, check_name)
        self.assertEqual(major, check_major)
        self.assertEqual(completed_courses, check_cc)
        self.assertEqual(remaining_required, check_rr)
        self.assertEqual(remaining_electives, check_re)
        self.assertEqual(gpa, check_gpa)

    def test_instructor(self) -> None:
        """
        this method is To test instructor
        """
        cwid: List[str] = list()
        name: List[str] = list()
        dept: List[str] = list()
        course: List[str] = list()
        cnt: List[int] = list()
        result: PrettyTable = self.repo.instructor_pt()
        for r in result:
            r.border = False
            r.header = False
            cwid.append(r.get_string(fields=["CWID"]).strip())
            name.append(r.get_string(fields=["Name"]).strip())
            dept.append(r.get_string(fields=["Dept"]).strip())
            course.append(r.get_string(fields=["Course"]).strip())
            cnt.append(r.get_string(fields=["Students"]).strip())
        check_cwid: List[str] = ['98764', '98763',
                                 '98763', '98762', '98762', '98762']
        check_name: List[str] = ['Cohen, R', 'Rowland, J',
                                 'Rowland, J', 'Hawking, S', 'Hawking, S', 'Hawking, S']
        check_dept: List[str] = ['SFEN', 'SFEN', 'SFEN', 'CS', 'CS', 'CS']
        check_course: List[str] = ['CS 546', 'SSW 810',
                                   'SSW 555', 'CS 501', 'CS 546', 'CS 570']
        check_cnt: List[str] = ['1', '4', '1', '1', '1', '1']
        self.assertEqual(cwid, check_cwid)
        self.assertEqual(name, check_name)
        self.assertEqual(dept, check_dept)
        self.assertEqual(course, check_course)
        self.assertEqual(cnt, check_cnt)

    def test_major(self) -> None:
        """
        this method is To test major
        """
        major: List[str] = list()
        rc: List[List[str]] = list()
        ec: List[List[str]] = list()
        result: PrettyTable = self.repo.major_pt()
        for r in result:
            r.border = False
            r.header = False
            major.append(r.get_string(fields=["Major"]).strip())
            rc.append(r.get_string(fields=["Required Courses"]).strip())
            ec.append(r.get_string(fields=["Electives"]).strip())
        check_major: List[str] = ['SFEN', 'CS']
        check_rc: List[List[str]] = [
            "['SSW 540', 'SSW 555', 'SSW 810']", "['CS 546', 'CS 570']"]
        check_ec: List[List[str]] = [
            "['CS 501', 'CS 546']", "['SSW 565', 'SSW 810']"]
        self.assertEqual(major, check_major)
        self.assertEqual(rc, check_rc)
        self.assertEqual(ec, check_ec)

    def test_student_grade(self) -> None:
        """
        This methis is to test grades summary
        """
        cwid: List[str] = list()
        name: List[str] = list()
        course: List[str] = list()
        grade: List[str] = list()
        inst: List[str] = list()
        result: PrettyTable = self.repo.grades_pt(self.dbpath)
        for r in result:
            r.border = False
            r.header = False
            name.append(r.get_string(fields=["Name"]).strip())
            cwid.append(r.get_string(fields=["CWID"]).strip())
            course.append(r.get_string(fields=["Course"]).strip())
            grade.append(r.get_string(fields=["Grade"]).strip())
            inst.append(r.get_string(fields=["Instructor"]).strip())
        test_name: List[str] = ['Bezos, J', 'Bezos, J', 'Gates, B',
                                'Gates, B', 'Gates, B', 'Jobs, S', 'Jobs, S', 'Musk, E', 'Musk, E']
        test_cwid: List[str] = ['10115', '10115', '11714',
                                '11714', '11714', '10103', '10103', '10183', '10183']
        test_course: List[str] = ['SSW 810', 'CS 546', 'SSW 810',
                                  'CS 546', 'CS 570', 'SSW 810', 'CS 501', 'SSW 555', 'SSW 810']
        test_grade: List[str] = ['A', 'F', 'B-',
                                 'A', 'A-', 'A-', 'B', 'A', 'A']
        test_inst: List[str] = ['Rowland, J', 'Hawking, S', 'Rowland, J',
                                'Cohen, R', 'Hawking, S', 'Rowland, J', 'Hawking, S', 'Rowland, J', 'Rowland, J']
        self.assertEqual(name, test_name)
        self.assertEqual(cwid, test_cwid)
        self.assertEqual(course, test_course)
        self.assertEqual(grade, test_grade)
        self.assertEqual(inst, test_inst)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
