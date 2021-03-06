# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify
from common.libs.Helper import ops_render,iPagination
from common.models.member import Member
from application import app
route_member = Blueprint( 'member_page',__name__ )

@route_member.route( "/index" )
def index():
    resp_data = {}
    req = request.values
    page  = int( req['p'] ) if ( 'p' in req and req['p'] ) else 1
    query = Member.query

    if 'mix_kw' in req:
        query = query.filter( Member.nickname.ilike( "%{0}%".format( req['mix_kw'] ) ) )

    if 'status' in req and int( req['status'] ) > -1 :
        query = query.filter( Member.status == int( req['status'] ) )

    page_params = {
        'total':query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page':page,
        'display':app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace("&p={}".format(page),"")
    }

    pages = iPagination( page_params )
    offset = ( page - 1 ) * app.config['PAGE_SIZE']
    list = query.order_by( Member.id.desc() ).offset( offset ).limit( app.config['PAGE_SIZE'] ).all()
    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['search_con'] = req
    resp_data['current'] = 'index'
    return ops_render( "member/index.html",resp_data )

