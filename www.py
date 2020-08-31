# -*- coding: utf-8 -*-
from application import app
from web.controllers.index import route_index
from web.controllers.static import route_static
from web.controllers.user.user import route_user
from web.controllers.index import route_index
from web.controllers.account.account import route_account
from web.controllers.tiezi.tiezi import route_tiezi
from web.controllers.member.Member import route_member
from web.controllers.api import route_api
from web.interceptor.AuthInterceptor import *
app.register_blueprint( route_index,url_prefix = "/" )
app.register_blueprint( route_static,url_prefix = "/static" )
app.register_blueprint( route_api,url_prefix = "/api" )
app.register_blueprint( route_user,url_prefix = "/user" )
app.register_blueprint(route_account,url_prefix="/account")
app.register_blueprint(route_tiezi,url_prefix="/tiezi")
app.register_blueprint(route_member,url_prefix="/member")
