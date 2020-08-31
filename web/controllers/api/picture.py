from web.controllers.api import route_api
from  flask import request,jsonify
from common.libs.Helper import *
from application import os,app
from common.libs.UrlManager import *
import datetime
import random


@route_api.route("/picture/index",methods = [ "GET","POST" ])
def picture_index():

    file_obj = request.files.get("file")  # "pic"对应前端表单name属性
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"
    url=create_uuid(file_obj.filename)
    file_obj.save(os.getcwd()+"/web/static/images/upload/"+url+".jpg")
    resp=UrlManager.buildPictureUrl(url)

    return  resp
def create_uuid(self): #生成唯一的图片的名称字符串，防止图片显示时的重名问题
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S"); # 生成当前时间
    randomNum = random.randint(0, 100); # 生成的随机整数n，其中0<=n<=100
    if randomNum <= 10:
      randomNum = str(0) + str(randomNum);
    uniqueNum = str(nowTime) + str(randomNum);
    return uniqueNum;
