from flask import  Blueprint
route_api=Blueprint('ipage_page',__name__ )
from web.controllers.api.Member import *
from web.controllers.api.tiezi import *
from web.controllers.api.louceng import *
from web.controllers.api.picture import *
@route_api.route("/")
def index():
    return "api-1.0"