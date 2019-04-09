from flask import Blueprint

from api.controllers import test_view
from api.controllers import index_controller


bp = Blueprint('url_register', __name__)


# index controller
bp.add_url_rule("/", view_func=index_controller, methods=['GET'])

# test api url view binding
bp.add_url_rule("/api/v1/test", view_func=test_view, methods=['GET'])
