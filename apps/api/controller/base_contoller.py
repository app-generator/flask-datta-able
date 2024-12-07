import flask
import traceback 
from flask import jsonify
from apps.api.exception import InvalidUsage

app = flask.current_app

class BaseController:

    # Set Json response
    def send_response(self, data, status_code=200):
        res = {
            "data": data,
            'status': status_code
        }
        resp = jsonify(res)
        return resp


    # Set success response.
    def success(self, data, message ="", code =200):
        """form final respose format

        Args:
            data (dict/list): for single record it would be dictionary and for multiple records it would be list.
            message (str): operation response message. Defaults to "".
            code (int): Http response code. Defaults to 200.

        Returns:
            dictionary of response data
            {
                data: [],
                message: "",
                status: 200,
            }
        """
        res = {
            "data": data,
            "message": message,
            'status': code
        }
        resp = jsonify(res)
        return resp

    # Set error response.
    def error(self, e, code=422):
        msg = str(e)
        if isinstance(e, InvalidUsage):
            msg = e.message

        # app.logger.error(traceback.format_exc())
        res = {
            # 'error':{
            #     'description': traceback.format_exc()
            # },
            "message": msg,
            'status': code
        }
        return res, code


    def errorGeneral(self, e, code=422):
        msg = str(e)
        if isinstance(e, InvalidUsage):
            msg = e.message
        res = {
            "message": msg,
            'status': code
        }
        return res, code
        # msg = 'An exception occurred: {}'.format(error)
        # res = {
        #     'errors':msg,
        #     'status': code
        # }
        # return res


    def simple_response(self, message, status_code):
        res = {
            "message": message,
            'status': status_code
        }
        resp = jsonify(res)
        return resp
