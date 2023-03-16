from flask import Flask

app = Flask(__name__)  # Flaskのアプリケーション本体

@app.route("/")  # / というルートを定義
def hello_world():  # / というルートにリクエストがあったときに実行する関数を定義
    return "<p>Hello, World!</p>"  # レスポンスの内容

@app.route('/sunabaco')
def sunabaco():
    return '<h1>SUNABACO KOZA でFlaskの講義を受講中</h1>'

# __name__ というのは、自動的に定義される変数で、現在のファイル(モジュール)名が入ります。 
# ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
if __name__ == '__main__':
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)