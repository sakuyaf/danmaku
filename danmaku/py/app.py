from flask import Flask,Response,request
from database import registerCheck,loginCheck,getMessage,insertMessage,judgekey,AhocorasickNer
from flask_socketio import SocketIO
import config
import datetime

app = Flask(__name__)
socketio = SocketIO(app)
app.config['SECRET_KEY'] = config.app['secret_key']

#注册
@app.route('/register',methods=['get','post'])
def users_register():
    username = request.get_data('username')
    pwd1 = request.get_data('password')
    pwd2 = request.get_data('comfirm_password')
    return registerCheck(username, pwd1, pwd2)

#登录
@app.route('/login',methods=['get','post'])
def users_login():
    username = request.get_data('username')
    pwd = request.get_data('password')
    return loginCheck(username, pwd)

#历史弹幕展示
@app.route('/message',methods=['get','psot'])
def main_message():
    _list = getMessage()
    return Response(_list,content_type=tuple)

#实时弹幕展示
@socketio.on('connect')
def inter_massage():
    while True:
#       content = request.get_data('danmuku')
#在这里对弹幕进行关键词屏蔽
        content = judgekey(request.get_data('danmuku'))
        username = request.get_data('username')
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if insertMessage(username,content,nowTime):
            # return {
            #     'errcode': 500,
            #    'errmsg' : "success"
            # }
            socketio.emit('sever_event',
                          {'username':username,
                           'danmuku': content,
                           'date': nowTime,
                           'errcode':500,
                           'errmsg':True},
                          broadcast=True)
        else:
            return  {
                'errcode' : '502',
                'errmsg' :  False
            }

if __name__ == '__main__':
    socketio.run(app)

