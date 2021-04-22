"""
author: Nidhi Chovatiya
CWID : 10457344
Objective: To write the test class in order to test HW10
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
        self.file_path = "C:\\Users\\Nidhi\\Desktop\\SEM3\\810\\HW10"
        self.repo = Repository(self.file_path, False)

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
            cwid.append(r.get_string(fields=["Cwid"]).strip())
            name.append(r.get_string(fields=["Name"]).strip())
            major.append(r.get_string(fields=["Major"]).strip())
            completed_courses.append(r.get_string(
                fields=["Completed Courses"]).strip())
            remaining_required.append(r.get_string(
                fields=["Remaining Required"]).strip())
            remaining_electives.append(r.get_string(
                fields=["Remaining Elective"]).strip())
            gpa.append(r.get_string(fields=["GPA"]).strip())

        check_cwid: List[str] = ['10103', '10115', '10172', '10175',
                                 '10183', '11399', '11461', '11658', '11714', '11788']

        check_name: List[str] = ['Baldwin, C', 'Wyatt, X', 'Forbes, I', 'Erickson, D',
                                 'Chapman, O', 'Cordova, I', 'Wright, U', 'Kelly, P', 'Morton, A', 'Fuller, E']

        check_major: List[str] = ['SFEN', 'SFEN', 'SFEN',
                                  'SFEN', 'SFEN', 'SYEN', 'SYEN', 'SYEN', 'SYEN', 'SYEN']

        check_cc: List[List[str]] = ["['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']",
                                     "['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']",
                                     "['SSW 555', 'SSW 567']",
                                     "['SSW 564', 'SSW 567', 'SSW 687']", "['SSW 689']",
                                     "['SSW 540']", "['SYS 611', 'SYS 750', 'SYS 800']",
                                     '[]', "['SYS 611', 'SYS 645']", "['SSW 540']"]
        check_re: List[List[str]] = ['[]',
                                     '[]',
                                     "['CS 501', 'CS 513', 'CS 545']",
                                     "['CS 501', 'CS 513', 'CS 545']",
                                     "['CS 501', 'CS 513', 'CS 545']",
                                     '[]',
                                     "['SSW 540', 'SSW 565', 'SSW 810']",
                                     '[]',
                                     "['SSW 540', 'SSW 565', 'SSW 810']",
                                     '[]']
        check_gpa: List[float] = ['3.44', '3.81', '3.88',
                                  '3.58', '4.00', '3.00', '3.92', '0.0', '3.00', '4.00']

        check_rr: List[List[str]] = ["['SSW 540', 'SSW 555']",
                                     "['SSW 540', 'SSW 555']",
                                     "['SSW 540', 'SSW 564']",
                                     "['SSW 540', 'SSW 555']",
                                     "['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567']",
                                     "['SYS 612', 'SYS 671', 'SYS 800']",
                                     "['SYS 612', 'SYS 671']",
                                     "['SYS 612', 'SYS 671', 'SYS 800']",
                                     "['SYS 612', 'SYS 671', 'SYS 800']",
                                     "['SYS 612', 'SYS 671', 'SYS 800']"]
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
            cwid.append(r.get_string(fields=["Cwid"]).strip())
            name.append(r.get_string(fields=["Name"]).strip())
            dept.append(r.get_string(fields=["Department"]).strip())
            course.append(r.get_string(fields=["Course"]).strip())
            cnt.append(r.get_string(fields=["Count"]).strip())

        check_cwid: List[str] = ['98765', '98765', '98764', '98764', '98764',
                                 '98764', '98763', '98763', '98760', '98760', '98760', '98760']
        check_name: List[str] = ['Einstein, A', 'Einstein, A', 'Feynman, R', 'Feynman, R', 'Feynman, R',
                                 'Feynman, R', 'Newton, I', 'Newton, I', 'Darwin, C', 'Darwin, C', 'Darwin, C', 'Darwin, C']
        check_dept: List[str] = ['SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN',
                                 'SFEN', 'SFEN', 'SFEN', 'SYEN', 'SYEN', 'SYEN', 'SYEN']
        check_course: List[str] = ['SSW 567', 'SSW 540', 'SSW 564', 'SSW 687', 'CS 501',
                                   'CS 545', 'SSW 555', 'SSW 689', 'SYS 800', 'SYS 750', 'SYS 611', 'SYS 645']
        check_cnt: List[str] = ['4', '3', '3', '3',
                                '1', '1', '1', '1', '1', '1', '2', '1']
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
            rc.append(r.get_string(
                fields=["Required Courses"]).strip())
            ec.append(r.get_string(
                fields=["Elective Courses"]).strip())

        check_major: List[str] = ['SFEN', 'SYEN']
        check_rc: List[List[str]] = [
            "['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567']", "['SYS 612', 'SYS 671', 'SYS 800']"]
        check_ec: List[List[str]] = [
            "['CS 501', 'CS 513', 'CS 545']", "['SSW 540', 'SSW 565', 'SSW 810']"]
        self.assertEqual(major, check_major)
        self.assertEqual(rc, check_rc)
        self.assertEqual(ec, check_ec)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
