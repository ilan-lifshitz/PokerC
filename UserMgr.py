from User import User


class UserMgr:
    def __init__(self):
        self.user_list = [];

    def add_user(self, user):
        self.user_list.append(user)

    def del_user(self, user):
        self.user_list.remove(self, user)

    def get_user(self, name):
        for user in self.user_list:
            if user.get_name() == name:
                return user

    def print(self):
        i = 0;
        print("num of users: ", len(self.user_list))
        for user in self.user_list:
            i = i+1
            print("user - ",i)
            user.print()


user_mgr = UserMgr()
user_1 = User("Itai")
user_mgr.add_user(user_1)
user_2 = User("Ilan")
user_mgr.add_user(user_2)
#print(User.global_var)
user_mgr.print()