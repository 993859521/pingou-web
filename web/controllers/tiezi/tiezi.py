from flask import Blueprint,request,jsonify
from common.libs.Helper import ops_render
from application import app,db
from common.models.tiezi import Tiezi
route_tiezi = Blueprint('tiezi_page', __name__ )
from common.libs.Helper import *
@route_tiezi.route("/cat")
def cat():
    return ops_render("/tiezi/cat.html")

@route_tiezi.route("/cat-set")
def cat_set():
    return ops_render("/tiezi/cat_set.html")

@route_tiezi.route("/index")
def index():
    resp_data = {}
    req = request.values

    page = int(req['page']) if ('page' in req and req["page"]) else 1

    query = Tiezi.query

    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': '/account/index'
    }

    pages = iPagination(page_params)
    offset = (page - 1) * app.config['PAGE_SIZE']
    limit = app.config['PAGE_SIZE'] * page

    list = query.order_by(Tiezi.id.desc()).all()[offset:limit]

    resp_data['list'] = list
    resp_data['pages'] = pages
    return ops_render("/tiezi/index.html", resp_data)

@route_tiezi.route("/info")
def info():
    return ops_render("/tiezi/info.html")

@route_tiezi.route("/set")
def set():
    return ops_render("/tiezi/set.html")
@route_tiezi.route("/ops",methods = [ "POST" ])
def ops():
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    id = req['id'] if 'id' in req else 0
    act = req['act'] if 'act' in req else ''
    if not id :
        resp['code'] = -1
        resp['msg'] = "请选择要操作的账号~~"
        return jsonify(resp)
    if  act not in [ 'remove','recover' ] :
        resp['code'] = -1
        resp['msg'] = "操作有误，请重试~~"
        return jsonify(resp)
    user_info = Tiezi.query.filter_by( id = id ).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "指定账号不存在~~"
        return jsonify(resp)
    if act == "remove":
        user_info.status = 0
    elif act == "recover":
        user_info.status = 1

    if user_info and user_info.id == 1:
        resp['code'] = -1
        resp['msg'] = "该用户是演示账号，不准操作账号~~"
        return jsonify(resp)
    db.session.add(user_info)
    db.session.commit()
    return jsonify(resp)