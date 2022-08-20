from flask_restful import fields

people_serializer = {
    "person_id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String
}

messages_serializer = {
    "message_id": fields.Integer,
    "sender_id": fields.Integer,
    "recipient_id": fields.Integer,
    "message": fields.String,
    "timestamp": fields.DateTime
}