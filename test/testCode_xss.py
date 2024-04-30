from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/lgin')
def lgin():

    first_name = request.args.get('name', '')
    return make_response("Your name==" + first_name )
