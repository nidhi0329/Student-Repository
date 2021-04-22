"""
author: Nidhi Chovatiya
CWID : 10457344
Objective: In this assignment we will work on student & instructor repository
"""

from typing import Dict, List, DefaultDict, Set, Iterator
from collections import defaultdict
from prettytable import PrettyTable
import os
import sys
import statistics


class Student:
    """In this class, we will be creating an instance of a student.
    """
    __titles__ = ['_cwid', '_name', '_courses']
    field_name: List[str] = ["Cwid", "Name", "Completed Courses"]

    def __init__(self, cwid: str, name: str, major: str) -> None:
        """In this method, we will be initializing all the fields related to a student.
        """
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()

    def student_courses(self, course: str, grade: str) -> None:
        """In this method, we will add courses for each student in the dictionary.
        """
        self._courses[course] = grade

    def detail(self) -> List[str]:
        """In this function, we will be returning the outputs.
        """
        return [self._cwid, self._name, sorted(self._courses.keys())]


class Instructor:
    """In this class, we will be creating an instance of an instructor.
    """
    __titles__ = ['_cwid', '_name', '_dept', '_courses']
    field_name: List[str] = ["Cwid", "Name", "Department", "Course", "Count"]

    def __init__(self, cwid: str, name: str, dept: str) -> None:
        """In this method, we will be initializing all the fields related to an
        Instructor
        """
        self._cwid: str = cwid
        self._name: str = name
        self._dept: str = dept
        self._courses: DefaultDict[str, int] = defaultdict(int)

    def instructor_courses(self, course: str) -> None:
        """In this method, we will add course name and number of students enrolled.
        """
        self._courses[course] += 1

    def detail(self) -> List[str]:
        """In this function, we will be returning the outputs.
        """

        for course, count in self._courses.items():
            yield[self._cwid, self._name, self._dept, course, count]


class Repository:
    """
    In this class, we will be creating a repository of student and instructor in an University
    """
    __titles__ = ['_path', '_students', '_instructors', '_majors']

    def file_reader(self, path: str, fields: int, sep: str = ',', header: bool = False) -> Iterator[List[str]]:
        """In this function, we will implement a generator that will yield new line of a file on call of next
        """
        try:
            fp: IO = open(path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError(f"Cannot open file at {path} ")
        else:
            with fp:
                line_number: int = 0
                for line in fp:
                    row: List[str] = line.strip().split(sep)
                    line_number += 1
                    if len(row) != fields:
                        fp.close()
                        raise ValueError(
                            f"File {path} at line {line_number} has  {len(row)} items, whereas the \
                            expected items where {fields} ")
                    if header is False:
                        yield row
                    else:
                        header = False

    def __init__(self, path: str, ptables: bool = True) -> None:
        """In this method, we will be initializing all the fields related to Repository"""
        self._path: str = path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._students_detail()
        self._instructors_detail()
        self._grades_detail()

    def _students_detail(self) -> None:
        """
        In this method, we will be reading each student and creating
        instances of each student as soon as it is read.
        """
        try:
            for cwid, name, major in self.file_reader(os.path.join(self._path,
                                                                   "students.txt"),
                                                      3, sep='\t', header=False):
                if cwid in self._students:
                    print("Student with CWID is already in the file")
                self._students[cwid] = Student(cwid, name, major)
        except FileNotFoundError:
            print(f"Cannot open file at {self._path}")
        except ValueError:
            print("Missing field")

    def _instructors_detail(self) -> None:
        """
        In this method, we will be reading each student and creating
        instances of each instructor as soon as it is read.
        """
        try:
            for cwid, name, dept in self.file_reader(os.path.join
                                                     (self._path,
                                                      "instructors.txt"),
                                                     3, sep='|', header=True):
                if cwid in self._instructors:
                    print("Instructor with CWID is already in the file")
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except FileNotFoundError:
            print(f"file not found")
        except ValueError:
            print("Missing field")

    def _grades_detail(self) -> None:
        """
        In this method, we will be reading the grades of each student.
        """
        try:
            for stud_cwid, course, grade, prof_cwid in self.file_reader(
                    os.path.join(self._path, "grades.txt"), 4, sep='\t', header=False):
                if stud_cwid in self._students:
                    # handle the key error if a new student
                    self._students[stud_cwid].student_courses(course, grade)
                else:
                    print(f"No such Student with {stud_cwid}")
                if prof_cwid in self._instructors:
                    # handle the key error if a new instructor
                    self._instructors[prof_cwid].instructor_courses(course)
                else:
                    print(f"No such Instructor with {prof_cwid}")

        except FileNotFoundError:
            print(f"Cannot open file at {self._path}")
        except ValueError:
            print("Wrong input")

    def student_pt(self) -> PrettyTable:
        """
        In this function, we will be creating pretty table for Student
        """
        pt: PrettyTable = PrettyTable()
        pt.field_names = Student.field_name
        for i in self._students.values():
            pt.add_row(i.detail())
        print("\nStudent Summary")
        print(pt)
        return pt

    def instructor_pt(self) -> PrettyTable:
        """
        In this function, we will be creating pretty table for Instructor
        """
        pt: PrettyTable = PrettyTable()
        pt.field_names = Instructor.field_name
        for i in self._instructors.values():
            for row in i.detail():
                pt.add_row(row)
        print("\nInstructor Summary")
        print(pt)
        return pt


def main():
    stevens: Repository = Repository(
        "C:\\Users\\Nidhi\\Desktop\\SEM3\\810\\HW09")


if __name__ == '__main__':
    main()
