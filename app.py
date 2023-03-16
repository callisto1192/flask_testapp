import sqlite3
from flask import Flask, render_template

app = Flask(__name__)  # Flaskのアプリケーション本体


#データベースのパスを定数で定義
DB_PATH = './testapp.db' # app.py 

@app.route("/")  # / というルートを定義
def hello_world():  # / というルートにリクエストがあったときに実行する関数を定義
    return "<p>Hello, World!</p>"  # レスポンスの内容

@app.route('/sunabaco')
def sunabaco():
    return '<h1>SUNABACO KOZA でFlaskの講義を受講中</h1>'

@app.route('/greet/<name>')
def greet(name):
    return name + 'さん、こんばんは！'
#これが書けたらFlaskサーバーを起動させてブラウザでルートにアクセスして確認

#このサイトに新しいルートを作ってください('/weather<weather>')
#関数名はweather()で引数にweatherを受け取って
#    関数の戻り値として「今日の天気は〇〇です」と表示してみましょう
@app.route('/weather/<weather>')
def weather(weather):
    return '今日の天気は' + weather + 'です'

#テンプレートを使ってリスポンスする
@app.route('/template/test')
def template_test():
    user_name = 'なかがわ'
    user_age = '15'
    return render_template('index.html', user_name=user_name, user_age=user_age)

@app.route('/tasks')
def tasks():
    conn = sqlite3.connect(DB_PATH) #DB接続
    c = conn.cursor() #カーソル起動
    c.execute('SELECT id,name FROM tasks') #SQLクエリを実行
    tasks = []
    for task in c.fetchall():
        tasks.append(
            {
            'id': task[0],
            'name': task[1]
            }
        )
    print(tasks) #ログに表示して確認する
    return render_template('tasks.html', tasks=tasks)


# __name__ というのは、自動的に定義される変数で、現在のファイル(モジュール)名が入ります。 
# ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
if __name__ == '__main__':
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)