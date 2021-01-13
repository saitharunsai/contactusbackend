from flask import Flask, jsonify, request
from datetime import datetime
from models import db, contact_form
from flask_cors import CORS
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:saitharun@123@localhost/assig'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)


def addform(firstName, lastName, message, email):
    if(firstName and lastName and message and email):
        try:
            data = contact_form(firstName, lastName, message, email)
            db.session.add(data)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False


@app.route('/api/contactus', methods=['POST'])
def new_form():
    try:
        firstName = request.json["firstName"]
        lastName = request.json["lastName"]
        email = request.json["email"]
        message = request.json["message"]
        addform(firstName, lastName, message, email)
        return jsonify({'status': 'successful'}, 200)
    except Exception as e:
        print(e)
        return jsonify({"error": e})


@app.route('/api/getAnalytics', methods=['POST'])
def send_from():
    mindate = request.json['mindate']
    maxdate = request.json['maxdate']

    formsid = {}
    posts = contact_form.query.filter(contact_form.date_posted >= mindate).filter(
        contact_form.date_posted <= maxdate)
    for j in posts:
        if j.date_posted.strftime("%m/%d/%Y") in formsid.keys():
            formsid[j.date_posted.strftime("%m/%d/%Y")] += 1
        else:
            formsid.update({j.date_posted.strftime("%m/%d/%Y"): 1})
    return jsonify(formsid)


if __name__ == '__main':
    app.run()
