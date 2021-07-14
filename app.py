from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_resive = request.form['name_give']
    num_resive = request.form['num_give']
    address_resive = request.form['address_give']
    phone_resive = request.form['phone_give']

    doc = {'name': name_resive,
           'num': num_resive,
           'address': address_resive,
           'phone': phone_resive
           }
    db.shopping.insert_one(doc)
    print(doc)
    return jsonify({'msg': '이 요청은 POST!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    shoplist = list(db.shopping.find({}, {'_id': False}))
    print(shoplist)
    return jsonify({'all_list': shoplist})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8088, debug=True)
