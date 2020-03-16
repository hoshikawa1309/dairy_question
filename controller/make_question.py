from model.user import User

def dairy_question(id):
    user = User(id)
    user.get_max_rate()
    user.get_question()
    # user.show_info()
