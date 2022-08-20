from app import db


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


