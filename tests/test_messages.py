from app import app
import json
import datetime
from datetime import datetime as dt

thirty_one_days_ago = datetime.datetime.now() - datetime.timedelta(31)

def test_messages_get():
    """
    Test for GET request to /messages endpoint
    """
    with app.test_client() as client:
        results = client.get("/messages?recipient_id=1")
        data = json.loads(results.data)
        last_date = dt.fromisoformat(data[-1]["timestamp"])

    assert len(data) <= 100
    assert last_date > thirty_one_days_ago