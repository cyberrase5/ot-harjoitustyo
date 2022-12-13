
class Session:
    def __init__(self, user_id=0, degree_id=0):
        self._user_id = int(user_id)
        self._degree_id = int(degree_id)

    def set_vars(self, user_id=0, degree_id=0):
        self._user_id = int(user_id)
        self._degree_id = int(degree_id)


    def logout(self):
        self._user_id = 0
        self._degree_id = 0

session = Session()
