from flask_restful import reqparse, inputs

people_get_args = reqparse.RequestParser()
people_get_args.add_argument("person_id", type=int, help="Unique ID for recipient or sender.", required=False)
people_get_args.add_argument("first_name", type=str, help="First name of recipient or sender.", required=False)
people_get_args.add_argument("last_name", type=str, help="Last name of recipient or sender.", required=False)

people_post_args = reqparse.RequestParser()
people_post_args.add_argument("person_id", type=int, help="Unique ID for recipient or sender is required.", required=True)
people_post_args.add_argument("first_name", type=str, help="First name of recipient or sender is required.", required=True)
people_post_args.add_argument("last_name", type=str, help="Last name of recipient or sender is required.", required=True)

people_delete_args = reqparse.RequestParser()
people_delete_args.add_argument("person_id", type=int, help="Unique ID for recipient or sender is required.", required=True)

messages_post_args = reqparse.RequestParser()
messages_post_args.add_argument("message_id", type=int, help="Message ID is required.", required=True)
messages_post_args.add_argument("sender_id", type=int, help="ID of sender is required.", required=True)
messages_post_args.add_argument("recipient_id", type=int, help="ID of recipient is required.", required=True)
messages_post_args.add_argument("message", type=str, help="Message content is required.", required=True)
messages_post_args.add_argument("timestamp", type=inputs.datetime_from_iso8601, help="Time of message is required.", required=True)

messages_get_args = reqparse.RequestParser()
messages_get_args.add_argument("message_id", type=int, help="Message ID.", required=False)
messages_get_args.add_argument("sender_id", type=int, help="ID of sender.", required=False)
messages_get_args.add_argument("recipient_id", type=int, help="ID of recipient.", required=False)

messages_delete_args = reqparse.RequestParser()
messages_delete_args.add_argument("message_id", type=int, help="Message ID is required.", required=True)


