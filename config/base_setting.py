SERVER_PORT=8080
SQLALCHEMY_DATABASE_URI='mysql://ceshi:123456@203.195.152.203/pingou'
SQLALCHEMY_TRACK_MODIFICATIONS=False
AUTH_COOKIE_NAME="[PING_GOU"
IGNORE_URLS={
    "^/user/login"
}
IGNORE_CHECK_LOGIN_URLS={
    "^/static",
    "^/favicon.ico"
}
API_IGNORE_URLS = [
    "^/api"
]
MINA_APP = {
    'appid':'wxb60faade60a66757',
    'appkey':'b1251b3bf61f7c9964f461d7317d6ecc',
}
PAGE_SIZE = 50
PAGE_DISPLAY = 10
STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}