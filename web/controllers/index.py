# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
from common.models.tiezi import Tiezi
from common.models.member import Member
from common.libs.Helper import ops_render
route_index = Blueprint( 'index_page',__name__ )

@route_index.route("/")
@route_index.route("/")
def index():
    resp_date = {}
    query1 = Tiezi.query
    query = Member.query
    info = {
    'tiezi':query1.count(),
    'member':query.count(),
       }

    resp_date['info'] = info
    return ops_render("index/index.html",resp_date)