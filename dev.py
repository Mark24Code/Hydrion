from app import create_app

app = create_app('development')


@app.route('/')
def index():
    return 'Hello flask!'


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])
