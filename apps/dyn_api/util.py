import inspect
import importlib
import json
import sys

from functools import wraps
import jwt
from flask import request, current_app
from flask import current_app
from apps.authentication.models import Users
from datetime import datetime

from apps import db
from apps.config import REGISTER_MODEL_MODULE 

from wtforms import Form
from wtforms_alchemy import model_form_factory
ModelForm = model_form_factory(Form)

class Utils:
    @staticmethod
    def add_row_to_db(obj, manager: db.Query):
        manager.session.add(obj)
        manager.session.commit()

    @staticmethod
    def remove_rows_from_db(rows, manager: db.Query):
        rows.delete()
        manager.session.commit()

    @staticmethod
    def commit_changes(manager: db.Query):
        db.session.commit()

    @staticmethod
    def get_class(config, name: str) -> db.Model:
        return Utils.model_name_to_class(config[name])

    @staticmethod
    def get_manager(config, name: str) -> db.Query:
        return Utils.get_class(config, name).query

    @staticmethod
    def get_form(config, name: str) -> ModelForm:
        class ThisClassForm(ModelForm):
            class Meta:
                model = Utils.get_class(config, name)

        return ThisClassForm

    @staticmethod
    def model_name_to_class(name: str):
        '''
        all_classes = inspect.getmembers(sys.modules[REGISTER_MODEL_MODULE], inspect.isclass)
        for cls in all_classes:
            if cls[0] == name:
                return cls[1]
        raise Exception(f'Wrong model name ({name}) in config!')
        '''
        module_name = '.'.join(name.split('.')[:-1])
        class_name = name.split('.')[-1]

        module = importlib.import_module(module_name)
        return getattr(module, class_name)
            
    @staticmethod
    def init_function(config, model_name):
        return Utils.get_manager(config, model_name),\
               Utils.get_class(config, model_name),\
               Utils.get_form(config, model_name)

    @staticmethod
    def standard_request_body(request):
        try:
            body_of_req = request.form
            if not body_of_req:
                raise Exception()
        except Exception:
            if len(request.data) > 0:
                body_of_req = json.loads(request.data)
            else:
                body_of_req = {}
        return body_of_req

def generate_token( aUserId ):

    now = int(datetime.utcnow().timestamp())
    api_token = jwt.encode(
        {"user_id": aUserId,
            "init_date": now},
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return api_token

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        else:
            return {
                       'message': 'Token is missing',
                       'data': None,
                       'success': False
                   }, 403
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Users.query.filter_by(id=data['user_id']).first()
            if current_user is None:
                return {
                           'message': 'Invalid token',
                           'data': None,
                           'success': False
                       }, 403
            now = int(datetime.utcnow().timestamp())
            init_date = data['init_date']
            
            #if now - init_date > 24 * 3600:  # expire token after 24 hours
            #    return {
            #               'message': 'Expired token',
            #               'data': None,
            #               'success': False
            #           }, 403
        
        except Exception as e:
            return {
                       'message': str(e),
                       'data': None,
                       'success': False
                   }, 500
        return func(*args, **kwargs)

    return decorated