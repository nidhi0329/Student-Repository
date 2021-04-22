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


class Major:
    """In this class, we will be creating an instance of Major.
    """
    __titles__ = ['_major', '_required', '_electives']
    field_name: List[str] = ["Major", "Required Courses", "Elective Courses"]

    def __init__(self, major: str) -> None:
        """
        Here we will be initializing the variables.
        """
        self._major: str = major
        self._required: List[str] = list()
        self._electives: List[str] = list()

    def add_course(self, type: str, course: str) -> None:
        """
        In this method, we will add course based on type (Required/Elective)
        """
        if type == "R":
            self._required.append(course)
        elif type == "E":
            self._electives.append(course)
        else:
            raise ValueError("Course not found")

    def required_course(self) -> List[str]:
        """In this functions, we will return the required courses.
        """
        return list(self._required)

    def electives_course(self) -> List[str]:
        """In this functions, we will return the elective courses.
        """
        return list(self._electives)

    def detail(self) -> List[str]:
        """
        In this function, we will be returning the outputs.
        """
        return [self._major, sorted(self._required), sorted(self._electives)]


class Student:
    """In this class, we will be creating an instance of a student.
    """
    __titles__ = ['_cwid', '_name', '_major', '_courses',
                  '_remaining_required', '_remaining_electives', '_fail',
                  '_grade']
    field_name: List[str] = ["Cwid", "Name", "Major", "Completed Courses",
                             "Remaining Required", "Remaining Elective", "GPA"]

    def __init__(
            self,
            cwid: str,
            name: str,
            major: str,
            required: List[str],
            electives: List[str]) -> None:
        """In this method, we will be initializing all the fields related to a student.
        """
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()
        self._remaining_required: List[str] = required
        self._remaining_electives: List[str] = electives
        self._fail: List[str] = ["C-", "D+", "D", "D-", "F"]
        self._grade: Dict[str, float] = {"A": 4.0, "A-": 3.75, "B+": 3.25,
                                         "B": 3.0, "B-": 2.75, "C+": 2.25,
                                         "C": 2.0, "C-": 0.0, "D+": 0.0,
                                         "D": 0.0, "D-": 0.0, "F": 0.0}

    def student_courses(self, course: str, grade: str) -> None:
        """In this method, we will add courses for each student in the dictionary.
        """
        if grade not in self._fail:
            self._courses[course] = grade
        if course in self._remaining_required:
            self._remaining_required.remove(course)
        if course in self._remaining_electives:
            self._remaining_electives.clear()

    def _gpa(self) -> float:
        """In this method, we will compute the GPA based on the courses
        """
        GPA: List[float] = list()
        for a1 in self._courses.values():
            if a1 in self._grade:
                GPA.append(self._grade[a1])
            else:
                print("grade is not valid")
        if len(GPA) > 0:
            gpa: float = statistics.mean(GPA)
        else:
            return 0.0

        return format(gpa, '.2f')

    def detail(self) -> List[str]:
        """In this function, we will be returning the outputs.
        """
        return [self._cwid, self._name, self._major,
                sorted(self._courses.keys()),
                sorted(self._remaining_required),
                sorted(self._remaining_electives),
                self._gpa()]


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
        self._majors: Dict[str, Major] = dict()
        self._majors_detail()
        self._students_detail()
        self._instructors_detail()
        self._grades_detail()

    def _majors_detail(self) -> None:
        """
        Reading each major and creating its instance
        """
        try:
            for major, type, course in self.file_reader(os.path.join(self._path,
                                                                     "majors.txt"),
                                                        3, sep='\t', header=True):
                if major not in self._majors:
                    self._majors[major] = Major(major)
                self._majors[major].add_course(type, course)
        except FileNotFoundError:
            print(f"Cannot open file at {self._path}")

    def _students_detail(self) -> None:
        """
        In this method, we will be reading each student and creating
        instances of each student as soon as it is read.
        """
        try:
            for cwid, name, major in self.file_reader(os.path.join(self._path,
                                                                   "students.txt"),
                                                      3, sep=';', header=True):
                if cwid in self._students:
                    print("Student with CWID is already in the file")
                required: List[str] = self._majors[major].required_course()
                electives: List[str] = self._majors[major].electives_course()
                self._students[cwid] = Student(
                    cwid, name, major, required, electives)
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
                    os.path.join(self._path, "grades.txt"), 4, sep='|', header=True):
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

    def major_pt(self) -> PrettyTable:
        """
        In this function, we will be creating pretty table for Major
        """
        pt: PrettyTable = PrettyTable()
        pt.field_names = Major.field_name
        for i in self._majors.values():
            pt.add_row(i.detail())
        print("Majors Summary")
        print(pt)
        return pt

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
        "C:\\Users\\Nidhi\\Desktop\\SEM3\\810\\HW10")


if __name__ == '__main__':
    main()
