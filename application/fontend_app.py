import os
import json
import datetime
from flask import current_app, Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import (current_user, login_required, login_user)
from flask_app import mongodb, db
from helper import get_mongo, send_email
from cerberus import Validator

fontend_app = Blueprint(
    __name__,
    __name__,
    template_folder='../templates',
    static_folder='../static',  # dir path
    static_url_path='/static-content'  # http/web path
)

# A helper that is accessible in templates
@fontend_app.add_app_template_global
def static_resource(asssetPath):
    return url_for('fontend_app.static', filename='theme-1/'+asssetPath)


@fontend_app.route("/")
def route_index():
    return render_template('landing_page.html')


@fontend_app.route("/api/subscriber", methods=['POST'])
def route_post_subscriber():
    db_mongo = get_mongo()
    subscriber = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'created_at': datetime.datetime.now(),
    }

    rules = {
        'name': {'required': True, 'type': 'string', 'empty': False},
        'email': {'required': True, 'type': 'string', 'empty': False},
    }
    v = Validator(rules)
    v.validate(request.form)
    if v.errors:
        return jsonify({"errors": v.errors}), 400

    # insert data into mongo and return success
    db_mongo["subscribers"].insert_one(subscriber)
    resp = {
        "message": "Thank you for subscribing.",
        'name': request.form['name'],
        'email': request.form['email'],
    }
    return jsonify(resp)


@fontend_app.route("/api/subscriber", methods=['GET'])
def route_get_subscriber():
    db_mongo = get_mongo()
    query = {}
    if request.args.get('email'):
        query['email'] = request.args.get('email')
    result = db_mongo["subscribers"].find(query)
    subscribers = []
    for item in result:
        subscribers.append({
            "_id": str(item['_id']),
            "name": item['name'],
            "email": item['email'],
            "created_at": str(item['created_at']),
        })
    return jsonify({"subscribers": subscribers})


@fontend_app.route("/api/survey", methods=['PUT'])
def route_put_survey():
    db_mongo = get_mongo()
    surveyData = {
        'name': request.form.get('name'),
        'position': request.form.get('position'),
        'feedback': request.form.get('feedback'),
        'created_at': datetime.datetime.now(),
    }
    rules = {
        'name': {'required': True, 'type': 'string', 'empty': False},
        'position': {'required': True, 'type': 'string', 'empty': False},
        'feedback': {'required': True, 'type': 'string', 'empty': False},
    }
    v = Validator(rules)
    v.validate(request.form)
    if v.errors:
        return jsonify({"errors": v.errors}), 400

    # insert data into mongo and return success
    db_mongo["surveys"].insert_one(surveyData)
    return jsonify({"message": "Your survey has been received. Thank you."})


@fontend_app.route("/api/survey", methods=['GET'])
def route_get_survey():
    db_mongo = get_mongo()
    result = db_mongo["surveys"].find()
    resp = []
    for item in result:
        resp.append({
            "name": item['name'],
            "position": item['position'],
            "feedback": item['feedback'],
            "created_at": str(item['created_at']),
        })
    return jsonify(resp)


@fontend_app.route("/api/sendemail", methods=['POST'])
def route_post_email():
    rules = {
        'email': {'required': True, 'type': 'string', 'empty': False},
        'message': {'required': True, 'type': 'string', 'empty': False},
    }
    v = Validator(rules)
    v.validate(request.form)
    if v.errors:
        return jsonify({"errors": v.errors}), 400
    send = send_email(request.form['email'], "test", request.form['message'])
    return jsonify({"send": send})


# Swagger doc start
@fontend_app.route('/api/json')
def api_doc_get_json():
    import yaml
    with open("./doc/apidoc.yaml", 'r') as yamlIn, open("./doc/apidoc.json", "w") as jsonOut:
        yamlObj = yaml.safe_load(yamlIn)
        json.dump(yamlObj, jsonOut, indent=4)
        return jsonify(yamlObj)


@fontend_app.route('/api/docs1')
def get_docs1():
    return render_template('swaggerui-theme2.html')


@fontend_app.route('/api/docs2')
def get_docs2():
    return render_template('swaggerui-theme1.html')
# Swagger doc end


# Demo endpoint to debug swagger api
@fontend_app.route("/api/demo-endpoint", methods=['GET', 'POST'])
def route_demo():
    data = {
        'request.headers': dict(request.headers),
        'request.args': dict(request.args),
        'request.json': request.json,
        'request.form': dict(request.form)
    }
    return jsonify({"you send:": data})


@fontend_app.route("/playground")
def route_playground():
    # attach_debugger()
    from schemas.UserSchema import UserSchema
    quotes_schema = UserSchema(many=True)
    # quotes_schema = UserSchema(many=True, only=("id", "email"))
    # result = db.engine.execute("select * from users").first()
    result = db.engine.execute("select * from users")
    result = quotes_schema.dump(result)

    engine_db2 = db.get_engine(current_app, 'db2')
    result = engine_db2.execute("select * from all_cities")
    # result = quotes_schema.dump(result)
    return jsonify(result)


@fontend_app.route("/reactjs-demo")
def route_view_reactjs_demo():
    return render_template('react_page.html', items=[])
