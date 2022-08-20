from flask import Flask
from flask_restful import Api, Resource, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
from request_parsers import *
from serializers import *
from models import *

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class People(Resource):
	@marshal_with(people_serializer)
	def get(self):
		args = people_get_args.parse_args()
		people = PeopleTable.query.all()
		people = people.filter(PeopleTable.person_id == args["person_id"]) \
			if args["person_id"] \
			else people
		people = people.filter(PeopleTable.first_name == args["first_name"]) \
			if args["first_name"] \
			else people
		people = people.filter(PeopleTable.last_name == args["last_name"]) \
			if args["last_name"] \
			else people

		return people

	@marshal_with(people_serializer)
	def post(self):
		args = people_post_args.parse_args()

		person = PeopleTable(person_id=args["person_id"], first_name=args["first_name"], last_name=args["last_name"])
		db.session.add(person)
		db.session.commit()
		return person, 201

api.add_resource(People, "/people")

if __name__ == "__main__":
	app.run(debug=True)
