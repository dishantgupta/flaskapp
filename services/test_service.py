from dbmodels.user import User


# test service
def execute():
    user = User("dishant", "dishant.gupta@cars24.com")
    user.save()
    print(1)
