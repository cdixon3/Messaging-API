from flask_restful import fields

people_serializer = {
    "person_id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String
}