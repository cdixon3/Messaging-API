from flask import Flask
from flask_restful import Api, Resource, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
from request_parsers import *
from serializers import *
import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

thirty_one_days_ago = datetime.datetime.now() - datetime.timedelta(31)

class PeopleTable(db.Model):

    __tablename__ = 'people'

    person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)


class MessagesTable(db.Model):

    __tablename__ = 'messages'

    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    recipient_id = db.Column(db.Integer)
    message = db.Column(db.String)
    timestamp = db.Column(db.DateTime(timezone=True))


class People(Resource):
	@marshal_with(people_serializer)
	def get(self):
		args = people_get_args.parse_args()
		people = PeopleTable.query
		people = people.filter(PeopleTable.person_id == args["person_id"]) \
			if args["person_id"] \
			else people
		people = people.filter(PeopleTable.first_name == args["first_name"]) \
			if args["first_name"] \
			else people
		people = people.filter(PeopleTable.last_name == args["last_name"]) \
			if args["last_name"] \
			else people

		return people.all()

	@marshal_with(people_serializer)
	def post(self):
		args = people_post_args.parse_args()

		person = PeopleTable(person_id=args["person_id"], first_name=args["first_name"], last_name=args["last_name"])
		db.session.add(person)
		db.session.commit()
		return person, 201

	def delete(self):
		args = people_delete_args.parse_args()

		person = db.session.query(PeopleTable).filter(PeopleTable.person_id == args["person_id"]).first()
		db.session.delete(person)
		db.session.commit()

		return 200


class Messages(Resource):
	@marshal_with(messages_serializer)
	def get(self):
		args = messages_get_args.parse_args()
		messages = MessagesTable.query
		messages = messages.filter(MessagesTable.message_id == args["message_id"]) \
			if args["message_id"] \
			else messages
		messages = messages.filter(MessagesTable.sender_id == args["sender_id"]) \
			if args["sender_id"] \
			else messages
		messages = messages.filter(MessagesTable.recipient_id == args["recipient_id"]) \
			if args["recipient_id"] \
			else messages
		messages = messages.filter(MessagesTable.timestamp > thirty_one_days_ago)

		return messages.order_by(MessagesTable.timestamp.desc()).limit(100).all()

	@marshal_with(messages_serializer)
	def post(self):
		args = messages_post_args.parse_args()

		message = MessagesTable(message_id=args["message_id"], sender_id=args["sender_id"],
								recipient_id=args["recipient_id"], message=args["message"],
								timestamp=args["timestamp"])

		db.session.add(message)
		db.session.commit()
		return message, 201

	def delete(self):
		args = messages_delete_args.parse_args()

		message = db.session.query(MessagesTable).filter(MessagesTable.message_id == args["message_id"]).first()
		db.session.delete(message)
		db.session.commit()

		return 200


api.add_resource(People, "/people")
api.add_resource(Messages, "/messages")

if __name__ == "__main__":
	app.run(debug=True)
