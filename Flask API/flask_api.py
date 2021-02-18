from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

students = {
	'1': {'name': 'Mark', 'age':20, 'subject': 'Programming', 'email': 'mark@gmail.com'},
	'2': {'name': 'Jane', 'age':22, 'subject': 'Numerical Analysis', 'email': 'jane02@gmail.com'},
	'3': {'name': 'Peter', 'age':24, 'subject': 'Statistics', 'email': 'peterparker@gmail.com'},
	'4': {'name': 'Kate', 'age':21, 'subject': 'Psycology', 'email': 'kate@gmail.com'},

}

parser = reqparse.RequestParser()


class StudentList(Resource):
	
	def get(self):
		return students

	def post(self):
		
		parser.add_argument('name')
		
		parser.add_argument('age')
		
		parser.add_argument('student')
		
		parser.add_argument('email')

		args = parser.parse_args()
		
		student_id = int(max(students.keys())) + 1
		
		student_id = f'{student_id}'
		
		students[student_id] = {
		'name': args['name'],
		'age': args['age'],
		'subject': args['subject'],
		'email': args['email'],
		}

		return students[student_id], 201



class Student(Resource):

	def get(self, student_id):
		if student_id not in students:
			return 'Not found', 404
		else:
			return students[student_id]


	def put(self, student_id):
		parser.add_argument('name')
		
		parser.add_argument('age')
		
		parser.add_argument('student')

		parser.add_argument('email')
		
		args = parser.parse_args()

		if student_id not in students:
			return 'Not found', 404
		else:
			student = student[student_id]
			
			student['name'] = args['name'] if args['name'] is not None else student['name']

			student['age'] = args['age'] if args['age'] is not None else student['age']
			
			student['subject'] = args['subject'] if args['subject'] is not None else student['subject']
			
			student['email'] = args['email'] if args['email'] is not None else student['email']
			
			return student, 200

			
	def delete(self, student_id):
		if student_id in students:
			return 'Not found', 404
		else:
			del student[student_id]
			return '', 204


api.add_resource(StudentList, '/students/')
api.add_resource(Student, '/students/<student_id>')

if __name__ == '__main__':
	app.run(debug=True)