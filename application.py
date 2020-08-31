from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from common.libs.UrlManager import UrlManager

import os
class Application( Flask ):
    def __init__(self,import_name,template_folder=None,root_path=None):
        super( Application,self ).__init__( import_name ,template_folder=template_folder,root_path=root_path,static_folder=None)
        self.config.from_pyfile( 'config/base_setting.py' )
        if "ops_config" in os.environ:
            self.config.from_pyfile( 'config/%s_setting.py'%os.environ['ops_config'] )

        db.init_app( self )
db = SQLAlchemy()#数据库初始化

app = Application( __name__,os.getcwd()+"/web/templates/" ,root_path=os.getcwd())#templates目录自定义，根目录自定义
manager = Manager( app )

app.config['JSON_AS_ASCII'] = False #防止乱码
app.add_template_global(UrlManager.buildUrl,'buildUrl')
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')