from web.controllers.api import route_api
from  flask import request,jsonify,g
from application import  app,db
from common.models.tiezi import Tiezi
from common.models.tiezi_type import TieziType
from common.models.member import Member
from sqlalchemy import  or_
from common.libs.Helper import *
from application import app



@route_api.route("/tiezi/search" ,methods = [ "GET","POST" ])
def tiezi_Search():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    type = int( req['type'] ) if 'type' in req else 0
    mix_kw = str(req['mix_kw']) if 'mix_kw' in req else ''
    p = int( req['p'] ) if 'p' in req else 1
    if p < 1:
        p = 1
    page_size = 8
    app.logger.info(p)
    offset = ( p - 1 ) * page_size
    query = Tiezi.query.filter_by(status=1)
    if type > 0:
        query = query.filter_by(type = type)
    if mix_kw:
        rule = or_(Tiezi.title.ilike("%{0}%".format(mix_kw)), Tiezi.context.ilike("%{0}%".format(mix_kw)))
        query = query.filter(rule)
    tiezi_list=query.order_by(Tiezi.id.desc()).slice(offset,offset+page_size).all()
    data_tiezi_list = []

    if tiezi_list:
        for item in tiezi_list:
            Member_list = Member.query.filter_by(id=item.owner).first()
            images_list=item.images.split("#")
            c=[]

            for i in images_list:
                if i:
                    tmc_data = {
                        'images': i
                    }
                    c.append(tmc_data)
            tmp_data = {
                'id': item.id,
                'answer_id': item.id,
                'images': Member_list.avatar,
                'title': "%s"%( item.title ),
                'feed_source_name': Member_list.nickname,
                'type': str(item.type),
                'context': item.context,
                'lcnum': str(item.lcnum),
                'images_list':c
            }
            data_tiezi_list.append(tmp_data)
    resp['data']['list'] = data_tiezi_list
    resp['data']['has_more'] = 0 if len( data_tiezi_list ) < page_size else 1
    return jsonify(resp)
@route_api.route("/tiezi/add" ,methods = [ "GET","POST" ])
def add():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    app.logger.info(req)
    title = req['title'] if 'title' in req else ''
    id = req['id'] if 'id' in req else ''
    status = req['status'] if 'status' in req else 1
    type = req['type'] if 'type' in req else 0
    context = req['context'] if 'context' in req else ''
    images = req['images'] if 'images' in req else ''
    app.logger.info(title)
    model_member = Tiezi()
    model_member.title = title
    model_member.owner = id
    model_member.status = status
    model_member.type = type
    model_member.context = context
    model_member.created_time = getCurrentDate()
    model_member.lcnum = 0
    model_member.images = images
    db.session.add(model_member)
    db.session.commit()
    return jsonify(resp)