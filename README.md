# Messaging-API

## How to run this API locally

This API can be run in any virtual environment that is using Python 3.7. I chose to use
[Anaconda](https://www.anaconda.com/products/distribution) to create a virtual 
environment by following the steps on 
[this page](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/). 
Once in the virtual environment, running 
`pip install -r requirements.txt`
will install the dependencies needed to successfully run the API locally. Finally, 
`python app.py`
will start the API! 

The `database.db` file already contains dummy data, so running `python app.py` should **just work**.

## Database Details

I created two tables in a SQLite database. The first table is called `people` and contains 
the following columns:

| person_id | first_name | last_name |
|-----------|------------|-----------|
| 1         | Michael    | Scott     |

One can see the full contents of `people` by running the following GET request:
```commandline
curl http://127.0.0.1:5000/people
```

The second table is called `messages` and contains the following columns:

| message_id | sender_id | recipient_id | message | timestamp |
|------------|-----------|--------------|---------|-----------|
| 1          | 2         | 1            | Text    | Date      |

One can see the full contents of `messages` by running the following GET request (note
that this returns all 300 rows from the database table including messages from more than
30 days ago):
```commandline
curl http://127.0.0.1:5000/allMessages
```

I separated this information into two tables in case there are multiple people with the
same first and last name. 

## High Level Requirements

- *"A short text message can be sent from one user (the sender) to another (the recipient)."*

A message can be "sent" from one user (the sender) to another (the recipient) by running the following
command:
```commandline
curl -X POST http://127.0.0.1:5000/messages -H "Content-Type: application/json" -d '{"message_id": 301, "sender_id": 1, "recipient_id": 3, "message": "Brisket magna swine turkey anim frankfurter chicken rump tail.", "timestamp": "2022-08-20T15:20:25.335650"}'  
```

All messages were generated using the [Bacon Ipsum API](https://baconipsum.com/api/) 🥓.

- *"Recent messages can be requested for a recipient from a specific sender. By default, only messages from the last 
30 days should be returned. Additionally, there should be a limit of 100 messages in a response."*

Messages can be retrieved for a recipient from a specific sender by running the following GET request (with 
`recipient_id` and `sender_id` as parameters):

```commandline
curl -X GET "http://127.0.0.1:5000/messages?recipient_id=1&sender_id=2"
```

The messages in the response are ordered by date in descending order.

- *"Recent messages can be requested from all senders. By default, only messages from the last 30 days should 
be returned. Additionally, there should be a limit of 100 messages in a response."*

Messages can be retrieved for a recipient from **all** senders by running the following GET request:

```commandline
curl -X GET "http://127.0.0.1:5000/messages?recipient_id=1"
```

Additionally, messages can be retrieved for all senders (regardless of recipient) with the following 
GET request:

```commandline
curl -X GET "http://127.0.0.1:5000/messages"
```

Once again, the messages in the response are ordered by date in descending order.

- *Include tests and document how to test your API.*

In order to test this API, I needed to generate dummy data. This was done using the 
code in `generate_data.py`. These data contain messages that are older than 30 days, as well
as more than 100 messages for certain `recipient_id`/`sender_id` combinations. This allows
us to test the two constraints outlined above. 

I wrote a basic test in `test_messages.py` that checks that

1. There are no more than 100 messages in the response and
2. Only messages from the last 30 days are being returned

This test can be run with

```commandline
python -m pytest tests/test_messages.py
```

With more time, I would have *hopefully* been more thoughtful about edge cases that would
need to be tested...

- All other High Level Requirements are covered by the information already outlined in 
`README.md`.



