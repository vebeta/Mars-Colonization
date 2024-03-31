from flask_restful import reqparse

parser = reqparse.RequestParser()
# parser.add_argument('title', required=True)
# parser.add_argument('content', required=True)
# parser.add_argument('is_private', required=True, type=bool)
# parser.add_argument('is_published', required=True, type=bool)
# parser.add_argument('user_id', required=True, type=int)


parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)