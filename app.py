"""
author: Nidhi Chovatiya
CWID : 10457344
Objective: In this assignment we will work on flask & Jinja2
"""

from flask import Flask, render_template, redirect, url_for
import sqlite3
from typing import Dict

app: Flask = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    """ Student Repository main page """
    # A Student Repository main page which shows all the available repositories
    # could be rendered here but we do not need it now. Redirecting to the only one, Stevens!
    return redirect(url_for('student_summary'))


@app.route('/student_summary/', methods=['GET'])
def student_summary() -> str:
    DataBase: str = r'C:/Users/Nidhi/Desktop/SEM3/810/HW12/810_startup.db'

    try:
        db: sqlite3.Connection = sqlite3.connect(DataBase)
    except sqlite3.OperationalError:
        return f"Not able to open database"
    else:
        query: str = """select s.name, s.cwid, g.Course, g.Grade,i.name from students
                        s join grades as g on s.cwid = g.StudentCWID join instructors i on
                        i.cwid = g.InstructorCWID order by s.name"""

        h1: List[str] = db.execute(query).description

    # convert the query result into dictionaries
    data: Dict[str,
               str] = [{'name': name, 'cwid': cwid, 'course': course, 'grade': grade, 'instructor': instructor}
                       for cwid, name, course, grade, instructor in db.execute(query)]

    # close the connection
    db.close()
    return render_template(
        'student.html',
        headers=h1,
        table=data)


if __name__ == '__main__':
    app.run(debug=True)
