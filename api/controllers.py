from config import settings
from services.test_service import execute


# test api controller
def test_view():
    execute()
    return "200 OK"


# index config controller
def index_controller():
    print(settings.getall())
    return "200 OK"
