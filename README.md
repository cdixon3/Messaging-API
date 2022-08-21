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

I separated this information into two tables in case there are multiple people with the
same first and last name. 

One can see the full contents of `messages` by running the following GET request (note
that this returns all 300 rows from the database table including messages from more than
30 days ago):
```commandline
curl http://127.0.0.1:5000/allMessages
```

