from user import User
from database import Database

# print(Database.connection_pool)
# my_object = Database()
# my_object.initialise()
#
# print(Database.connection_pool)

Database.initialise(database="learning", host='localhost', user='postgres', password="1234", port=5433)

my_user = User('jose@schoolofcode.me', 'Jose', 'Smith', None)


my_user.save_to_db()

# my_user = User.load_from_db_by_email('jose@schooolofcode.me')
# print(my_user)

user_from_db = User.load_from_db_by_email('jose@schooolofcode.me')

print(user_from_db)