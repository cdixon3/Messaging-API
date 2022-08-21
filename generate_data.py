from random import randrange
from datetime import timedelta, datetime


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


#######################################################################
# Generate 125 messages of sender_id=2 to recipient_id=1 within 30 days
#######################################################################

d1 = datetime.strptime('7/21/2022 4:00 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('8/20/2022 4:00 PM', '%m/%d/%Y %I:%M %p')

for i in range(125):
    params = {
        "message_id": i + 1,
        "sender_id": 2,
        "recipient_id": 1,
        "message": requests.get("https://baconipsum.com/api/?type=meat-and-filler&sentences=1").json()[0],
        "timestamp": random_date(d1, d2).isoformat()
    }

    request = requests.post("http://127.0.0.1:5000/messages", params=params)


###############################################################################
# Generate 25 messages of sender_id=2 to recipient_id=1 outside of 30 day range
###############################################################################

d1 = datetime.strptime('5/20/2022 4:00 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('7/21/2022 4:00 PM', '%m/%d/%Y %I:%M %p')

for i in range(125, 150):
    params = {
        "message_id": i + 1,
        "sender_id": 2,
        "recipient_id": 1,
        "message": requests.get("https://baconipsum.com/api/?type=meat-and-filler&sentences=1").json()[0],
        "timestamp": random_date(d1, d2).isoformat()
    }

    request = requests.post("http://127.0.0.1:5000/messages", params=params)


#######################################################################
# Generate 125 messages of sender_id=3 to recipient_id=1 within 30 days
#######################################################################

d1 = datetime.strptime('7/21/2022 4:00 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('8/20/2022 4:00 PM', '%m/%d/%Y %I:%M %p')

for i in range(150, 275):
    params = {
        "message_id": i + 1,
        "sender_id": 3,
        "recipient_id": 1,
        "message": requests.get("https://baconipsum.com/api/?type=meat-and-filler&sentences=1").json()[0],
        "timestamp": random_date(d1, d2).isoformat()
    }

    request = requests.post("http://127.0.0.1:5000/messages", params=params)


###############################################################################
# Generate 25 messages of sender_id=3 to recipient_id=1 outside of 30 day range
###############################################################################

d1 = datetime.strptime('5/20/2022 4:00 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('7/21/2022 4:00 PM', '%m/%d/%Y %I:%M %p')

for i in range(275, 300):
    params = {
        "message_id": i + 1,
        "sender_id": 3,
        "recipient_id": 1,
        "message": requests.get("https://baconipsum.com/api/?type=meat-and-filler&sentences=1").json()[0],
        "timestamp": random_date(d1, d2).isoformat()
    }

    request = requests.post("http://127.0.0.1:5000/messages", params=params)