from web.controllers.api import route_api
from  flask import request,jsonify,g
from application import  app,db
from common.models.louceng import Louceng
from common.models.tiezi import Tiezi
from common.models.member import Member
from common.libs.Helper import *
from sqlalchemy import  or_
from common.libs.UrlManager import *
@route_api.route("/louceng/index" ,methods = [ "GET","POST" ])
def loucengindex():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    id = req['id'] if 'id' in req else 0
    Louceng_info = Louceng.query.filter_by( tieziid=id).order_by( Louceng.tieziid.asc() ).all()

    data_Tiezi_list = []
    if Louceng_info:
        for item in Louceng_info:
            Member_list = Member.query.filter_by(id=item.owner).first()
            tmp_data = {
                'id': item.id,
                'feed_source_name': Member_list.nickname,
                'images':Member_list.avatar,
                'context': "%s" % (item.Context),
                'created_time': str(item.created_time),
            }
            data_Tiezi_list.append(tmp_data)

    resp['data']['list'] = data_Tiezi_list
    return  jsonify(resp)
@route_api.route("/louceng/add" ,methods = [ "GET","POST" ])
def loucneg_add():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    tieziid = req['tieziid'] if 'tieziid' in req else ''
    Context = req['Context'] if 'Context' in req else ''
    owner = req['owner'] if 'owner' in req else ''
    model_member = Louceng()
    model_member.tieziid = tieziid
    model_member.Context = Context
    model_member.owner = owner
    model_member.created_time = getCurrentDate()
    db.session.add(model_member)
    db.session.commit()
    user_info = Tiezi.query.filter_by(id=tieziid).first()
    if user_info:
        model_user = user_info
        model_user.lcnum=model_user.lcnum+1
        db.session.add(model_user)
        db.session.commit()
    return jsonify(resp)