from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

STUDENTS = {
    '1':{'name':'Mark', 'age': 22, 'course':'math'},
    '2':{'name':'Jane', 'age': 20, 'course':'biology'},
    '3':{'name':'Peter', 'age': 21, 'course':'chemistry'},
    '4':{'name':'Kate', 'age': 24, 'course':'history'}
}

parser = reqparse.RequestParser()

class StudentList(Resource):
    def get(self):
        return STUDENTS

    def post(self):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("course")
        args = parser.parse_args()
        student_id = int (max(STUDENTS.keys())) + 1
        student_id = '%i' % student_id

        STUDENTS[student_id] = {
            "name":args["name"],
            "age" : args["age"],
            "course": args["course"]
        }

        return STUDENTS[student_id], 201

class Student(Resource):
    def get(self, student_id):
        if student_id not in STUDENTS:
            return 'Not Found', 404
        else:
            return STUDENTS[student_id]
        
    def put(self, student_id):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("course")
        args = parser.parse_args()

        if student_id not in STUDENTS:
            return 'Record not Found', 404
        
        else:
            student = STUDENTS[student_id]
            student["name"] = args["name"] if args is not None else student["name"]
            student["age"] = args["age"] if args is not None else student["age"]
            student["course"] = args["course"] if args is not None else student["course"]
            return student, 200
        
    def delete(self, student_id):    
        if student_id not in STUDENTS:
            return 'Not found', 404
        else:
            del STUDENTS[student_id]
            return '', 204

api.add_resource(StudentList, '/students/')
api.add_resource(Student, '/students/<student_id>')

if __name__ == '__main__':
    app.run(debug = True)