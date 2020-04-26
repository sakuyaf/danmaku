from config import db
import pymysql
import ahocorasick

con=pymysql.connect(db['host'],db['user'],db['passwd'],db['database'],charset='utf8')
cursor=con.cursor()


class AhocorasickNer:
    def __init__(self, user_dict_path):
        self.user_dict_path = user_dict_path
        self.actree = ahocorasick.Automaton()

    def add_keywords(self):
        flag = 0
        with open(self.user_dict_path, "r", encoding = 'GBK') as file:
            for line in file:
                word, flag = line.strip(), flag + 1
                self.actree.add_word(word, (flag, word))
        self.actree.make_automaton()

        def get_ner_results(self, sentence):
            ner_results = []
            # i的形式为(index1,(index2,word))
            # index1: 提取后的结果在sentence中的末尾索引
            # index2: 提取后的结果在self.actree中的索引
            for i in self.actree.iter(sentence):
                ner_results.append((i[1], i[0] + 1 - len(i[1][1]), i[0] + 1))
            return ner_results

if True:
    ahocorasick_ner = AhocorasickNer(user_dict_path="sensitive.txt")
    ahocorasick_ner.add_keywords()

def registerCheck(username, pwd1, pwd2):
    cursor.rowcount = cursor.execute('select username from users where username = %s', (username,))
    if not pwd1 == pwd2:
        # return False
        return {
            'errcode': 401,
            'errmsg':'密码与重复密码不一致',
        }
    elif cursor.rowcount is 1:
        # return False
        return {
            'errcode':401,
            'errmsg':'用户名已经存在',
        }
    else:
        # return True
        # noinspection PyBroadException
        try:
            cursor.execute('insert into users (username, password),VALUES (%s,%s)',(username,pwd1))
            con.commit()
            return {
                'errcode':500,
                'errmsg':'注册成功',
            }
        except:
            return {
                'errcode':500,
                'errmsg':'服务端数据插入失败',
            }

def loginCheck(username,pwd):
    cursor.rowcount = cursor.execute('select * from users where username = %s,password = %s', (username, pwd))
    if not cursor.rowcount is 1:
        return {
            'errcode':500,
            'errmsg':'不存在该用户，或密码用户名错误',
        }
    else:
        return{
            'errcode':500,
            'errmsg':'登录成功',
        }

def getMessage():
    #这里是同时返回用户，时间，弹幕
    try:
        cursor.execute('select * from message')
        return cursor.fetchall()
    except:
        print("提取弹幕出错")
    # ###这里是只返回弹幕
    # try:
    #     cursor.execute('select content from message')
    #     return cursor.fetchall()
    # except:
    #     print("提取弹幕出错")

def insertMessage(username,content,nowTime):
    try:
        cursor.execute('insert into message (username,content,nowTime),values (%s,%s,%s)',(username,content,nowTime))
        con.commit()
        return True
    except:
        return False

def judgekey(content):
    res = ahocorasick_ner.get_ner_results(content)
    for i in res:
        head = i[1]
        tail = i[2]-1
        while head <= tail:
            content[head]='*'
            head = head + 1
    return content