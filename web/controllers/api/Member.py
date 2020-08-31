from web.controllers.api import route_api
from  flask import request,jsonify,g
from application import  app,db
from common.models.tiezi_type import TieziType
from common.models.member import Member
from common.libs.member.MemberService import MemberService
from common.libs.Helper import *
@route_api.route("/member/login",methods = [ "GET","POST" ])
def login():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    code = req['code'] if 'code' in req else ''
    if not code or len(code) < 1:
        resp['code'] = -1
        resp['msg'] = "需要code"
        return jsonify(resp)
    openid = MemberService.getWeChatOpenId(code)
    if openid is None:
        resp['code'] = -1
        resp['msg'] = "调用微信出"
        return jsonify(resp)

    nickname = req['nickName'] if 'nickName' in req else ''
    sex = req['gender'] if 'gender' in req else 0
    avatar = req['avatarUrl'] if 'avatarUrl' in req else ''
    city = req['city'] if 'avatarUrl' in req else ''
    '''
        判断是否已经测试过，注册了直接返回一些信息
    '''
    bind_info = Member.query.filter_by(openid=openid).first()
    app.logger.info(bind_info)
    if not bind_info:
        model_member = Member()
        model_member.nickname = nickname
        model_member.sex = sex
        model_member.avatar = avatar
        model_member.salt = MemberService.geneSalt()
        model_member.created_time = getCurrentDate()
        model_member.openid = openid
        model_member.reg_ip = request.remote_addr
        model_member.city = city
        db.session.add(model_member)
        db.session.commit()
    bind_info = Member.query.filter_by(openid=openid).first()
    token = "%s#%s" % (MemberService.geneAuthCode(bind_info), bind_info.id)
    mes = {
        'id': bind_info.id,
        'nickname': bind_info.nickname,
        'sex': bind_info.sex,
        'reg_ip': bind_info.reg_ip,
        'created_time': bind_info.created_time,
        'avatar': bind_info.avatar,
        'city':bind_info.city
    }
    resp['data'] = {'token': token}
    resp['data']['list'] = mes
    return jsonify(resp)
@route_api.route("/member/check-reg",methods = [ "GET","POST" ])
def checkReg():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    code = req['code'] if 'code' in req else ''
    if not code or len(code) < 1:
        resp['code'] = -1
        resp['msg'] = "需要code"
        return jsonify(resp)

    openid = MemberService.getWeChatOpenId(code)
    if openid is None:
        resp['code'] = -1
        resp['msg'] = "调用微信出错"
        return jsonify(resp)



    member_info = Member.query.filter_by( openid=openid).first()
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "未查询到绑定信息"
        return jsonify(resp)

    token = "%s#%s"%( MemberService.geneAuthCode( member_info ),member_info.id )
    cat_list = TieziType.query.filter_by(status=1).all()
    data_cat_list = []
    if cat_list:
        for item in cat_list:
            tmp_data = {
                'id':item.id,
                'name':item.name
            }
            data_cat_list.append( tmp_data  )
    mes={
        'id':member_info.id,
        'nickname':member_info.nickname,
        'sex':member_info.sex,
        'reg_ip':member_info.reg_ip,
        'created_time':member_info.created_time,
        'avatar': member_info.avatar,
        'city': member_info.city
    }
    resp['data'] = { 'token':token }
    resp['data']['list'] = mes
    resp['data']['tlist'] = data_cat_list
    return jsonify(resp)
