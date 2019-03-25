from user import User

my_user = User('jose@schoolofcode.me', 'Jose', 'Smith', None)
my_user.save_to_db()

# my_user = User.load_from_db_by_email('jose@schooolofcode.me')
# print(my_user)

user_from_db = User.load_from_db_by_email('jose@schooolofcode.me')

print(user_from_db)