from flask import  Flask,make_response

app = Flask(__name__)

@app.route('/health')
def health():
    return make_response({'status': 'ok'}, 200)

@app.route('/notFound')
def not_found():
    return make_response({'message': 'not found'}, 404)

@app.route('/serverError')
def server_error():
    return make_response({'message':'internal error'}, 500)

app.run('0.0.0.0', 500)

if __name__ == "__main__":
    from gevent.pywsgi import WSGIServer
    port = 500
    http_server = WSGIServer(('',port), app)
    print('Started at port: {port}')
    http_server.serve_forever()