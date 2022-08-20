from flask_restful import reqparse

people_get_args = reqparse.RequestParser()
people_get_args.add_argument("person_id", type=int, help="Unique ID for recipient or sender is required.", required=False)
people_get_args.add_argument("first_name", type=str, help="First name of recipient or sender is required.", required=False)
people_get_args.add_argument("last_name", type=str, help="Last name of recipient or sender.", required=False)

people_post_args = reqparse.RequestParser()
people_post_args.add_argument("person_id", type=int, help="Unique ID for recipient or sender is required.", required=True)
people_post_args.add_argument("first_name", type=str, help="First name of recipient or sender is required.", required=True)
people_post_args.add_argument("last_name", type=str, help="Last name of recipient or sender.", required=False)

