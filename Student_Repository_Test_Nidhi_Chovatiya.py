"""
author: Nidhi Chovatiya
CWID : 10457344
Objective: To write the test class in order to test HW10
"""

import unittest
from Student_Repository_Nidhi_Chovatiya import Repository, Student, Instructor
from typing import List, Dict, Tuple
from prettytable import PrettyTable


class HW10TestCase(unittest.TestCase):
    """
    class to test the HW10 assignment
    """

    def setUp(self) -> None:
        """
        this method is to set the file path
        """
        self.file_path = "C:\\Users\\Nidhi\\Desktop\\SEM3\\810\\HW09"
        self.repo = Repository(self.file_path, False)

    def test_students(self) -> None:
        """
        this method is to test student
        """

        cwid: List[str] = list()
        name: List[str] = list()
        major: List[str] = list()
        completed_courses: List[List[str]] = list()
        result: PrettyTable = self.repo.student_pt()
        for r in result:
            r.border = False
            r.header = False
            cwid.append(r.get_string(fields=["Cwid"]).strip())
            name.append(r.get_string(fields=["Name"]).strip())
            completed_courses.append(r.get_string(
                fields=["Completed Courses"]).strip())

        check_cwid: List[str] = ['10103', '10115', '10172', '10175',
                                 '10183', '11399', '11461', '11658', '11714', '11788']

        check_name: List[str] = ['Baldwin, C', 'Wyatt, X', 'Forbes, I', 'Erickson, D',
                                 'Chapman, O', 'Cordova, I', 'Wright, U', 'Kelly, P', 'Morton, A', 'Fuller, E']

        check_cc: List[List[str]] = ["['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']",
                                     "['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']",
                                     "['SSW 555', 'SSW 567']",
                                     "['SSW 564', 'SSW 567', 'SSW 687']", "['SSW 689']",
                                     "['SSW 540']", "['SYS 611', 'SYS 750', 'SYS 800']",
                                     "['SSW 540']", "['SYS 611', 'SYS 645']", "['SSW 540']"]

        self.assertEqual(cwid, check_cwid)
        self.assertEqual(name, check_name)
        self.assertEqual(completed_courses, check_cc)

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


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
